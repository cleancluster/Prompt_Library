
import streamlit as st
import json

# Load prompt data
with open("prompt_library.json", "r") as f:
    prompt_data = json.load(f)

st.set_page_config(layout="wide")
st.title("📚 Prompt Library")

# Sidebar navigation
categories = list(prompt_data.keys())
selected_category = st.sidebar.selectbox("Choose a category", categories)

subcategories = list(prompt_data[selected_category].keys())
selected_subcategory = st.sidebar.selectbox("Choose a subcategory", subcategories)

prompt_entry = prompt_data[selected_category][selected_subcategory]

# Display selected prompt
st.header(f"📂 {selected_category} → 🧠 {selected_subcategory}")
st.markdown(f"**Summary:** {prompt_entry['summary']}")
st.code(prompt_entry['prompt'], language='markdown')
st.button("📋 Copy Prompt", key=selected_subcategory)

st.markdown("---")
st.info("Use your mouse to select and copy prompts. 'Copy' button is visual-only (no clipboard JS).")
