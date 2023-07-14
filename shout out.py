import win32com.client as wincl

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)



user_names = input("Enter your name and your friends names seperated by comas = ")
name_list = user_names.split(",")

for x in name_list:
    spk.Speak(f"Hello, {x} Hope you are doing good")

spk.Speak("Zira, this side happy to meet you")



