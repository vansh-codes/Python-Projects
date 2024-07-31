import tkinter as tk
from tkinter import messagebox
import random as R

# Global variables
score = 0

def start_game():
    global r, tries, count
    l = int(lower_limit_entry.get())
    u = int(upper_limit_entry.get())
    r = R.randint(l, u)
    tries = 3
    count = 0
    guess_button.config(state=tk.NORMAL)
    result_label.config(text="Guess the number!")

def guess_number():
    global count, tries, score
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return

    if guess == r:
        count += 1
        if count == 1:
            score += 15
        elif count == 2:
            score += 10
        else:
            score += 5
        messagebox.showinfo("Congratulations!", f"You guessed the number in {count} tries!\nYour score: {score}")
        guess_button.config(state=tk.DISABLED)
        result_label.config(text="Guess the number!")
    else:
        count += 1
        tries -= 1
        if tries > 0:
            if guess > r:
                result_label.config(text="Try again! Your guess was high.")
            else:
                result_label.config(text="Try again! Your guess was low.")
            tries_label.config(text=f"Tries left: {tries}")
        else:
            messagebox.showinfo("Game Over", f"You lost. The number was {r}.\nYour score: {score}")
            guess_button.config(state=tk.DISABLED)
            result_label.config(text="Game Over! Press 'Start New Game' to play again.")

def exit_game():
    global root
    messagebox.showinfo("Final Score", f"Your final score: {score}")
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Guess the Number Game")

# Create widgets
welcome_label = tk.Label(root, text="Guess the Number", font=("Helvetica", 16))
rules_label = tk.Label(root, text="You have 3 tries to guess the number.\n"
                                "You get 15 points if you guess in 1 try.\n"
                                "You get 10 points if you guess in 2 tries.\n"
                                "You get 5 points if you guess in 3 tries.\n")
rules_label.pack(pady=10)

lower_limit_label = tk.Label(root, text="Enter lower limit of the range:")
lower_limit_label.pack()
lower_limit_entry = tk.Entry(root)
lower_limit_entry.pack(pady=5)

upper_limit_label = tk.Label(root, text="Enter upper limit of the range:")
upper_limit_label.pack()
upper_limit_entry = tk.Entry(root)
upper_limit_entry.pack(pady=5)

start_button = tk.Button(root, text="Start New Game", command=start_game)
start_button.pack(pady=10)

guess_label = tk.Label(root, text="Guess the number:")
guess_label.pack()
guess_entry = tk.Entry(root)
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Submit Guess", command=guess_number, state=tk.DISABLED)
guess_button.pack(pady=10)

tries_label = tk.Label(root, text="Tries left: 3")
tries_label.pack(pady=5)

result_label = tk.Label(root, text="Press 'Start New Game' to begin.")
result_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
