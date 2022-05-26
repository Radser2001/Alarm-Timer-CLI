from win10toast import ToastNotifier
import time
import datetime
import webbrowser

print('   ██╗  ░█████╗░██╗░░░░░░█████╗░██████╗░███╗░░░███╗  ░░░░██╗  ████████╗██╗███╗░░░███╗███████╗██████╗░ ██╗  ')
print('   ╚█║  ██╔══██╗██║░░░░░██╔══██╗██╔══██╗████╗░████║  ░░░██╔╝  ╚══██╔══╝██║████╗░████║██╔════╝██╔══██╗ ╚█║  ')
print('   ░╚╝  ███████║██║░░░░░███████║██████╔╝██╔████╔██║  ░░██╔╝░  ░░░██║░░░██║██╔████╔██║█████╗░░██████╔╝ ░╚╝  ')
print('        ██╔══██║██║░░░░░██╔══██║██╔══██╗██║╚██╔╝██║  ░██╔╝░░  ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗      ')
print('        ██║░░██║███████╗██║░░██║██║░░██║██║░╚═╝░██║  ██╔╝░░░  ░░░██║░░░██║██║░╚═╝░██║███████╗██║░░██║      ')
print('        ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░░░  ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝      ')

print('               ██████╗░░█████╗░██████╗░░██████╗███████╗██████╗░██████╗░░█████╗░░█████╗░░░███╗░░')
print('               ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗╚════██╗██╔══██╗██╔══██╗░████║░░')
print('             < ██████╔╝███████║██║░░██║╚█████╗░█████╗░░██████╔╝░░███╔═╝██║░░██║██║░░██║██╔██║░░ >')
print('               ██╔══██╗██╔══██║██║░░██║░╚═══██╗██╔══╝░░██╔══██╗██╔══╝░░██║░░██║██║░░██║╚═╝██║░░')
print('               ██║░░██║██║░░██║██████╔╝██████╔╝███████╗██║░░██║███████╗╚█████╔╝╚█████╔╝███████╗')
print('               ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚══════╝')
print('                                            (っ◔◡◔)っ ❤                                      ')
print("\n")


def openlink():
    webbrowser.open('https://github.com/Radser2001')
    print('debug - went')
    

def countdowm(hours, minutes, seconds):
    
    if(mode == 'op'):
        start = "yes"
        while start == "yes"  or sessions == 0:
             total_seconds = hours * 3600 + minutes * 60 + seconds

             while total_seconds >= 0:
            
                timer = datetime.timedelta(seconds=total_seconds)
                time.sleep(1)
                total_seconds -= 1
                print("\t",timer, end="\r")
                
             toaster = ToastNotifier()

             toaster.show_toast("RADSER OP","\nBreak!!!")
             total_seconds =  300
             
             while total_seconds >= 0:
            
                timer = datetime.timedelta(seconds=total_seconds)
                time.sleep(1)
                total_seconds -= 1
                print("\t",timer, end="\r")
                
             toaster.show_toast("RADSER OP","\nBreak over!!!")
             sessions -= 1
             start = input("Start new session (yes/no):").lower()
             
        toaster = ToastNotifier()

        toaster.show_toast("RADSER OP","\nSessions are OVER!!!")

        print("Have a nice day!!! (っ◔◡◔)っ ❤\n")
        go_to = input("Enter go to visit my Github :").lower()
        if go_to == 'go':
            openlink()

             

    else:
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

        print("Have a nice day!!! (っ◔◡◔)っ ❤\n")
        go_to = input("Enter go to visit my Github :").lower()
        if go_to == 'go':
            openlink


print('█▀▄▀█ █▀█ █▀▄ █▀▀   ▄█   ▀   ▄▀█ █░░ ▄▀█ █▀█ █▀▄▀█')
print('█░▀░█ █▄█ █▄▀ ██▄   ░█   ▄   █▀█ █▄▄ █▀█ █▀▄ █░▀░█')
print("\n")

print('█▀▄▀█ █▀█ █▀▄ █▀▀   ▀█   ▀   ▀█▀ █ █▀▄▀█ █▀▀ █▀█')
print('█░▀░█ █▄█ █▄▀ ██▄   █▄   ▄   ░█░ █ █░▀░█ ██▄ █▀▄')
print("\n")


print('█▀▄▀█ █▀█ █▀▄ █▀▀   █░█   ▀   █▀█ █▀█ ▀█▀ █ █▀▄▀█ ▄▀█ █░░   █▀ ▀█▀ █░█ █▀▄ █▄█   █▀█ █░░ ▄▀█ █▄░█')
print('█░▀░█ █▄█ █▄▀ ██▄   ▀▀█   ▄   █▄█ █▀▀ ░█░ █ █░▀░█ █▀█ █▄▄   ▄█ ░█░ █▄█ █▄▀ ░█░   █▀▀ █▄▄ █▀█ █░▀█' + '\n25 min study 5 min break')
print("\n")



select = int(input("Enter 1 or 2 or 4 : "))

if select == 1:
    mode = 'alarm'
    
elif select == 2:
    mode = 'timer'
    
elif select == 4:
    mode = 'op'

else:
    mode = 'timer'
    
print("\n---Set a time for the", mode + "---")

if mode == 'timer' or mode == 'alarm':
    hours= int(input("\nHours: "))
    minutes= int(input("Minutes:"))
    seconds = int(input("seconds: "))
else:
    hours = int(0)
    minutes = int(25)
    seconds = int(0)

current_date_and_time = datetime.datetime.now()

hours_added = datetime.timedelta(hours = hours)
minutes_added = datetime.timedelta(minutes = minutes)
seconds_added = datetime.timedelta(seconds = seconds)

alarm_set_time = current_date_and_time + hours_added + minutes_added + seconds_added


if mode == "alarm":
    print("\n*******", mode.capitalize(), "will go off at -> ", alarm_set_time , "*******")
    choice = input("\n\nDo you want the countdown (y/n) ? ")
    
if mode == "op":
    sessions = input("Enter number of sessions :")
    choice = input("\n\nDo you want the countdown (y/n) ? ")

print("\n")

countdowm(hours, minutes, seconds)
