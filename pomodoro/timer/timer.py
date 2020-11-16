import time
import datetime as dt

import tkinter
from tkinter import messagebox
from tkinter import simpledialog

root = tkinter.Tk()
root.withdraw()

total_pomodoros = 0
POMODORO_SEC = 25*60       #3*60                         # Pomodoro time                 [int, seconds]
DELTA_SEC = 5*60         #1*60                           # Break time, after pomodoro    [int, seconds]

current_time = dt.datetime.now()                       # Current time for reference.   [datetime object]
remaining_time = dt.timedelta(0,POMODORO_SEC)          # Time delta in mins            [datetime object]
final_productive_time = current_time + remaining_time               # Future time for reference     [datetime object]
final_break_time = current_time + dt.timedelta(0,POMODORO_SEC+DELTA_SEC) # Final time (w/ 5 mins break)  [datetime object]

print(f"Bug check 0: \nt_now: {current_time}\nend_time: {final_productive_time}")

messagebox.showinfo("Pomodoro Started!", "\nIt is now "+current_time.strftime("%H:%M") + " \nTimer set for 25 mins.")
print("Pomodoro Started!", "\nIt is now "+current_time.strftime("%H:%M") +
" hrs. \nTimer set for 25 mins.")


while True:

    # check if time is still in the 25 minutes interval 
    if current_time < final_productive_time:
        print('First tnow < tfut')
        print ('final_productive_time : ' + final_productive_time.strftime("%H:%M"))
        print ('final_break_time : ' + final_break_time.strftime("%H:%M"))
        print('\007') #this is supposed to make a noise ...
        
    # check if time is in the 5 minutes break interval 
    elif final_productive_time < current_time < final_break_time:
        print('Break time!')
        messagebox.showinfo("Break Time! ", "The 5 minutes break will end at  \n " + final_productive_time.strftime("%H:%M") )

    #after pomodoro and break 
    else:
        print('Done!')

        usr_ans = messagebox.askyesno("Pomodoro Finished!","Do you want to start another pomodoro?") 
        total_pomodoros = total_pomodoros + 1
        
        if usr_ans == True:
            # new pomodoro will update current time
            current_time = dt.datetime.now()
            final_productive_time = current_time + dt.timedelta(0,POMODORO_SEC)
            final_break_time = current_time + dt.timedelta(0,POMODORO_SEC+DELTA_SEC)
            continue
        
        elif usr_ans == False:
            # no more pomodoros
            print(f'Pomodoro timer complete! \nYou have completed {total_pomodoros} pomodoros today.')
            messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+ timenow +
            "\nYou completed "+ str(total_pomodoros)+" pomodoros so far today!")
            break
        
    #update current time every 10 milisecpnds
    time.sleep(10)
    current_time = dt.datetime.now()
    timenow = current_time.strftime("%H:%M")

print('\n\nMade it to the end!\n\n')