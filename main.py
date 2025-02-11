import tkinter as tk
import random
import json
from turtle import width
from typing import final

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
            ("ひらがな", self.show_hiragana),
            ("カタカナ", self.show_katakana),
            ("漢字", self.show_kanji)
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
    
    '''
    #######################################################################################################HIRAGANA
    #######################################################################################################'''

    def show_hiragana(self):
        mode_frame = self.create_mode_frame("Hiragana")
        
        sections_frame = tk.Frame(mode_frame)
        sections_frame.pack(after=mode_frame.winfo_children()[0], fill=tk.X, padx=20)  # Pack after title

        for i in range(4):
            sections_frame.columnconfigure(i, weight=1)
            sections_frame.rowconfigure(i, weight=1)

        sections = [
            ("ごじゅうおん", self.hiragana_basic_quiz),
            ("だくてん", self.hiragana_dakuten_quiz),
            ("はんだくてん", self.hiragana_handakuten_quiz),
            ("ようおん", self.hiragana_combinations_quiz)
        ]

        for i, (text, command) in enumerate(sections):
            btn = tk.Button(sections_frame, text=text, command=command, width=10, height=2)
            btn.grid(row=0, column=i, pady=10, padx=5)
    
    def load_hiragana_dict(self):
        with open('dictionaries/hiragana.json', 'r', encoding='utf-8') as f:
            self.hiragana_dict = json.load(f)
    
    def get_random_hiragana_pair(self, section="basic"):
        self.load_hiragana_dict()
        if section not in self.hiragana_dict:
            raise ValueError(f"Invalid section: {section}")
            
        romaji = random.choice(list(self.hiragana_dict[section].values()))
        hiragana = [k for k, v in self.hiragana_dict[section].items() if v == romaji][0]
        return romaji, hiragana

    def clear_quiz_frame(self):
        # Clear all widgets from current frame except the title and navigation
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("text").startswith("Welcome"):
                    continue
                if isinstance(widget, tk.Frame) and len(widget.winfo_children()) > 0 and isinstance(widget.winfo_children()[0], tk.Button):
                    continue
                if isinstance(widget, tk.Label) and widget.cget("text") == "By: Rob ®":
                    continue
                if isinstance(widget, tk.Button) and widget.cget("text") == "Back to menu":
                    continue
                widget.destroy()

    def hiragana_basic_quiz(self):
        self.clear_quiz_frame()
        romaji, hiragana = self.get_random_hiragana_pair("basic")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + hiragana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.hiragana_basic_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    def hiragana_dakuten_quiz(self):
        self.clear_quiz_frame()
        romaji, hiragana = self.get_random_hiragana_pair("dakuten")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + hiragana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.hiragana_dakuten_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    def hiragana_handakuten_quiz(self):
        self.clear_quiz_frame()
        romaji, hiragana = self.get_random_hiragana_pair("handakuten")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + hiragana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.hiragana_handakuten_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    def hiragana_combinations_quiz(self):
        self.clear_quiz_frame()
        romaji, hiragana = self.get_random_hiragana_pair("combinations")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + hiragana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.hiragana_combinations_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    '''
    #######################################################################################################KATAKANA
    #######################################################################################################'''

    def show_katakana(self):
        mode_frame = self.create_mode_frame("Katakana")
        
        sections_frame = tk.Frame(mode_frame)
        sections_frame.pack(after=mode_frame.winfo_children()[0], fill=tk.X, padx=20)

        for i in range(4):
            sections_frame.columnconfigure(i, weight=1)
            sections_frame.rowconfigure(i, weight=1)

        sections = [
            ("ごじゅうおん", self.katakana_basic_quiz),
            ("だくてん", self.katakana_dakuten_quiz),
            ("はんだくてん", self.katakana_handakuten_quiz),
            ("ようおん", self.katakana_combinations_quiz)
        ]

        for i, (text, command) in enumerate(sections):
            btn = tk.Button(sections_frame, text=text, command=command, width=10, height=2)
            btn.grid(row=0, column=i, pady=10, padx=5)
    
    def load_katakana_dict(self):
        with open('dictionaries/katakana.json', 'r', encoding='utf-8') as f:
            self.katakana_dict = json.load(f)
    
    def get_random_katakana_pair(self, section="basic"):
        self.load_katakana_dict()
        if section not in self.katakana_dict:
            raise ValueError(f"Invalid section: {section}")
            
        romaji = random.choice(list(self.katakana_dict[section].values()))
        katakana = [k for k, v in self.katakana_dict[section].items() if v == romaji][0]
        return romaji, katakana

    def clear_quiz_frame(self):
        # Clear all widgets from current frame except the title and navigation
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("text").startswith("Welcome"):
                    continue
                if isinstance(widget, tk.Frame) and len(widget.winfo_children()) > 0 and isinstance(widget.winfo_children()[0], tk.Button):
                    continue
                if isinstance(widget, tk.Label) and widget.cget("text") == "By: Rob ®":
                    continue
                if isinstance(widget, tk.Button) and widget.cget("text") == "Back to menu":
                    continue
                widget.destroy()

    def katakana_basic_quiz(self):
        self.clear_quiz_frame()
        romaji, katakana = self.get_random_katakana_pair("basic")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + katakana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.katakana_basic_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    def katakana_dakuten_quiz(self):
        self.clear_quiz_frame()
        romaji, katakana = self.get_random_katakana_pair("dakuten")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + katakana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.katakana_dakuten_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    def katakana_handakuten_quiz(self):
        self.clear_quiz_frame()
        romaji, katakana = self.get_random_katakana_pair("handakuten")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + katakana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.katakana_handakuten_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    def katakana_combinations_quiz(self):
        self.clear_quiz_frame()
        romaji, katakana = self.get_random_katakana_pair("combinations")
        answer_romaji = romaji

        self.quiz_question = tk.Label(self.current_frame, text="(" + katakana + ")", font=("Arial", 70))
        self.quiz_question.pack(side=tk.TOP, pady=40)

        self.result_label = tk.Label(self.current_frame, text="", font=("Arial", 40))
        self.result_label.pack(side=tk.TOP, pady=40)

        answer_entry = tk.Entry(self.current_frame)
        answer_entry.pack(side=tk.TOP, pady=10)
        answer_entry.focus()

        def check_answer(event=None):
            answer_check = answer_entry.get()
            if answer_check == answer_romaji:
                self.result_label.config(text="Correct!")
                self.current_frame.after(500, delete_question)
                self.current_frame.after(500, self.hiragana_combinations_quiz)
            else:
                self.result_label.config(text=f"Incorrect! Try again.", font=("Arial", 30))
            
            answer_entry.delete(0, tk.END)

        def delete_question():
            self.quiz_question.destroy()
            self.result_label.destroy()
            answer_entry.destroy()
        
        answer_entry.bind('<Return>', check_answer)

    '''
    #######################################################################################################KANJI
    #######################################################################################################'''

    def show_kanji(self):
        self.create_mode_frame("Kanji")

if __name__ == "__main__":
    app = JapaneseApp()