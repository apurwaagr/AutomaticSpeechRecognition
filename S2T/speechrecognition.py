import torch
import whisper
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Start Speaking ... ")
	while True:
		audio = r.listen(source)
		result = r.recognize_whisper(audio)
		print(result)
