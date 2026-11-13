from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Quiz")
window.geometry("700x300")
window.config(bg="skyblue")
horse = PhotoImage(file="horse.png")
zebra = PhotoImage(file="zebra.png")
giraffe = PhotoImage(file="giraffe.png")
penguin = PhotoImage(file="penguin.png").subsample(4, 4)
chicken = PhotoImage(file="chicken.png").subsample(4, 4)
duck = PhotoImage(file="duck.png").subsample(4, 4)

def wrong():
    messagebox.showerror("Answer", "Wrong answer!")
def win():
    messagebox.showinfo("Answer", "Correct! It is a penguin!")
    window.destroy()

def next_q():
    messagebox.showinfo("Answer", "Correct! It is a zebra.")
    question.config(text="Which bird cannot fly at all?")
    btn1.config(image=penguin, command=win)
    btn2.config(image=chicken, command=wrong)
    btn3.config(image=duck, command=wrong)

question = Label(window, text="Which animal do people walk on\nand cars drive on?", font=("Arial", 18, "bold"), bg="skyblue")
question.place(x=120, y=20)
btn1 = Button(window, image=horse, width=120, height=120, command=wrong)
btn1.place(x=80, y=120)
btn2 = Button(window, image=zebra, width=120, height=120, command=next_q)
btn2.place(x=290, y=120)
btn3 = Button(window, image=giraffe, width=120, height=120, command=wrong)
btn3.place(x=500, y=120)
window.mainloop()
