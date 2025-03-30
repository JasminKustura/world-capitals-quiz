
import tkinter as tk

import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import random
import json
import requests
import io
import os

class WorldCapitalsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("World Capitals")
        self.root.attributes('-fullscreen', True)

        self.background_img = Image.open(resource_path("mapa.webp")).resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.background_photo = ImageTk.PhotoImage(self.background_img)

        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("backgroundsound.mp3"))
        pygame.mixer.music.play(-1)
        self.sound_on = True

        self.score = 0
        self.time_left = 10
        self.timer_id = None
        self.current_question = {}
        self.continent = ""
        self.questions = []

        self.load_data()
        self.setup_overlay_elements()
        self.create_main_menu()

    def setup_overlay_elements(self):
        self.logo_img = Image.open(resource_path("Virus DS logo_.png")).resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(self.logo_img)
        self.logo_label = tk.Label(self.root, image=self.logo_photo, bd=0, bg="white")
        self.logo_label.place(relx=0.98, rely=0.88, anchor="se")
        self.animate_logo()

        self.signature = tk.Label(self.root, text="Made by VirusDesignStudio-Jasmin Kustura", font=("Arial", 10, "italic"), fg="#8B0000", bg="white")
        self.signature.place(x=-300, rely=0.97, anchor="sw")
        self.signature_direction = 1
        self.move_signature()
        
        

    def animate_logo(self):
        def pulse(scale=1.0, grow=True):
            size = int(100 * scale)
            img = self.logo_img.resize((size, size))
            self.logo_photo = ImageTk.PhotoImage(img)
            self.logo_label.config(image=self.logo_photo)
            next_scale = scale + 0.01 if grow else scale - 0.01
            if next_scale >= 1.1:
                grow = False
            elif next_scale <= 0.9:
                grow = True
            self.root.after(50, lambda: pulse(next_scale, grow))
        pulse()

    def move_signature(self):
        x = self.signature.winfo_x()
        if self.signature_direction == 1:
            if x < self.root.winfo_screenwidth():
                self.signature.place(x=x+2)
            else:
                self.signature_direction = -1
        else:
            if x > -300:
                self.signature.place(x=x-2)
            else:
                self.signature_direction = 1
        self.root.after(30, self.move_signature)

    def load_data(self):
        try:
            with open(resource_path("countries_all_sample.json"), "r", encoding="utf-8") as f:
                self.all_data = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
            self.root.destroy()

    def create_main_menu(self):
        self.clear_screen(keep_overlay=True)

        title = tk.Label(self.canvas, text="🌍 World Capitals 🌍", font=("Arial", 36, "bold"), fg="#8B0000")
        title.place(relx=0.5, rely=0.2, anchor="center")

        start_btn = tk.Button(self.canvas, text="Start Quiz", font=("Arial", 20), command=self.choose_continent, width=20, bg="#3498db", fg="#8B0000")
        start_btn.place(relx=0.5, rely=0.35, anchor="center")

        mute_btn = tk.Button(self.canvas, text="Mute Music", font=("Arial", 14), command=self.toggle_sound, bg="#e67e22", fg="#8B0000")
        mute_btn.place(relx=0.5, rely=0.45, anchor="center")

        exit_btn = tk.Button(self.canvas, text="Exit", font=("Arial", 14), command=self.root.quit, bg="#c0392b", fg="#8B0000")
        exit_btn.place(relx=0.5, rely=0.55, anchor="center")

    def choose_continent(self):
        self.clear_screen(keep_overlay=True)

        label = tk.Label(self.canvas, text="Choose a Continent", font=("Arial", 28, "bold"), fg="#8B0000")
        label.place(relx=0.5, rely=0.15, anchor="center")

        continents = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
        for i, cont in enumerate(continents):
            btn = tk.Button(self.canvas, text=cont, font=("Arial", 18), width=20,
                            command=lambda c=cont: self.start_quiz(c), bg="#1abc9c", fg="#8B0000")
            btn.place(relx=0.5, rely=0.3 + i*0.08, anchor="center")

    def toggle_sound(self):
        pygame.mixer.music.set_volume(0 if self.sound_on else 1)
        self.sound_on = not self.sound_on

    def start_quiz(self, continent):
        self.continent = continent
        self.questions = [q for q in self.all_data if q["continent"] == continent]
        if len(self.questions) < 4:
            messagebox.showwarning("Not enough questions", f"Not enough data for {continent}")
            self.create_main_menu()
            return
        self.score = 0
        self.next_question()

    def next_question(self):
        self.clear_screen(keep_overlay=True)
        self.time_left = 10

        self.current_question = random.choice(self.questions)
        question_text = f"What is the capital of {self.current_question['country']}?"

        tk.Label(self.canvas, text=question_text, font=("Arial", 24), fg="#8B0000").place(relx=0.5, rely=0.2, anchor="center")
        self.load_flag(self.current_question["flag"])

        answers = [self.current_question["capital"]]
        while len(answers) < 4:
            random_cap = random.choice(self.questions)["capital"]
            if random_cap not in answers:
                answers.append(random_cap)
        random.shuffle(answers)

        for i, ans in enumerate(answers):
            tk.Button(self.canvas, text=ans, font=("Arial", 16), width=25,
                      command=lambda a=ans: self.check_answer(a)).place(relx=0.5, rely=0.4 + i*0.08, anchor="center")

        tk.Label(self.canvas, text=f"Score: {self.score}", font=("Arial", 14), fg="#8B0000").place(relx=0.5, rely=0.75, anchor="center")
        self.timer_label = tk.Label(self.canvas, text=f"Time: {self.time_left}", font=("Arial", 14), fg="#8B0000")
        self.timer_label.place(relx=0.5, rely=0.8, anchor="center")

        tk.Button(self.canvas, text="End Quiz", font=("Arial", 12), command=self.create_main_menu, bg="#e74c3c", fg="#8B0000").place(relx=0.5, rely=0.9, anchor="center")

        self.update_timer()

    def load_flag(self, url):
        try:
            response = requests.get(url)
            img_data = response.content
            img = Image.open(io.BytesIO(img_data)).resize((150, 100))
            self.flag_img = ImageTk.PhotoImage(img)
            flag_label = tk.Label(self.canvas, image=self.flag_img, )
            flag_label.place(relx=0.5, rely=0.3, anchor="center")
        except:
            pass

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.check_answer("")

    def check_answer(self, answer):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        correct = self.current_question["capital"]
        if answer == correct:
            self.score += 1
            self.play_sound(resource_path("correct.wav"))
            messagebox.showinfo("Correct", "That's correct! 🎉")
        else:
            self.play_sound(resource_path("wrong.wav"))
            messagebox.showerror("Wrong", f"Wrong answer! The capital of {self.current_question['country']} is {correct}.")

        self.next_question()

    def play_sound(self, file_name):
        try:
            sound = pygame.mixer.Sound(file_name)
            sound.play()
        except:
            pass

    def clear_screen(self, keep_overlay=False):
        for widget in self.canvas.winfo_children():
            if keep_overlay and widget in (self.logo_label, self.signature):
                continue
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WorldCapitalsQuiz(root)
    root.mainloop()
