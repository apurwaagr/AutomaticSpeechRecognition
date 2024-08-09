import speech_recognition as sr

def listen():
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		print("Start")
		audio = r.listen(source, timeout=10)
		return r.recognize_sphinx(audio)
		print("Thankyou! Time Over")
		pass
print(listen())
