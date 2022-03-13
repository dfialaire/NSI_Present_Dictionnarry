# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:13:05 2022

@author: dfial
"""
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write ## enregistrer des fichiers WAV à partir de données
import wavio as wv 
import speech_recognition as sr  ## module de reconnaissance verbale API Google (internet branché)
####
import pyttsx3  ## pour parler
#####   Demmarage du moteur de paraole  ######
engine = pyttsx3.init()
# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
#########################################################
def parle(phrase):
    engine.say(phrase)
    engine.runAndWait()
#############################################
def enregistre():
    yepi="Je vous écoute"
    engine.say(yepi)
    engine.runAndWait()
    freq = 44100
    duration = 3
    recording = sd.rec(int(duration * freq), 
    				samplerate=freq, channels=2) 
    sd.wait() 
    wv.write("recording1.wav", recording, freq, sampwidth=2)     
##############
def reconn():
    r = sr.Recognizer()
    audio = sr.AudioFile('recording1.wav')
    with audio as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio_file = r.record(source)
    try:            
        result = r.recognize_google(audio_file, language="fr-FR")
        print("result = ", result)
        return result
    except sr.UnknownValueError:
        print("Désolé.. Non compris.")
#########################
Dico_Fran_Ang = {'Bonjour':'hello', 'école':'school','voiture':'car','fleur':'flower','chien':'dog','valise':'suitcase','Bonjour à tous':'hello everybody','oridnateur':'computer'}
# for k,v in Dico_Fran_Ang.items():
#     phrase = k
#     parle(phrase)
#     phrase = v
#     parle(phrase)
#################################
while True:
    enregistre()
    resultat = reconn()
    if resultat == 'stop':
        break
    elif resultat in Dico_Fran_Ang:
        phrase = Dico_Fran_Ang[resultat]
        parle(phrase)
