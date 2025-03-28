import streamlit as st
import requests

API_URL = "http://localhost:8000/generate-content"  # Change this to your deployed FastAPI endpoint if needed

st.title("🧠 Content Generator Demo")

st.markdown("Enter a URL and a topic to generate formatted MDX content using your AI agent.")

# Input fields
url = st.text_input("📎 Enter URL")
topic = st.text_input("📝 Enter Topic")

# When the button is clicked
if st.button("🚀 Generate Content"):
    if not url or not topic:
        st.warning("Please enter both URL and Topic.")
    else:
        with st.spinner("Generating content..."):
            try:
                response = requests.post(API_URL, json={"url": url, "topic": topic})
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Content generated successfully!")

                    st.markdown("### 🧾 Preview of Generated MDX")
                    st.code(data["mdx_content"], language="mdx")

                    # Optional download
                    st.download_button("💾 Download MDX File", data["mdx_content"], file_name="generated_content.mdx", mime="text/markdown")
                else:
                    st.error(f"Error: {response.status_code} — {response.text}")
            except Exception as e:
                st.error(f"Exception occurred: {str(e)}")
