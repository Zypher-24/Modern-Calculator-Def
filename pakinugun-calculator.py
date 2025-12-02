#system modern calculator project

import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("280x350")
root.configure(background="black")

#logo-picture
logo = tk.PhotoImage(file="logo.png")
root.iconphoto(True,logo)


display = tk.StringVar(value="0")
tk.Label(root, textvariable=display, background="white",
         fg="black", font=("Arial", 20, "bold"), height=2).pack(fill="x", padx=10, pady=10)

#clickable buttons
def click(button):
    current = display.get()
    if button == "C": display.set("0")
    elif button == "=":
        try: display.set(str(eval(current)))
        except: display.set("error")
    else:
        display.set(current + button if current != "0" else button)

#buttons
button = [
    ["C", "", "", ""],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "4", "+"],
    ["0", ".", "=", "/"]
]

for i, row in enumerate(button):
    frame = tk.Frame(root, bg="black")
    frame.pack(fill="x", padx=10, pady=2)
    for j, button in enumerate(row):
        color = ("grey" if button in "+-*/="
            else "red" if button in "C" else "grey")
        button_widget = tk.Label(frame, text=button, font=("Arial", 14, "bold"), background=color, foreground="white",
        width=5, height=2, relief="flat")

        button_widget.bind("<Button-1>", lambda e, b=button: click(b))
        button_widget.pack(side="left", padx=2)

root.mainloop()