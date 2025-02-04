import tkinter as tk

class JapaneseApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Learn Japanese Basics")
        self.root.geometry("400x800")
        self.current_frame = None
        self.show_main_menu()
        self.root.mainloop()

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        menu_frame = tk.Frame(self.root)
        self.current_frame = menu_frame

        title = tk.Label(menu_frame, text="Welcome to Learn Japanese Basics")
        title.pack(side=tk.TOP)

        buttonframe = tk.Frame(menu_frame)
        for i in range(3):
            buttonframe.columnconfigure(i, weight=1)
            buttonframe.rowconfigure(i, weight=1)

        buttons = [
            ("Hiragana", self.show_hiragana),
            ("Katakana", self.show_katakana),
            ("Kanji", self.show_kanji)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(buttonframe, text=text, command=command, width=10, height=2)
            btn.grid(row=i, column=1, pady=10)

        buttonframe.pack(expand=True)
        
        author = tk.Label(menu_frame, text="By: Rob ®")
        author.pack(side=tk.BOTTOM)
        
        menu_frame.pack(fill=tk.BOTH, expand=True)

    def create_mode_frame(self, title_text):
        if self.current_frame:
            self.current_frame.destroy()
            
        mode_frame = tk.Frame(self.root)
        self.current_frame = mode_frame

        title = tk.Label(mode_frame, text=f"Welcome to {title_text}")
        title.pack(side=tk.TOP)

        author = tk.Label(mode_frame, text="By: Rob ®")
        author.pack(side=tk.BOTTOM)
        
        back_button = tk.Button(mode_frame, text="Back to menu", command=self.show_main_menu)
        back_button.pack(side=tk.BOTTOM)

        mode_frame.pack(fill=tk.BOTH, expand=True)
        return mode_frame

    def show_hiragana(self):
        self.create_mode_frame("Hiragana")

    def show_katakana(self):
        self.create_mode_frame("Katakana")

    def show_kanji(self):
        self.create_mode_frame("Kanji")

if __name__ == "__main__":
    app = JapaneseApp()