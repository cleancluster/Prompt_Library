import streamlit as st
import json
import html
import streamlit.components.v1 as components

# Load prompt data
with open("prompt_library.json", "r") as f:
    prompt_data = json.load(f)

# Set layout and title
st.set_page_config(layout="wide")

# Language toggle
language = st.sidebar.radio("Choose Language / Vælg Sprog", ["English", "Dansk"])

# Simple translation function
def t(en, da):
    return en if language == "English" else da

# App title
st.markdown(f"<h1 style='font-size: 2.4rem;'>📚 {t('Prompt Library', 'Promptbibliotek')}</h1>", unsafe_allow_html=True)

# --- CATEGORY SELECTION ---
categories = [cat for cat in prompt_data if "meta" in prompt_data[cat] and "subcategories" in prompt_data[cat]]
category_labels = [prompt_data[cat]["meta"][language] for cat in categories]
category_map = dict(zip(category_labels, categories))

selected_category_label = st.sidebar.selectbox(t("📂 Choose a category", "📂 Vælg en kategori"), category_labels)
selected_category = category_map[selected_category_label]

# --- SUBCATEGORY SELECTION ---
subcategories = list(prompt_data[selected_category]["subcategories"].keys())
subcategory_labels = [prompt_data[selected_category]["subcategories"][sub]["meta"][language] for sub in subcategories]
subcategory_map = dict(zip(subcategory_labels, subcategories))

selected_subcategory_label = st.sidebar.selectbox(t("🧠 Choose a subcategory", "🧠 Vælg en underkategori"), subcategory_labels)
selected_subcategory = subcategory_map[selected_subcategory_label]

# --- ENTRY SELECTION ---
entry = prompt_data[selected_category]["subcategories"][selected_subcategory]
summary = entry["summary"][language]
prompt = entry["prompt"][language]

# --- DISPLAY MAIN CONTENT ---
st.markdown(f"<h3 style='margin-bottom: 0.2em;'>📂 {selected_category_label} → 🧠 {selected_subcategory_label}</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 1.1rem; margin-top: 0.5em;'><strong>{t('Summary:', 'Opsummering:')}</strong> {summary}</p>", unsafe_allow_html=True)
st.code(prompt, language="markdown")

# --- COPY BUTTON ---
js_safe_prompt = prompt.replace("`", "\\`").replace('"', '\\"').replace("\n", "\\n")

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

# --- OPTIONAL EXAMPLE LINK ---
if "example_link" in entry:
    st.markdown(f"[🔗 {t('View ChatGPT Example Thread', 'Se eksempeltråd i ChatGPT')}]({entry['example_link']})", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color: #888;'>{t('No example thread available yet.', 'Ingen eksempeltråd tilgængelig endnu.')}</span>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.info(t("Click the button above or highlight the text manually to copy the prompt.",
          "Klik på knappen ovenfor, eller markér teksten manuelt for at kopiere prompten."))
