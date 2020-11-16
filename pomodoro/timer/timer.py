import time
import datetime as dt

import tkinter
from tkinter import messagebox
from tkinter import simpledialog


class Pomodoro():
    
    POMODORO_SEC = 25*60       #3*60                         # Pomodoro time                 [int, seconds]
    DELTA_SEC = 5*60         #1*60                           # Break time, after pomodoro    [int, seconds]
    
    def __init__(self):
    
        self.root = tkinter.Tk()
        self.root.withdraw()

        self.total_pomodoros = 0
        
        self.current_time = dt.datetime.now()                       # Current time for reference.   [datetime object]
        self.pomodoro_length = dt.timedelta(0, self.POMODORO_SEC)          # Time delta in mins            [datetime object]
        self.final_productive_time = self.current_time + self.pomodoro_length               # Future time for reference     [datetime object]
        self.final_break_time = self.current_time + dt.timedelta(0, self.POMODORO_SEC+ self.DELTA_SEC) # Final time (w/ 5 mins break)  [datetime object]

        print(f"Bug check 0: \nt_now: {self.current_time}\nend_time: {self.final_productive_time}")

        messagebox.showinfo("Pomodoro Started!", "\nIt is now "+ self.current_time.strftime("%H:%M") + " \nTimer set for 25 mins.")
        print("Pomodoro Started!", "\nIt is now "+ self.current_time.strftime("%H:%M") +
        " hrs. \nTimer set for 25 mins.")


    def start_new_timer(self):
        '''
            Resets time variables for a new pomodoro.
        '''
        # set start & end times
    
        self.current_time = dt.datetime.now()
        self.final_productive_time = self.current_time + dt.timedelta(0, self.POMODORO_SEC)
        self.final_break_time = self.current_time + dt.timedelta(0, self.POMODORO_SEC + self.DELTA_SEC)
        print('\n---- Began new pomodoro! ----\n')

def main():
    alert = 0 
    pomodoro = Pomodoro()
    final_productive_time = pomodoro.final_productive_time 
    
    while True:

        # check if time is still in the 25 minutes interval 
        if pomodoro.current_time < pomodoro.final_productive_time:
            print('\007') #this is supposed to make a noise ...
            
        # check if time is in the 5 minutes break interval 
        elif pomodoro.final_productive_time < pomodoro.current_time < pomodoro.final_break_time:
            if (alert == 0 ):
                print('Break time!')
                messagebox.showinfo("Break Time! ", "The 5 minutes break will end at  \n " + final_productive_time.strftime("%H:%M") )
                alert = 1

        #after pomodoro and break 
        else:
            print('Done!')
            usr_ans = messagebox.askyesno("Pomodoro Finished!","Do you want to start another pomodoro?") 
            pomodoro.total_pomodoros = pomodoro.total_pomodoros + 1
            
            if usr_ans == True:
                # new pomodoro will update current time
                pomodoro.start_new_timer()
                alert = 0
                continue
            
            elif usr_ans == False:
                # no more pomodoros
                print(f'Pomodoro timer complete! \nYou have completed {pomodoro.total_pomodoros} pomodoros today.')
                messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+ pomodoro.current_time.strftime("%H:%M") +
                "\nYou completed "+ str(pomodoro.total_pomodoros)+" pomodoros so far today!")
                break
            
        #update current time every 10 miliseconds
        time.sleep(10)
        pomodoro.current_time = dt.datetime.now()
        pomodoro.timenow = pomodoro.current_time.strftime("%H:%M")

    print('\n\nMade it to the end!\n\n')
    
if __name__ == '__main__':
    main()