import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        # Language choices for translation
        self.languages = ['English', 'Spanish', 'Hindi', 'Bengali', 'French', 'German', 'Italian', 'Japanese', 'Korean', 'Chinese']

        # Source and destination language variables
        self.source_lang = tk.StringVar()
        self.destination_lang = tk.StringVar()

        # Set default source and destination languages
        self.source_lang.set(self.languages[0])
        self.destination_lang.set(self.languages[1])

        # Creating GUI elements
        self.create_gui()

    def create_gui(self):
        # Source language selection
        source_label = ttk.Label(self.root, text="Source Language:")
        source_label.grid(row=0, column=0, padx=10, pady=10)
        source_combobox = ttk.Combobox(self.root, values=self.languages, textvariable=self.source_lang)
        source_combobox.grid(row=0, column=1, padx=10, pady=10)

        # Destination language selection
        dest_label = ttk.Label(self.root, text="Destination Language:")
        dest_label.grid(row=1, column=0, padx=10, pady=10)
        dest_combobox = ttk.Combobox(self.root, values=self.languages, textvariable=self.destination_lang)
        dest_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Text entry and translation result display
        text_label = ttk.Label(self.root, text="Enter Text:")
        text_label.grid(row=2, column=0, padx=10, pady=10)
        self.text_entry = ttk.Entry(self.root, width=40)
        self.text_entry.grid(row=2, column=1, padx=10, pady=10)

        self.translation_label = ttk.Label(self.root, text="Translation:")
        self.translation_label.grid(row=3, column=0, padx=10, pady=10)
        self.translation_result = ttk.Label(self.root, text="")
        self.translation_result.grid(row=3, column=1, padx=10, pady=10)

        # Translate button
        translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        # Get the selected languages and text to be translated
        source_language = self.source_lang.get()
        destination_language = self.destination_lang.get()
        text_to_translate = self.text_entry.get()

        if not text_to_translate:
            self.translation_result.config(text="Please enter some text to translate.")
            return

        # Perform translation
        translator = Translator()
        try:
            translated_text = translator.translate(text_to_translate, src=source_language.lower(), dest=destination_language.lower())
            self.translation_result.config(text=translated_text.text)
        except Exception as e:
            self.translation_result.config(text="Translation failed. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
