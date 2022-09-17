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
reps = 0
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global checks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checks = ""
    reps = 0
    check_label.config(text=checks)
    timer_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps > 8:
        pass
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global checks
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            checks += "✓"
            check_label.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="", bg=YELLOW, font=(FONT_NAME, 15, "bold"), fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
