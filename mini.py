import datetime,subprocess,os,pyautogui,string,random
import pyttsx3
import speech_recognition as sr
import sounddevice
from scipy.io.wavfile import write
from tkinter import filedialog
from tkinter import *

class SpeakRecog:
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    # print(voices[].id)
    # print(voices)

    """ VOICE RATE"""
    rate = engine.getProperty('rate')               # getting details of current speaking rate
    # print(rate)
    engine.setProperty('rate', 170)                 # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')           #getting to know current volume level (min=0 and max=1)
    # print(volume)                                 #printing current volume level
    engine.setProperty('volume', 1.0)               # setting up volume level  between 0 and 1

    def speak(self,audio):
        """It speaks the audio"""
        print(audio)
        self.engine.say(audio)
        # engine.save_to_file('Hello World', 'test.mp3')
        self.engine.runAndWait()
        # engine.stop()

    def takeCommand(self):
        """It take microphone input from the user and return string"""
        recog=sr.Recognizer()
        # mic=Microphone()
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            print("Listening....")
            recog.pause_threshold = 1
            # r.energy_threshold = 45.131829621150224
            # print(sr.Microphone.list_microphone_names())
            #print(r.energy_threshold)
            audio=recog.listen(source)
        try:
            print("Recognizing...")
            query= recog.recognize_google(audio)
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return 'None'
        return query

class TextSpeech:
    def speak(self):
        root=Tk()
        root.withdraw()
        file_path=filedialog.askopenfilename(initialdir = "/",title="Select file",filetypes=(('text file',"*.txt"),("All files", "*.*")))
        with open(file_path,'r') as f:
            g=f.read()
        SR=SpeakRecog()
        SR.speak(g)
        del SR

class note:
    def Note(self,data):
        date=datetime.datetime.now()
        filename=str(date).replace(':','-')+'-note.txt'
        a=os.getcwd()
        if not os.path.exists('Notes'):
            os.mkdir('Notes')
        os.chdir(a+r'\Notes')
        with open(filename,'w') as f:
            f.write(data)
        subprocess.Popen(['notepad.exe',filename])
        os.chdir(a)

class screenshot:
    def takeSS(self):
        img_captured=pyautogui.screenshot()
        a=os.getcwd()
        if not os.path.exists("Screenshots"):
            os.mkdir("Screenshots")
        os.chdir(a+'\Screenshots')
        date=datetime.datetime.now()
        img_captured.save('screenshot-'+str(date).replace(':','-')+'.png')
        os.chdir(a)

class PasswordGenerator:
    def givePSWD(self):
        SR=SpeakRecog()
        SR.speak("What type of password you want")
        print("\nPassword Level we have:-\n\nPoor Level\nAverage Level\nStrong Level\n")
        while(True):
            query=SR.takeCommand().lower()
            if ('poor' in query):
                return "Your Password is = "+"".join(random.sample(string.ascii_letters,7))
                break
            elif ('average' in query):
                return "Your Password is = "+"".join(random.sample(string.ascii_letters+string.digits,10))
                break
            elif ('strong' in query):
                return "Your Password is = "+"".join(random.sample(string.ascii_letters+string.digits+string.punctuation,13))
                break
            else:
                SR.speak("Please say it again")
        del SR

class GuessTheNumber:
    def start(self):
        n=random.randint(1,10)
        SR=SpeakRecog()
        attempt=0
        SR.speak("Guess a number between 1 to 10. \nTo become winner of the game you need to guess the number within 3 attempts.")
        while(True):
            guess=int(input("Enter number: "))
            if guess<n:
                SR.speak("Your guess was low.")
            elif guess>n:
                SR.speak("Your guess was high")
            elif guess==n:
                SR.speak("yep you got it.")
                break
            else:
                SR.speak("Invalid data. Please enter right data.")
            attempt+=1
        if attempt>=3:
            print(f"Your attempts= {attempt}")
            SR.speak("Looser. \n Good luck next time")
        else:
            SR.speak("Congratulations. You are winner of the game.")
        del SR

class VoiceRecorer:
    def Record(self):
        SR=SpeakRecog()
        SR.speak("This recording is of 10 seconds.")
        fs=44100
        second=10
        print("Recording.....")
        record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
        sounddevice.wait()
        a=os.getcwd()
        if not os.path.exists("Recordings"):
            os.mkdir("Recordings")
        os.chdir(a+'\Recordings')
        write("Recording-"+str(datetime.datetime.now()).replace(':','-')+".wav",fs,record_voice)
        SR.speak("Voice is recorded in \'Recordings\' folder.")
        os.chdir(a)
        del SR