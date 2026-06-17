import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Set page config
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Add custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        text-align: center;
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("🌍 Language Translator")
st.markdown("**Translate text into 100+ languages with ease!**")
st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input")
    
with col2:
    st.subheader("📤 Output")

st.markdown("---")

# Language dictionary with codes
languages = {
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

# Create three columns for layout
col1, col2, col3 = st.columns([2, 1, 2])

# Input section
with col1:
    st.subheader("📝 Input Text")
    input_text = st.text_area(
        "Enter text to translate:",
        placeholder="Type something here...",
        height=200,
        label_visibility="collapsed"
    )
    
    source_language = st.selectbox(
        "Source Language:",
        list(languages.keys()),
        index=0,
        label_visibility="collapsed"
    )

# Middle section - Arrow
with col2:
    st.markdown("<br>" * 3, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>⬇️</h1>", unsafe_allow_html=True)

# Output section
with col3:
    st.subheader("📤 Translated Text")
    
    target_language = st.selectbox(
        "Target Language:",
        list(languages.keys()),
        index=1,
        label_visibility="collapsed"
    )

st.markdown("---")

# Translate button
if st.button("🔄 Translate", use_container_width=True, type="primary"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text to translate!")
    else:
        with st.spinner("🔄 Translating..."):
            try:
                # Get language codes
                source_code = languages[source_language]
                target_code = languages[target_language]
                
                # Translate the text
                result = translator.translate(
                    input_text,
                    src_language=source_code,
                    dest_language=target_code
                )
                
                translated_text = result['text']
                
                # Display result
                col1, col2, col3 = st.columns([2, 1, 2])
                
                with col1:
                    st.info(f"**{source_language}:**\n\n{input_text}")
                
                with col3:
                    st.success(f"**{target_language}:**\n\n{translated_text}")
                
                # Copy button
                st.markdown("---")
                st.markdown(f"**Translated Text:** `{translated_text}`")
                
                # Additional info
                st.markdown("""
                    **Translation Details:**
                    - Source: {}
                    - Target: {}
                    - Characters: {}
                """.format(source_language, target_language, len(input_text)))
                    
            except Exception as e:
                st.error(f"❌ Error during translation: {str(e)}")
                st.info("Please try again or check your internet connection.")

st.markdown("---")

# Footer
st.markdown("""
    <div style='text-align: center; color: gray; margin-top: 2rem;'>
        <p><strong>Language Translator v1.0</strong></p>
        <p>Powered by Google Translate API • Built with Streamlit & Python</p>
    </div>
""", unsafe_allow_html=True)