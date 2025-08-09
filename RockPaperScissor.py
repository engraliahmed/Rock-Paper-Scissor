import tkinter as tk
import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

emojis = {ROCK: '🪨', SCISSOR: '✂️', PAPER: '📜'}
choices = tuple(emojis.keys())

# Game functions
def play(user_choice):
    computer_choice = random.choice(choices)
    display_choices(user_choice, computer_choice)
    determine_winner(user_choice, computer_choice)

def display_choices(user_choice, computer_choice):
    user_label.config(text=f"You chose {emojis[user_choice]}")
    computer_label.config(text=f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        result_label.config(text="It's a Tie! 🤝", fg="blue")
    elif ((user_choice == ROCK and computer_choice == SCISSOR) or
          (user_choice == PAPER and computer_choice == ROCK) or
          (user_choice == SCISSOR and computer_choice == PAPER)):
        result_label.config(text="You Win! 🎉", fg="green")
    else:
        result_label.config(text="You Lose! 😢", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Times New Roman", 24, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Display Labels
user_label = tk.Label(root, text="", font=("Times New Roman", 16), bg="#f0f0f0")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="", font=("Times New Roman", 16), bg="#f0f0f0")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Times New Roman", 18, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Times New Roman", 14), width=10, command=lambda: play(ROCK))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="📜 Paper", font=("Times New Roman", 14), width=10, command=lambda: play(PAPER))
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(button_frame, text="✂️ Scissor", font=("Times New Roman", 14), width=10, command=lambda: play(SCISSOR))
scissor_btn.grid(row=0, column=2, padx=5)

# Exit Button
exit_btn = tk.Button(root, text="Exit Game", font=("Times New Roman", 12), bg="red", fg="white", command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
