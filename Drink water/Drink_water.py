from datetime import datetime, timedelta
import time
import win32com.client as wincl
from plyer import notification

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))

for x in range(0,5):
    time.sleep(1)
    print("hello")
    present_time = (datetime.now())
    x= (present_time + timedelta(seconds=10)).strftime('%H:%M:%S')
    spk.Speak(f"Hello, its been 10 seconds, its time to Drink water")
    notification.notify(
    title = 'Reminder',
    message = 'Drink Water',
    timeout = 10,
    
)



        






