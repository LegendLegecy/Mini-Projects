from googletrans import Translator

def translate_text(text, source__language, destination_language):
    translator = Translator()
    src_code = language_detector(source__language)
    dest_code = language_detector(destination_language)
    translation = translator.translate(text, src=src_code, dest=dest_code)
    return translation.text

def language_detector(language):

    match language.lower():
        case 'afrikaans':
            return 'af'
        case 'arabic':
            return 'ar'
        case 'bengali':
            return 'bn'
        case 'bulgarian':
            return 'bg'
        case 'catalan':
            return 'ca'
        case 'chinese (simplified)':
            return 'zh-cn'
        case 'chinese (traditional)':
            return 'zh-tw'
        case 'croatian':
            return 'hr'
        case 'czech':
            return 'cs'
        case 'danish':
            return 'da'
        case 'dutch':
            return 'nl'
        case 'english':
            return 'en'
        case 'estonian':
            return 'et'
        case 'finnish':
            return 'fi'
        case 'french':
            return 'fr'
        case 'german':
            return 'de'
        case 'greek':
            return 'el'
        case 'gujarati':
            return 'gu'
        case 'hebrew':
            return 'he'
        case 'hindi':
            return 'hi'
        case 'hungarian':
            return 'hu'
        case 'icelandic':
            return 'is'
        case 'indonesian':
            return 'id'
        case 'irish':
            return 'ga'
        case 'italian':
            return 'it'
        case 'japanese':
            return 'ja'
        case 'kannada':
            return 'kn'
        case 'korean':
            return 'ko'
        case 'latin':
            return 'la'
        case 'latvian':
            return 'lv'
        case 'lithuanian':
            return 'lt'
        case 'malay':
            return 'ms'
        case 'malayalam':
            return 'ml'
        case 'marathi':
            return 'mr'
        case 'nepali':
            return 'ne'
        case 'norwegian':
            return 'no'
        case 'persian':
            return 'fa'
        case 'polish':
            return 'pl'
        case 'portuguese':
            return 'pt'
        case 'punjabi':
            return 'pa'
        case 'romanian':
            return 'ro'
        case 'russian':
            return 'ru'
        case 'serbian':
            return 'sr'
        case 'slovak':
            return 'sk'
        case 'slovenian':
            return 'sl'
        case 'spanish':
            return 'es'
        case 'swahili':
            return 'sw'
        case 'swedish':
            return 'sv'
        case 'tamil':
            return 'ta'
        case 'telugu':
            return 'te'
        case 'thai':
            return 'th'
        case 'turkish':
            return 'tr'
        case 'ukrainian':
            return 'uk'
        case 'urdu':
            return 'ur'
        case 'vietnamese':
            return 'vi'
        case 'welsh':
            return 'cy'
        case _:
            raise ValueError(f"Unsupported language: {language}")

if __name__ == "__main__":
    cmd = input("\nGive me text: ")
    src_lang= input("\nWhat's the source language: ").title()
    dest_lang= input("\nWhat's the destination language: ").title()
    translated_txt=translate_text(cmd , src_lang,dest_lang)
    with open("Answer.txt", "w", encoding='utf-8') as f:
        f.write(translated_txt)
    print("\nYour answer is generated in file 'Answer.txt'.Please have a look.")