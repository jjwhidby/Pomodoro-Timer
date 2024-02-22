import time
from tkinter import *

# Define timer lengths
pomodoro_time = 25 # minutes
short_break_time = 5
long_break_time = 20

# Global variables
current_time = 0
current_status = "Pomodoro"
reps = 0

def start_timer():
    global current_time, current_status, reps
    if current_status == "Pomodoro":
        current_time = pomodoro_time * 60 # convert to seconds
    elif current_status == "Short Break":
        current_time = short_break_time * 60
    elif current_status == "Long Break":
        current_time == long_break_time * 60
    
    reps += 1 
    count_down()
    start_button.config(state="disabled")

def count_down():
    global current_time, current_status
    if current_time > 0:
        current_time -= 1
        time_string = f"{int(current_time / 60):02d}:{int(current_time % 60):02d}"
        timer_label.config(text = time_string)
        timer_label.after(1000, count_down)
    else:
        if current_status == "Pomodoro":
            if reps % 4 == 0:
                current_status = "Long Break"
            else:
                current_status = "Short Break"
        else:
            current_status = "Pomodoro"
        start_button.config(state="normal")





# Create the main window
root = Tk()
root.title("Pomodoro Timer")

# Create labels and buttons
timer_label = Label(root, font=("Arial", 40), text="25:00")
start_button = Button(root, text="Start", command=start_timer)
status_label = Label(root, font=('Arial', 25), text=current_status )

# Layout the widgets
timer_label.pack(pady=20)
start_button.pack(pady=20)
status_label.pack()

#Run the main loop
root.mainloop()
