import tkinter as tk

def click(event):
    """Handles button click."""
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display calculations
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20 bold", borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place buttons
row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 20", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:  # Move to the next row after 4 columns
        col = 0
        row += 1

# Run the main loop
root.mainloop()
