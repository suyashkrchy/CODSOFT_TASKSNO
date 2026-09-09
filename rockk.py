import random
import tkinter as tk

# Console Version

def play_console():
    user_score = 0
    computer_score = 0

    print(" Welcome to Rock-Paper-Scissors (Console Mode)!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' anytime to exit the game.\n")

    while True:
        user_choice = input(" Enter your choice (rock/paper/scissors): ").lower()

        if user_choice == "quit":
            print(" Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f" Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(" It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print(" You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            computer_score += 1

        print(f" Current Score → You: {user_score} | Computer: {computer_score}\n")

        play_again = input(" Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print(" Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

# Tkinter GUI Version
def play_gui():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    def play(choice):
        global user_score, computer_score
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result_text.set(f"You chose {choice} | Computer chose {computer_choice}")

        if choice == computer_choice:
            outcome = "It's a tie!"
        elif (choice == "rock" and computer_choice == "scissors") or \
             (choice == "scissors" and computer_choice == "paper") or \
             (choice == "paper" and computer_choice == "rock"):
            outcome = "You win this round!"
            user_score += 1
        else:
            outcome = "Computer wins this round!"
            computer_score += 1

        score_text.set(f"Score → You: {user_score} | Computer: {computer_score}")
        outcome_text.set(outcome)

    def reset_game():
        global user_score, computer_score
        user_score = 0
        computer_score = 0
        result_text.set("Make your choice!")
        outcome_text.set("")
        score_text.set("Score → You: 0 | Computer: 0")

    root = tk.Tk()
    root.title("Rock-Paper-Scissors Game 🎮")
    root.geometry("400x300")

    result_text = tk.StringVar()
    result_text.set("Make your choice!")
    outcome_text = tk.StringVar()
    score_text = tk.StringVar()
    score_text.set("Score → You: 0 | Computer: 0")

    tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack(pady=10)
    tk.Label(root, textvariable=outcome_text, font=("Arial", 12), fg="blue").pack(pady=5)
    tk.Label(root, textvariable=score_text, font=("Arial", 12), fg="green").pack(pady=10)

    frame = tk.Frame(root)
    frame.pack()

    tk.Button(frame, text=" Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
    tk.Button(frame, text=" Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
    tk.Button(frame, text=" Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

    tk.Button(root, text=" Reset Game", command=reset_game).pack(pady=20)

    root.mainloop()


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    print("Choose game mode:")
    print("1. Console Mode")
    print("2. GUI Mode (Tkinter)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        play_console()
    elif choice == "2":
        play_gui()
    else:
        print("Invalid choice. Exiting...")
