import tkinter as tk

root = tk.Tk()
root.title("Cute Dog Drawing")

canvas = tk.Canvas(root, width=500, height=520, bg="white")
canvas.pack()

# Shapes
canvas.create_rectangle(30, 30, 130, 100, fill="#ADD8E6", outline="black")
canvas.create_oval(160, 30, 260, 130, fill="#90EE90", outline="black")
canvas.create_line(300, 30, 420, 120, width=3)

# Dog head
canvas.create_oval(150, 180, 350, 350, fill="#D2B48C", outline="black")

# Ears
canvas.create_oval(130, 150, 200, 260, fill="#A0522D", outline="black")
canvas.create_oval(300, 150, 370, 260, fill="#A0522D", outline="black")

# Eyes
canvas.create_oval(200, 230, 230, 260, fill="white")
canvas.create_oval(270, 230, 300, 260, fill="white")

canvas.create_oval(210, 240, 225, 255, fill="black")
canvas.create_oval(280, 240, 295, 255, fill="black")

# Nose
canvas.create_oval(240, 270, 260, 290, fill="black")

# Smile (matches screenshot)
canvas.create_arc(220, 300, 280, 350, start=0, extent=-180, style=tk.ARC, width=2)

# Tongue
canvas.create_oval(240, 300, 260, 330, fill="pink")

# Name
canvas.create_text(
    250, 490,
    text="Villanueva, Raniel Mark A.",
    font=("Arial", 16, "bold")
)

root.mainloop()
