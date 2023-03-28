BACKGROUND_COLOR = "#B1DDC6"

import tkinter
import pandas
import random
random_word = {}
to_learn={}

try:
    data = pandas.read_csv("./data/words_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    canvas.itemconfig(card_backround, image=image_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text =random_word["English"], fill="white")
    canvas.itemconfig(card_backround, image=image_back)

def is_known():
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    next_card()


#window
window = tkinter.Tk()
window.title("Learning with Capstone")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Canvas front
canvas = tkinter.Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = tkinter.PhotoImage(file="./images/card_front.png")
image_back = tkinter.PhotoImage(file="./images/card_back.png")
card_backround = canvas.create_image(400, 263, image=image_front)
title_text = canvas.create_text(400,150, text="Titel", font=("Ariel",40, "italic"))
word_text = canvas.create_text(400, 263, text="Start", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Button
image_wrong =tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=image_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

#Button right
image_right = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=image_right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()