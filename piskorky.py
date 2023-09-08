import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()

# Initialize variables
current_player = "X"
board = [" " for _ in range(9)]

# Create a function to check for a win
def check_win():
    for win_combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]:
        if board[win_combo[0]] == board[win_combo[1]] == board[win_combo[2]] != " ":
            return True
    return False

# Create a function for a button click
def button_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            root.quit()
        elif " " not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create buttons
buttons = [tk.Button(root, text=" ", font=("normal", 20), width=8, height=4,
                     command=lambda index=i: button_click(index)) for i in range(9)]

# Grid layout for buttons
for i in range(3):
    for j in range(3):
        buttons[i * 3 + j].grid(row=i, column=j)

# Run the main loop
root.mainloop()
