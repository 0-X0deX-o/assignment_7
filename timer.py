import time, datetime, os

def clear():
    os.system('cls')

def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end='\r')
        time.sleep(1)
        total_seconds -= 1
    os.system('start "C:\Program Files\Google\Chrome\Application\chrome.exe" "C:\\Users\pc0\startup_page\\alarm.html"')
    exit()
    os.system('exit')
    # os.system('$PlayWav=NewObject System.Media.SoundPlayer')
    # os.system('$PlayWav.SoundLocation="C:\\Users\pc0\Downloads\mixkit-scanning-sci-fi-alarm-905.wav"')
    # os.system('$PlayWav.playsync()')
h = int(input('Enter Hours: '))
m = int(input('Enter minutes: '))
s = int(input('Enter seconds: '))
clear()
countdown(h,m,s)