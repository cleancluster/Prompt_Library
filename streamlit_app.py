import streamlit as st
import json

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

# Clipboard copy button using JS
st.markdown(f"""
    <button onclick="navigator.clipboard.writeText(`{prompt_entry['prompt'].replace('`', '\\`')}`)" 
        style="margin-top: 10px; padding: 0.5em 1em; background-color: #f4f4f4; border: 1px solid #ccc; border-radius: 6px; cursor: pointer;">
        📋 Copy Prompt
    </button>
""", unsafe_allow_html=True)

# Footer note
st.markdown("---")
st.info("Click the button above or highlight the text manually to copy the prompt.")
