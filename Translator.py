from Speak import Say
from Listen import Listen
from googletrans import Translator


def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def translation():
    try:
        Say("What would you like to translate?")
        text_to_translate = Listen()
        Say("To which language?")
        target_language = Listen()
        print("Target language:", target_language)
        translated_text = translate_text(text_to_translate, target_language)
        print("Translated text:", translated_text)
        Say(translated_text)

    except :
        Say("Sorry, I couldn't understand what you said.")








