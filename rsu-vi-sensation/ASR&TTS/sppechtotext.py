import speech_recognition as sr
import pyttsx3
import pyaudio

index=pyaudio.PyAudio().get_device_count() - 1
print(index)

r = sr.Recognizer()

def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

while(1):
	try:
		with sr.Microphone() as source2:
			print("Start saying")
			r.adjust_for_ambient_noise(source2, duration=0.2)
			audio2 = r.listen(source2)
			#MyText = r.recognize_sphinx(audio2)
			#MyText = MyText.lower()

			print("Did you say ", r.recognize(audio2))
			SpeakText(r.recognize(audio2))
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	except sr.UnknownValueError:
		print("unknown error occured")
