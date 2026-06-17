#!/usr/bin/env python3
"""
Simple Language Translator - Command Line Version
No setup required! Just run: python simple_translator.py
"""

from googletrans import Translator
import sys

def main():
    """
    Simple command-line translator
    """
    
    # Initialize translator
    translator = Translator()
    
    # Language codes reference
    languages = {
        '1': ('Spanish', 'es'),
        '2': ('French', 'fr'),
        '3': ('German', 'de'),
        '4': ('Italian', 'it'),
        '5': ('Portuguese', 'pt'),
        '6': ('Chinese (Simplified)', 'zh-cn'),
        '7': ('Japanese', 'ja'),
        '8': ('Korean', 'ko'),
        '9': ('Russian', 'ru'),
        '10': ('Arabic', 'ar'),
    }
    
    print("\n" + "="*60)
    print("🌍 SIMPLE LANGUAGE TRANSLATOR")
    print("="*60)
    
    # Get text to translate
    print("\nEnter text to translate (or 'quit' to exit):")
    text = input("Text: ").strip()
    
    if text.lower() == 'quit':
        print("\nGoodbye! 👋\n")
        return
    
    if not text:
        print("\n❌ Error: Please enter some text!\n")
        return
    
    # Display language options
    print("\n" + "-"*60)
    print("Select target language:")
    print("-"*60)
    for key, (name, code) in languages.items():
        print(f"{key}. {name} ({code})")
    
    # Get language choice
    choice = input("\nEnter number (1-10): ").strip()
    
    if choice not in languages:
        print("\n❌ Error: Invalid choice!\n")
        return
    
    lang_name, lang_code = languages[choice]
    
    # Translate
    print(f"\n🔄 Translating to {lang_name}...")
    
    try:
        result = translator.translate(text, src_language='en', dest_language=lang_code)
        translated = result['text']
        
        # Display result
        print("\n" + "="*60)
        print(f"📝 Original (English):\n{text}")
        print("-"*60)
        print(f"📤 Translated ({lang_name}):\n{translated}")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Make sure you have internet connection!\n")

if __name__ == "__main__":
    main()