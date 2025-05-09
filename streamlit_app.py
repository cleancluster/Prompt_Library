
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

prompts = prompt_data[selected_category][selected_subcategory]

# Display prompts
st.header(f"{selected_category} → {selected_subcategory}")

for item in prompts:
    with st.expander(f"🧠 {item['problem']}"):
        st.code(item['prompt'], language='markdown')
        st.button("📋 Copy Prompt", key=item['problem'])  # UI-only button; copy by selecting

st.markdown("---")
st.info("Use your mouse to select and copy prompts. 'Copy' button is visual-only (no clipboard JS).")
