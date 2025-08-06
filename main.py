from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TICKS = ""
TIMER = None
# ---------------------------- TIMER STOP ------------------------------- #
def stop_timer():
    global REPS
    REPS = 0
    window.after_cancel(TIMER)
    button1.config(text="Start", command=start_time)
# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global TICKS, REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(time, text="00:00")
    text1.config(text="Timer", fg=GREEN)
    text2.config(text="")
    REPS = 0
    TICKS = ""
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global REPS
    button1.config(text="Stop", command=stop_timer)
    REPS += 1
    if REPS % 2 != 0:
        text1.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif REPS % 8 == 0:
        text1.config(text="Break", fg=PINK)
        count_down(LONG_BREAK_MIN * 60)
    else:
        text1.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER, TICKS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1, count_down, count - 1)
    else:
        start_time()
        if REPS % 2 == 0:
            TICKS += "✔"
            text2.config(text=TICKS)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro GUI Application")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
time = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, 'bold'), fill="white")
canvas.grid(column=1, row=1)

text1 = Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 45, 'bold'))
text1.grid(column=1, row=0)

text2 = Label(fg=GREEN, background=YELLOW, font=(FONT_NAME, 10, 'bold'))
text2.grid(column=1, row=3)

button1 = Button(text="Start", command=start_time)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset_time)
button2.grid(column=2, row=2)

window.mainloop()