import tkinter as tk
from tkinter import messagebox
import random

# Global variables
u_sc = 0
cpu = 0

def update_score(result):
    global u_sc, cpu
    
    if result == "win":
        u_sc += 1
        messagebox.showinfo("Result", f"CPU chose {r}\nYou Win!")
    elif result == "loose":
        cpu += 1
        messagebox.showinfo("Result", f"CPU chose {r}\nYou Lose!")
    elif result == "tie":
        messagebox.showinfo("Result", f"CPU chose {r}\nIt's a Tie!")

def play(choice):
    global r
    ch = ["Stone", "Paper", "Scissor"]
    r = random.choice(ch)

    if choice == "Stone":
        if r == "Stone":
            update_score("tie")
        elif r == "Paper":
            update_score("loose")
        elif r == "Scissor":
            update_score("win")
    elif choice == "Paper":
        if r == "Stone":
            update_score("win")
        elif r == "Paper":
            update_score("tie")
        elif r == "Scissor":
            update_score("loose")
    elif choice == "Scissor":
        if r == "Stone":
            update_score("loose")
        elif r == "Paper":
            update_score("win")
        elif r == "Scissor":
            update_score("tie")

def exit_game():
    global root
    result = f"Your Score: {u_sc}\nCPU's Score: {cpu}"
    if u_sc == cpu:
        result += "\nIt's a Tie!"
    elif u_sc > cpu:
        result += "\nCongratulations! You Win!"
    else:
        result += "\nTry Again! You Lose!"
    messagebox.showinfo("Game Over", result)
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Stone Paper Scissor Game")

# Create widgets
title_label = tk.Label(root, text="Stone, Paper, Scissor Game by Vansh", font=("Helvetica", 16))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

stone_button = tk.Button(button_frame, text="Stone", command=lambda: play("Stone"))
stone_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissor_button = tk.Button(button_frame, text="Scissor", command=lambda: play("Scissor"))
scissor_button.grid(row=0, column=2, padx=10)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
