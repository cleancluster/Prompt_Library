import streamlit as st
import json
import html
import streamlit.components.v1 as components

# Load prompt data
with open("prompt_library.json", "r") as f:
    prompt_data = json.load(f)

st.set_page_config(layout="wide")
st.markdown("<h1 style='font-size: 2.4rem;'>📚 Prompt Library</h1>", unsafe_allow_html=True)

# Sidebar navigation
categories = list(prompt_data.keys())
selected_category = st.sidebar.selectbox("📂 Choose a category", categories)

subcategories = list(prompt_data[selected_category].keys())
selected_subcategory = st.sidebar.selectbox("🧠 Choose a subcategory", subcategories)

prompt_entry = prompt_data[selected_category][selected_subcategory]

# Display header and summary
st.markdown(f"<h3 style='margin-bottom: 0.2em;'>📂 {selected_category} → 🧠 {selected_subcategory}</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 1.1rem; margin-top: 0.5em;'><strong>Summary:</strong> {prompt_entry['summary']}</p>", unsafe_allow_html=True)

# Prompt content
st.code(prompt_entry["prompt"], language="markdown")

# Escape backticks and double quotes for JS safety
js_safe_prompt = prompt_entry["prompt"].replace("`", "\\`").replace('"', '\\"').replace("\n", "\\n")

# Optional example thread link (if present in JSON)
if "example_link" in prompt_entry:
    st.markdown(
        f"[🔗 View ChatGPT Example Thread]({prompt_entry['example_link']})",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<span style='color: #888;'>No example thread available yet.</span>",
        unsafe_allow_html=True
    )

# Copy button as before
components.html(f"""
    <div style="margin-top: 10px;">
        <button id="copy-btn"
            style="padding: 0.5em 1em; background-color: #f4f4f4; border: 1px solid #ccc; border-radius: 6px; cursor: pointer;">
            📋 Copy Prompt
        </button>
        <script>
            const btn = document.getElementById("copy-btn");
            btn.addEventListener("click", function() {{
                navigator.clipboard.writeText("{js_safe_prompt}");
                btn.innerText = "✅ Copied!";
                setTimeout(() => btn.innerText = "📋 Copy Prompt", 2000);
            }});
        </script>
    </div>
""", height=60)


