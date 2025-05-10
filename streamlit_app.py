import streamlit as st
import json
import html
import streamlit.components.v1 as components

# Load bilingual prompt data
with open("prompt_library_bilingual.json", "r") as f:
    prompt_data = json.load(f)

st.set_page_config(layout="wide")

# Language selector
language = st.sidebar.radio("Choose Language / Vælg Sprog", ["English", "Dansk"])

# Extract translated labels
def t(en, da):
    return en if language == "English" else da

st.markdown(f"<h1 style='font-size: 2.4rem;'>📚 {t('Prompt Library', 'Promptbibliotek')}</h1>", unsafe_allow_html=True)

# Sidebar navigation
categories = list(prompt_data.keys())
category_labels = [prompt_data[cat]["meta"][language] for cat in categories]
category_map = dict(zip(category_labels, categories))

selected_category_label = st.sidebar.selectbox(t("\ud83d\udcc2 Choose a category", "\ud83d\udcc2 Vælg en kategori"), category_labels)
selected_category = category_map[selected_category_label]

subcategories = list(prompt_data[selected_category]["subcategories"].keys())
subcategory_labels = [prompt_data[selected_category]["subcategories"][sub]["meta"][language] for sub in subcategories]
subcategory_map = dict(zip(subcategory_labels, subcategories))

selected_subcategory_label = st.sidebar.selectbox(t("\ud83e\udde0 Choose a subcategory", "\ud83e\udde0 Vælg en underkategori"), subcategory_labels)
selected_subcategory = subcategory_map[selected_subcategory_label]

prompt_entry = prompt_data[selected_category]["subcategories"][selected_subcategory]

# Display header and summary
st.markdown(f"<h3 style='margin-bottom: 0.2em;'>\ud83d\udcc2 {selected_category_label} → \ud83e\udde0 {selected_subcategory_label}</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 1.1rem; margin-top: 0.5em;'><strong>{t('Summary:', 'Opsummering:')}</strong> {prompt_entry['summary'][language]}</p>", unsafe_allow_html=True)

# Prompt content
st.code(prompt_entry["prompt"][language], language="markdown")

# Escape text for JavaScript
js_safe_prompt = prompt_entry["prompt"][language].replace("`", "\\`").replace('"', '\\"').replace("\n", "\\n")

# Optional example thread link
if "example_link" in prompt_entry:
    st.markdown(f"[\ud83d\udd17 {t('View ChatGPT Example Thread', 'Se eksempeltråd i ChatGPT')}]({prompt_entry['example_link']})", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color: #888;'>{t('No example thread available yet.', 'Ingen eksempeltråd tilgængelig endnu.')}</span>", unsafe_allow_html=True)

# Copy button
components.html(f"""
    <div style="margin-top: 10px;">
        <button id="copy-btn"
            style="padding: 0.5em 1em; background-color: #f4f4f4; border: 1px solid #ccc; border-radius: 6px; cursor: pointer;">
            📋 {t('Copy Prompt', 'Kopiér prompt')}
        </button>
        <script>
            const btn = document.getElementById("copy-btn");
            btn.addEventListener("click", function() {{
                navigator.clipboard.writeText("{js_safe_prompt}");
                btn.innerText = "✅ {t('Copied!', 'Kopieret!')}";
                setTimeout(() => btn.innerText = "📋 {t('Copy Prompt', 'Kopiér prompt')}", 2000);
            }});
        </script>
    </div>
""", height=60)

# Footer
st.markdown("---")
st.info(t("Click the button above or highlight the text manually to copy the prompt.",
        "Klik på knappen ovenfor, eller markér teksten manuelt for at kopiere prompten."))
