import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="00:00")
    title_label.config(text="Timer")
    global reps
    reps = 0
    window.title("Pomodoro Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break")
    else:
        count_down(work_sec)
        title_label.config(text="Work")

# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    time_string = f"{minutes}:{seconds}"
    timer_label.config(text=time_string)
    window.title(f"Pomodoro - {time_string}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- DRAG WINDOW ------------------------------- #
def start_move(event):
    window.x = event.x
    window.y = event.y

def stop_move(event):
    window.x = None
    window.y = None

def do_move(event):
    x = window.winfo_pointerx() - window.x
    y = window.winfo_pointery() - window.y
    window.geometry(f"+{x}+{y}")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.overrideredirect(True)  # No window border
window.attributes('-topmost', True)  # Always on top
window.config(bg="#1e1e1e")
window.geometry("200x120+100+100")


# Dragging
window.bind("<ButtonPress-1>", start_move)
window.bind("<ButtonRelease-1>", stop_move)
window.bind("<B1-Motion>", do_move)

title_label = tk.Label(window, text="Timer", fg="#ffffff", bg="#1e1e1e", font=("Helvetica", 12))
title_label.pack(pady=(8, 0))

timer_label = tk.Label(window, text="00:00", fg="#00ffcc", bg="#1e1e1e", font=("Helvetica", 28, "bold"))
timer_label.pack()

button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=(10, 10))

start_button = tk.Button(button_frame, text="Start", command=start_timer, font=("Helvetica", 10), width=6, bg="#333333", fg="white")
start_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_timer, font=("Helvetica", 10), width=6, bg="#333333", fg="white")
reset_button.grid(row=0, column=1, padx=5)

def right_click_exit(event):
    window.destroy()

window.bind("<Button-3>", right_click_exit)

window.mainloop()
