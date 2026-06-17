# ============================================================================
# PYTHON BASICS FOR LANGUAGE TRANSLATOR PROJECT
# ============================================================================

print("\n" + "="*70)
print("PYTHON BASICS TUTORIAL FOR LANGUAGE TRANSLATOR")
print("="*70)

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================
print("\n1. VARIABLES AND DATA TYPES")
print("-" * 70)

# String - text data
text_to_translate = "Hello, how are you?"
print(f"String: {text_to_translate}")
print(f"Type: {type(text_to_translate)}")

# Integer - whole numbers
number_of_languages = 100
print(f"\nInteger: {number_of_languages}")
print(f"Type: {type(number_of_languages)}")

# Float - decimal numbers
confidence_score = 0.95
print(f"\nFloat: {confidence_score}")
print(f"Type: {type(confidence_score)}")

# Boolean - True or False
is_translation_complete = True
print(f"\nBoolean: {is_translation_complete}")
print(f"Type: {type(is_translation_complete)}")

# ============================================================================
# 2. LISTS - ORDERED COLLECTIONS
# ============================================================================
print("\n\n2. LISTS - ORDERED COLLECTIONS")
print("-" * 70)

# Create a list of languages
languages_list = ["English", "Spanish", "French", "German", "Chinese"]
print(f"Languages List: {languages_list}")
print(f"Type: {type(languages_list)}")

# Access elements by index (starts from 0)
first_language = languages_list[0]
print(f"\nFirst language (index 0): {first_language}")

last_language = languages_list[-1]
print(f"Last language (index -1): {last_language}")

# List length
print(f"\nTotal languages: {len(languages_list)}")

# Add to list
languages_list.append("Japanese")
print(f"After adding Japanese: {languages_list}")

# Remove from list
languages_list.remove("German")
print(f"After removing German: {languages_list}")

# ============================================================================
# 3. DICTIONARIES - KEY-VALUE PAIRS
# ============================================================================
print("\n\n3. DICTIONARIES - KEY-VALUE PAIRS")
print("-" * 70)

# Language codes dictionary
language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn"
}

print(f"Language Codes Dictionary: {language_codes}")
print(f"Type: {type(language_codes)}")

# Access value by key
english_code = language_codes["English"]
print(f"\nEnglish code: {english_code}")

# Add new key-value pair
language_codes["Japanese"] = "ja"
print(f"\nAfter adding Japanese: {language_codes}")

# Check if key exists
if "Spanish" in language_codes:
    print("Spanish is in the dictionary!")

# Get all keys
print(f"\nAll language names: {list(language_codes.keys())}")

# Get all values
print(f"All language codes: {list(language_codes.values())}")

# ============================================================================
# 4. STRING OPERATIONS
# ============================================================================
print("\n\n4. STRING OPERATIONS")
print("-" * 70)

text = "Language Translator"

# String length
print(f"Text: {text}")
print(f"Length: {len(text)} characters")

# String concatenation
greeting = "Hello, " + "World!"
print(f"\nConcatenation: {greeting}")

# String formatting
lang = "Spanish"
code = "es"
formatted = f"Language: {lang}, Code: {code}"
print(f"\nF-String formatting: {formatted}")

# String methods
print(f"\nOriginal: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('Translator', 'Converter')}")
print(f"Split: {text.split()}")

# ============================================================================
# 5. CONDITIONAL STATEMENTS (IF/ELSE)
# ============================================================================
print("\n\n5. CONDITIONAL STATEMENTS (IF/ELSE)")
print("-" * 70)

user_language = "Spanish"
available_languages = ["English", "Spanish", "French"]

if user_language in available_languages:
    print(f"✓ {user_language} is available for translation")
else:
    print(f"✗ {user_language} is not available")

# Multiple conditions
confidence = 0.85

if confidence >= 0.95:
    quality = "Excellent"
elif confidence >= 0.80:
    quality = "Good"
elif confidence >= 0.60:
    quality = "Fair"
else:
    quality = "Poor"

print(f"\nConfidence Score: {confidence}")
print(f"Quality Rating: {quality}")

# ============================================================================
# 6. LOOPS - ITERATION
# ============================================================================
print("\n\n6. LOOPS - ITERATION")
print("-" * 70)

# For loop - iterate through a list
print("\nLanguages available:")
for lang in ["English", "Spanish", "French"]:
    print(f"  - {lang}")

# For loop with range
print("\nTranslation progress:")
for i in range(1, 6):
    print(f"  Step {i}: Processing...")

# For loop with dictionary
print("\nLanguage codes:")
for language, code in language_codes.items():
    print(f"  {language}: {code}")

# ============================================================================
# 7. FUNCTIONS
# ============================================================================
print("\n\n7. FUNCTIONS")
print("-" * 70)

def translate_simple(text, source_lang, target_lang):
    """
    A simple translation function (mock)
    
    Args:
        text (str): Text to translate
        source_lang (str): Source language code
        target_lang (str): Target language code
    
    Returns:
        str: Translated text
    """
    return f"[Translated from {source_lang} to {target_lang}]: {text}"

# Call the function
result = translate_simple("Hello", "en", "es")
print(f"Function result: {result}")

# Function with default parameters
def greet(name, language="English"):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour"
    }
    return f"{greetings.get(language, 'Hello')}, {name}!"

print(f"\n{greet('Alice')}")
print(f"{greet('María', 'Spanish')}")
print(f"{greet('Jean', 'French')}")

# ============================================================================
# 8. EXCEPTIONS - ERROR HANDLING
# ============================================================================
print("\n\n8. EXCEPTIONS - ERROR HANDLING")
print("-" * 70)

def safe_translate(text, lang_code):
    """Safely translate with error handling"""
    try:
        if not text:
            raise ValueError("Text cannot be empty")
        if len(text) > 500:
            raise ValueError("Text is too long (max 500 characters)")
        return f"Translated: {text}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

print(f"Valid input: {safe_translate('Hello world', 'es')}")
print(f"Empty input: {safe_translate('', 'es')}")
print(f"Long input: {safe_translate('a' * 600, 'es')}")

# ============================================================================
# 9. WORKING WITH APIs (Conceptual)
# ============================================================================
print("\n\n9. WORKING WITH APIs (CONCEPTUAL)")
print("-" * 70)

# Simulated API response
api_response = {
    "status": "success",
    "original_text": "Hello",
    "translated_text": "Hola",
    "source_language": "en",
    "target_language": "es",
    "confidence": 0.98
}

print(f"API Response: {api_response}")
print(f"\nResponse Details:")
for key, value in api_response.items():
    print(f"  {key}: {value}")

# ============================================================================
# 10. LIST COMPREHENSION
# ============================================================================
print("\n\n10. LIST COMPREHENSION")
print("-" * 70)

# Create a list of language codes
languages = {"English": "en", "Spanish": "es", "French": "fr"}
codes = [code for code in languages.values()]
print(f"Language codes: {codes}")

# Create a list of language names in uppercase
upper_names = [name.upper() for name in languages.keys()]
print(f"Language names (uppercase): {upper_names}")

# Filter list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n\n" + "="*70)
print("SUMMARY OF PYTHON BASICS")
print("="*70)
print("""
✓ Variables: Store data
✓ Lists: Ordered collections
✓ Dictionaries: Key-value pairs
✓ Strings: Text manipulation
✓ Conditionals: Make decisions
✓ Loops: Repeat operations
✓ Functions: Reusable code blocks
✓ Error Handling: Handle exceptions gracefully
✓ APIs: Communicate with external services
✓ List Comprehension: Elegant list creation
""")
print("="*70)
print("\nNow you're ready to build your Language Translator!")
print("="*70 + "\n")