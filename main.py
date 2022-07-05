from tkinter import *


window = Tk()
window.title('Disappearing Text App')
window.config(bg='#F5F5F5')
window.config(padx=15, pady=15)


title = Label(
    text='Disappearing Text App',
    font=('Arial', 19)
)
title.grid(row=0, column=1)

explainer = Label(
    text='Stop Typing for 5 seconds and loose all your work!',
    font=('Arial', 11)
)
explainer.grid(row=1, column=1)

entry_box = Text(
    height=10,
    width=52,
    font=('Helvetica', 15),
    wrap='word',
    padx=10,
    pady=10,
)
entry_box.grid(row=2, column=1)

STARTING_LENGTH = 0


def disappearing_text():
    global STARTING_LENGTH
    window.after(5000, disappearing_text)
    current_length = len(entry_box.get('1.0', 'end-1c'))
    if STARTING_LENGTH == current_length:
        entry_box.delete('1.0', 'end')

    elif STARTING_LENGTH != current_length:
        new_lenght = len(entry_box.get('1.0', 'end-1c'))
        STARTING_LENGTH = new_lenght


def start(event):
    disappearing_text()
    return event


entry_box.bind('<FocusIn>', start)
window.mainloop()
