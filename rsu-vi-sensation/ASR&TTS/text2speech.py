from gtts import gTTS

import os

mytext = input("Enter your text: ")
language = 'en'

myobj =gTTS(text=mytext, lang=language, slow=False)
myobj.save("test.mp3")
os.system("mpg321 test.mp3")
