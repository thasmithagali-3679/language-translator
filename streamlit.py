import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

translator = Translator()

LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi",
    "Turkish": "tr",
    "Polish": "pl",
    "Swedish": "sv",
    "Greek": "el",
    "Hebrew": "he",
    "Vietnamese": "vi",
    "Thai": "th",
    "Indonesian": "id",
    "Filipino": "tl",
    "Urdu": "ur"
}

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #1f4fa3;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 1.5rem;
    }
    .footer {
        text-align: center;
        color: #888;
        margin-top: 2rem;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">🌍 Language Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text into multiple languages with a clean Streamlit interface.</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.subheader("Input")
    input_text = st.text_area("Enter text", height=220, placeholder="Type something here...")
    source_language = st.selectbox("Source language", list(LANGUAGES.keys()), index=0)

with right:
    st.subheader("Output")
    target_language = st.selectbox("Target language", list(LANGUAGES.keys()), index=1)
    output_box = st.empty()
    output_box.info("Translated text will appear here.")

col1, col2 = st.columns([1, 1])
translate_clicked = col1.button("🔄 Translate", use_container_width=True, type="primary")
clear_clicked = col2.button("🧹 Clear", use_container_width=True)

if clear_clicked:
    st.rerun()

if translate_clicked:
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                result = translator.translate(
                    input_text,
                    src=LANGUAGES[source_language],
                    dest=LANGUAGES[target_language],
                )
                translated_text = result.text
                output_box.success(translated_text)

                st.markdown("---")
                st.write("### Translation Details")
                st.write(f"**Source language:** {source_language}")
                st.write(f"**Target language:** {target_language}")
                st.write(f"**Characters:** {len(input_text)}")
                st.code(translated_text, language="text")
            except Exception as e:
                output_box.error(f"Translation failed: {e}")

st.markdown('<div class="footer">Built with Streamlit and Python • Ready for live deployment</div>', unsafe_allow_html=True)
