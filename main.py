from tkinter import *
import pandas
import random
import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDERS_NUMBER = os.getenv("SENDERS_NUMBER")
RECEIVERS_NUMBER = os.getenv("RECEIVERS_NUMBER")


BACKGROUND_COLOR = "#B1DDC6"
current_card_num = 0

# holds the serial number of the terms to be learnt
to_learn = []

# holds the terms learnt in this session
learnt_terms = []

file1 = open("data/terms_to_learn.txt", "r")
contents_to_learn = file1.readlines()
file1.close()

for line in contents_to_learn:
    line = line.strip()
    to_learn.append(int(line))


terms_file = open("data/all_terms.txt", "r")
desc_file = open("data/all_desc.txt", "r")
terms = terms_file.readlines()
descs = desc_file.readlines()
terms_file.close()
desc_file.close()

all_terms = []
for term in terms:
    all_terms.append(term.strip())
all_descs = []
for desc in descs:
    all_descs.append(desc.strip())


def next_card():
    global to_learn, all_descs, all_terms, current_card_num, flip_timer
    window.after_cancel(flip_timer)
    current_card_num = random.choice(to_learn)
    current_term = all_terms[current_card_num]

    canvas.itemconfig(card_title, text="Term", fill="black")
    canvas.itemconfig(
        card_word, text=current_term, fill="black", font=("Ariel", 40, "bold")
    )
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global to_learn, all_descs, all_terms, current_card_num

    current_desc = all_descs[current_card_num]
    canvas.itemconfig(card_title, text="", fill="white")
    canvas.itemconfig(
        card_word,
        text=current_desc,
        fill="white",
        font=(
            "Ariel",
            15,
            "bold",
        ),
    )
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    global to_learn, current_card_num, learnt_terms, all_terms
    learnt_terms.append(all_terms[current_card_num])
    to_learn.remove(current_card_num)
    print("Number of terms yet to learn: ", len(to_learn))
    with open("data/terms_to_learn.txt", "w") as fp:
        for num in to_learn:
            fp.write(str(num) + "\n")
    next_card()


window = Tk()
window.title("FoodBrain")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, width=380, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()


num_terms_to_learn = len(to_learn)
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
learnt_words = ""
for term in learnt_terms:
    learnt_words += term + ","

message = client.messages.create(
    body=f"You learnt {learnt_words[:-1]} today. There are only {num_terms_to_learn} terms left. Keep up the learning!😄",
    from_=SENDERS_NUMBER,
    to=RECEIVERS_NUMBER,
)
print("Message status: " + message.status)
