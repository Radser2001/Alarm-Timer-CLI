from win10toast import ToastNotifier
import time
import datetime

print('''
            #####################################
               ' ALARM / TIMER '  by radser2001
            #####################################
''')

def countdowm(hours, minutes, seconds):

    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        
        timer = datetime.timedelta(seconds=total_seconds)

        if mode == 'timer':
            print("\t",timer, end="\r")

        elif mode == "alarm":
            if  choice == 'y': 
                print("\t",timer, end="\r")

        time.sleep(1)

        total_seconds -= 1
        
    toaster = ToastNotifier()

    toaster.show_toast("RADSER alarm","\nTIME IS OVER!!!")

    print("Have a nice day!!!\n")



mode = input("Alarm or timer (alarm/timer)? ").lower()

print("\n---Set a time for the", mode + "---")

hours= int(input("\nHours: "))
minutes= int(input("Minutes:"))
seconds = int(input("seconds: "))

current_date_and_time = datetime.datetime.now()

hours_added = datetime.timedelta(hours = hours)
minutes_added = datetime.timedelta(minutes = minutes)
seconds_added = datetime.timedelta(seconds = seconds)

alarm_set_time = current_date_and_time + hours_added + minutes_added + seconds_added


if mode == "alarm":
    print("\n*******", mode.capitalize(), "will go off at -> ", alarm_set_time , "*******")
    choice = input("\n\nDo you want the countdown (y/n) ? ")

print("\n")

countdowm(hours, minutes, seconds)