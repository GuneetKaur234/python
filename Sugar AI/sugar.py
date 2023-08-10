import speech_recognition as sr
import win32com.client as wincl
import webbrowser
import os
import datetime
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))


def search(data):

    text = data[11:]
    print(text)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)

    url = "https://www.google.com"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys(text)
    search_box.send_keys(Keys.ENTER)


def say(text):
    spk.Speak(f"{text}")


def take_command():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          audio = r.listen(source)
          try:
                query = r.recognize_google(audio)
                print(query)
                return query
          except Exception as e:
               return 'error occurred, sorry'


if __name__ == "__main__":
     
    print('welcome')
    say('hello! My name is Sugar')
    while True:
        print('listening...')
        query = take_command()

        sites = [['youtube','https://www.youtube.com/'],['google','https://www.google.com/'],['wikipedia','https://www.wikipedia.com/']]

        for site in sites:
          if f'{site[0]}'.lower() in query.lower():
             say(f'opening {site[0]}')
             webbrowser.open(site[1])

        if "hello Sugar" in query:
            say('hello guneet')

        elif "play music" in query:
            music_path = "D:\guneet\study\python\Drinking Water.mp3"
            os.startfile(music_path)

        elif "time" in query:
            time_now = datetime.datetime.now().strftime("%I:%M:%p")
            say(time_now)

        elif "joke" in query:
            joke = pyjokes.get_joke(language="en")
            say(joke)

        elif "Chrome" in query:
            chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            say('opening chrome')
            os.startfile(chrome)

        elif "calculator" in query:
            calculator = "C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2210.0.0_x64__8wekyb3d8bbwe\CalculatorApp.exe"
            say("opening calculator")
            os.startfile(calculator)

        elif "Notepad" in query:
            notepad ="C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2305.18.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            say('opening notepad')
            os.startfile(notepad)

        elif "spotify" in query:
            spotify = 'C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.216.947.0_x64__zpdnekdrzrea0\SpotifyMigrator.exe'
            say('opening spotify')
            os.startfile(spotify)
        
        elif "store" in query:
            store = "C:\Program Files\WindowsApps\Microsoft.WindowsStore_22306.1401.1.0_x64__8wekyb3d8bbwe\WinStore.App.exe"
            say('opening windows store')
            os.startfile(store)

        elif "WhatsApp" in query:
            whatsapp = "C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2327.6.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"
            say('opening whatsapp')
            os.startfile(whatsapp)

        elif "search" in query.lower():
              search(query)