# 🌍 Language Translator with Streamlit

A complete, beginner-friendly language translator application built with Python, Streamlit, and Google Translate API.

## ✅ Features

- ✅ **100+ Language Support** - Translate to/from multiple languages
- ✅ **Easy-to-Use Interface** - Beautiful Streamlit web app
- ✅ **No API Key Required** - Uses free Google Translate API
- ✅ **Real-time Translation** - Instant results
- ✅ **Python Basics Included** - Learn Python fundamentals
- ✅ **Mobile Responsive** - Works on all devices

## 🚀 Quick Start

### Step 1: Install Python (If Not Already Installed)

- Download from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation
- Verify installation:
  ```bash
  python --version
  ```

### Step 2: Clone or Download This Repository

```bash
git clone https://github.com/thasmithagali-3679/language-translator.git
cd language-translator
```

### Step 3: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Required Libraries

**No API key setup needed!** Just run:

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit` - Web app framework
- `googletrans` - Google Translate API wrapper
- `requests` - HTTP library

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📚 Learn Python Basics

Before running the app, learn Python fundamentals:

```bash
python python_basics.py
```

This covers:
1. Variables and Data Types
2. Lists
3. Dictionaries
4. String Operations
5. Conditionals (if/else)
6. Loops
7. Functions
8. Error Handling
9. Working with APIs
10. List Comprehension

## 📁 Project Structure

```
language-translator/
├── app.py                 # Main Streamlit application
├── simple_translator.py   # Command-line version
├── python_basics.py       # Python fundamentals tutorial
├── requirements.txt       # Package dependencies
├── README.md             # This file
└── .gitignore            # Git configuration
```

## 🎯 How to Use the App

1. **Enter Text** - Type or paste text in the input area
2. **Select Languages** - Choose source and target languages
3. **Click Translate** - Press the translate button
4. **View Results** - See the translated text
5. **Copy & Share** - Copy the result and share

## 🌐 Supported Languages

### Common Languages
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Chinese Simplified (zh-cn)
- Chinese Traditional (zh-tw)
- Japanese (ja)
- Korean (ko)
- Russian (ru)
- Arabic (ar)
- Hindi (hi)
- And 85+ more!

## 💻 Code Examples

### Basic Translation

```python
from googletrans import Translator

translator = Translator()

# Translate English to Spanish
result = translator.translate('Hello', dest_language='es')
print(result['text'])  # Output: Hola
```

### Using with Streamlit

```python
import streamlit as st
from googletrans import Translator

translator = Translator()

text = st.text_input('Enter text:')
lang = st.selectbox('Target Language:', ['Spanish', 'French', 'German'])

if st.button('Translate'):
    result = translator.translate(text, dest_language='es')
    st.success(result['text'])
```

## 🔧 Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Make sure you're in the virtual environment and installed requirements:
```bash
pip install -r requirements.txt
```

### Issue: Translation Not Working
**Solution:** Check your internet connection. The app requires internet for Google Translate API.

### Issue: Streamlit Not Found
**Solution:** Reinstall Streamlit:
```bash
pip install --upgrade streamlit
```

## 📦 Dependencies

| Library | Version | Purpose |
|---------|---------|----------|
| streamlit | 1.28.1 | Web app framework |
| googletrans | 4.0.0rc1 | Translation API |
| requests | 2.31.0 | HTTP requests |

## 🌟 Next Steps

1. **Customize the UI** - Modify colors, fonts, layout
2. **Add Features** - Text-to-speech, history, favorites
3. **Deploy** - Host on Streamlit Cloud, Heroku, or AWS
4. **Learn More** - Explore advanced Python concepts

## 📖 Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Translate API Documentation](https://github.com/ssut/py-googletrans)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## ❓ FAQ

**Q: Do I need a Google API key?**
A: No! This uses the free unofficial Google Translate API.

**Q: Can I translate images?**
A: Current version only supports text. You can add image OCR in the future.

**Q: Is there a limit on text length?**
A: Google Translate works best with text under 500 characters.

**Q: Can I deploy this online?**
A: Yes! Use Streamlit Cloud, Heroku, or other hosting platforms.

## 📞 Support

If you face any issues:
1. Check the Troubleshooting section
2. Review the code comments
3. Check Python and library versions
4. Ensure internet connection is stable

---

**Made with ❤️ by Your Developer**

Happy Translating! 🚀