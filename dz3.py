from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Quiz")
window.geometry("700x300")
window.config(bg="skyblue")
question = Label(
    window,
    text="Which animal do people walk on\nand cars drive on?",
    font=("Arial", 18, "bold"),
    bg="skyblue"
)
question.place(x=120, y=20)
def correct():
    messagebox.showinfo("Answer", "Correct! It is a zebra.")
def wrong():
    messagebox.showerror("Answer", "Wrong answer!")

Button(window, text="Horse", width=12, height=4,
  command=wrong).place(x=70, y=140)

Button(window, text="Zebra", width=12, height=4,
 command=correct).place(x=290, y=140)

Button(window, text="Giraffe", width=12, height=4,
     command=wrong).place(x=510, y=140)
horse = PhotoImage(file="horse.png")
label = Label(window, image=horse)
label.place(x=50, y=100)
zebra = PhotoImage(file="zebra.png")
label = Label(window, image=zebra)
label.place(x=250, y=100)

giraffe = PhotoImage(file="giraffe.png")
label = Label(window, image=giraffe)
label.place(x=470, y=100)


window.mainloop()