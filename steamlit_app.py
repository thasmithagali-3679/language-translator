import streamlit as st
from googletrans import Translator

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="wide"
)

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

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f77b4;
    margin-bottom: 10px;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}
.result-box {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌍 Language Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text into 100+ languages easily</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input")
    input_text = st.text_area(
        "Enter text to translate",
        height=250,
        placeholder="Type or paste your text here..."
    )
    source_language = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys()),
        index=0
    )

with col2:
    st.subheader("📤 Output")
    target_language = st.selectbox(
        "Target Language",
        list(LANGUAGES.keys()),
        index=1
    )
    output_area = st.empty()

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 2])

with btn_col1:
    translate_btn = st.button("🔄 Translate", use_container_width=True, type="primary")

with btn_col2:
    clear_btn = st.button("🧹 Clear", use_container_width=True)

if clear_btn:
    st.rerun()

if translate_btn:
    if not input_text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                result = translator.translate(
                    input_text,
                    src=LANGUAGES[source_language],
                    dest=LANGUAGES[target_language]
                )
                translated_text = result.text

                output_area.markdown(
                    f'''
                    <div class="result-box">
                        <h4>✅ Translated Text</h4>
                        <p style="font-size:18px;">{translated_text}</p>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

                st.markdown("---")
                st.subheader("📋 Translation Details")
                detail1, detail2, detail3 = st.columns(3)
                detail1.metric("Source", source_language)
                detail2.metric("Target", target_language)
                detail3.metric("Characters", len(input_text))

                st.code(translated_text, language="text")

            except Exception as e:
                output_area.error(f"❌ Translation failed: {e}")

st.markdown("---")
st.caption("Built with Streamlit + Python + Google Translate")
