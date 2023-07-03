from playsound import playsound
from time import sleep

def tone1():
    tone1_wave = "resource/tone1.wav"
    playsound(tone1_wave)

def tone2():
    tone2_wave = "resource/tone2.wav"
    playsound(tone2_wave)

def tone3():
    tone3_wave = "resource/tone3.wav"
    playsound(tone3_wave)

def tone4():
    tone4_wave = "resource/tone4.wav"
    playsound(tone4_wave)

def tone5():
    tone5_wave = "resource/tone5.wav"
    playsound(tone5_wave)

def tone6():
    tone6_wave = "resource/tone6.wav"
    playsound(tone6_wave)

def tone7():
    tone7_wave = "resource/tone7.wav"
    playsound(tone7_wave)

def tone8():
    tone8_wave = "resource/tone8.wav"
    playsound(tone8_wave)

def tone9():
    tone9_wave = "resource/tone9.wav"
    playsound(tone9_wave)

def tone0():
    tone0_wave = "resource/tone0.wav"
    playsound(tone0_wave)

def tone_asterisk():
    tone_asterisk = "resource/aster.wav"
    playsound(tone_asterisk)

def tone_tagar():
    tone_tagar = "resource/tagar.wav"
    playsound(tone_tagar)

def toneA():
    toneA = "resource/toneA.wav"
    playsound(toneA)

def toneB():
    toneB = "resource/toneB.wav"
    playsound(toneB)

def toneC():
    toneC = "resource/toneC.wav"
    playsound(toneC)

def toneD():
    toneD = "resource/toneD.wav"
    playsound(toneD)

def InvokeStr(perintah):
    for c in perintah:
        if c == "1":
            tone1()
        elif c == "2":
            tone2()
        elif c == "3":
            tone3()
        elif c == "4":
            tone4()
        elif c == "5":
            tone5()
        elif c == "6":
            tone6()
        elif c == "7":
            tone7()
        elif c == "8":
            tone8()
        elif c == "9":
            tone9()
        elif c == "0":
            tone0()
        elif c == "*":
            tone_asterisk()
        elif c == "#":
            tone_tagar()
        elif c == "A":
            toneA()
        elif c == "B":
            toneB()
        elif c == "C":
            toneC()
        elif c == "D":
            toneD()
        else:
            pass