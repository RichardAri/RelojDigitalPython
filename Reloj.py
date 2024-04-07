from tkinter import Label, Tk
from time import strftime

window = Tk()
window.title('Reloj Digital')
window.config(bg='black')


def update_clock():
    hour = strftime('%I:%M:%S')
    txt_hour.config(text=hour, fg='green', font=('Helvetica', 48))
    txt_hour.after(1000, update_clock)

bg_color = "#00FF00"
txt_hour = Label(window, fg=bg_color, bg='black')
txt_hour.grid(ipadx=20, ipady=20)

update_clock()

window.mainloop()
