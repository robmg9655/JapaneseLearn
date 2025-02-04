import tkinter as tk

class JapaneseApp:
    def __init__(self):
        self.menu = tk.Tk()
        self.menu.title("Learn Japanese Basics")
        self.menu.geometry("400x800")

        self.title = tk.Label(self.menu, text="Welcome to Learn Japanese Basics")
        self.title.pack(side= tk.TOP)

        self.buttonframe = tk.Frame(self.menu)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.rowconfigure(0, weight=1)
        self.buttonframe.rowconfigure(1, weight=1)
        self.buttonframe.rowconfigure(2, weight=1)

        self.button_1 = tk.Button(self.buttonframe, text="Hiragana", command=self.hiragana, width=10, height=2)
        self.button_1.grid(row=0, column=1, pady=10)

        self.button_2 = tk.Button(self.buttonframe, text="Katakana", command=self.katakana, width=10, height=2)
        self.button_2.grid(row=1, column=1, pady=10)

        self.button_3 = tk.Button(self.buttonframe, text="Kanji", command=self.kanji, width=10, height=2)
        self.button_3.grid(row=2, column=1, pady=10)

        self.buttonframe.pack(expand=True)

        self.author = tk.Label(self.menu, text="By: Rob ®")
        self.author.pack(side= tk.BOTTOM)

    def hiragana(self):
        self.menu.destroy()
        self.hiragana = tk.Tk()
        self.hiragana.title("Hiragana")
        self.hiragana.geometry("400x800")

        self.title = tk.Label(self.hiragana, text="Welcome to Hiragana")
        self.title.pack(side= tk.TOP)

        self.author = tk.Label(self.hiragana, text="By: Rob ®")
        self.author.pack(side= tk.BOTTOM)

        self.back_button = tk.Button(self.hiragana, text="Back to menu", command=self.back_to_meu)
        self.back_button.pack(side= tk.BOTTOM)

    def katakana(self):
        self.menu.destroy()
        self.katakana = tk.Tk()
        self.katakana.title("Katakana")
        self.katakana.geometry("400x800")

        self.title = tk.Label(self.katakana, text="Welcome to Katakana")
        self.title.pack(side= tk.TOP)

        self.author = tk.Label(self.katakana, text="By: Rob ®")
        self.author.pack(side= tk.BOTTOM)

        self.back_button = tk.Button(self.katakana, text="Back to menu", command=self.back_to_meu)
        self.back_button.pack(side= tk.BOTTOM)

    def kanji(self):
        self.menu.destroy()
        self.kanji = tk.Tk()
        self.kanji.title("Kanji")
        self.kanji.geometry("400x800")

        self.title = tk.Label(self.kanji, text="Welcome to Kanji")
        self.title.pack(side= tk.TOP)

        self.author = tk.Label(self.kanji, text="By: Rob ®")
        self.author.pack(side= tk.BOTTOM)

        self.back_button = tk.Button(self.kanji, text="Back to menu", command=self.back_to_meu)
        self.back_button.pack(side= tk.BOTTOM)

    def back_to_meu(self):
        if hasattr(self, "hiragana"):
            self.hiragana.destroy()
            self.__init__()
        elif hasattr(self, "katakana"):
            self.katakana.destroy()
            self.__init__()
        elif hasattr(self, "kanji"):
            self.kanji.destroy()
            self.__init__()
        else:
            self.__init__()

if __name__ == "__main__":
    app = JapaneseApp()
    app.menu.mainloop()