from typing import Dict, Any
from datetime import datetime
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage


class FormatterAgent:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="""
You are a markdown-to-MDX formatting agent. Convert the content into valid `.mdx`.

Rules:
- Add YAML frontmatter at the top, wrapped in triple dashes `---`.
- Frontmatter includes: `title`, `date`, and `topic`.
- The `title` value must be in double quotes.
- Add a blank line after frontmatter.
- Use `##` for headings and fenced code blocks with language (e.g., ```python).
- DO NOT wrap the entire response in triple backticks.
- Return only valid `.mdx` content.
"""),
            ("human", "Content:\n{content}\n\nTitle: {title}\nDate: {date}\nTopic: {topic}\n\nFormat this into MDX.")
        ])

    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # Step 1: Extract input state safely
        title = state.get("title", "Untitled")
        date = state.get("date", datetime.today().strftime("%Y-%m-%d"))
        topic = state.get("topic", "General")
        content = state.get("reviewed_content", "")

        print("🚀 Formatter started")

        # Step 2: Format the prompt
        messages = self.prompt.format_messages(
            content=content,
            title=title,
            date=date,
            topic=topic
        )

        # Step 3: Call the LLM
        response = await self.llm.ainvoke(messages)
        raw_response = getattr(response, "content", None)

        # Step 4: Safely parse and clean the response
        mdx_content = ""

        if raw_response and isinstance(raw_response, str) and raw_response.strip():
            mdx_content = raw_response.strip()

            # Remove ```mdx wrapper if present
            if mdx_content.startswith("```mdx") and mdx_content.endswith("```"):
                mdx_content = mdx_content[len("```mdx"):-3].strip()

            # Ensure blank line after frontmatter (avoid table rendering)
            if mdx_content.startswith("---"):
                parts = mdx_content.split("---")
                if len(parts) >= 3:
                    frontmatter = "---" + parts[1] + "---\n\n"
                    rest = "---".join(parts[2:]).lstrip()
                    mdx_content = frontmatter + rest
        else:
            print("⚠️ LLM returned empty or invalid content. Using empty fallback.")
            mdx_content = ""

        # Step 5: Optional — Save output to file for debugging
        with open("output.mdx", "w", encoding="utf-8") as f:
            f.write(mdx_content)

        # Step 6: Triple-check for Pydantic validation
        if mdx_content is None:
            print("❌ mdx_content is None — forcing empty string.")
            mdx_content = ""
        elif not isinstance(mdx_content, str):
            print(f"❌ mdx_content is type {type(mdx_content)} — converting to string.")
            mdx_content = str(mdx_content)

        status = "success" if mdx_content.strip() else "empty"

        # Step 7: Log before returning
        print("✅ Final MDX content preview:\n", repr(mdx_content[:300]), "...\n")
        print("✅ Returning ContentResponse with status:", status)

        return {
            "formatted_content": mdx_content
        }
