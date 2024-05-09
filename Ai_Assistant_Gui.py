from Lock_Assistant import verify_password
import random
import json
import torch.cuda
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

# todo *********************************************************** GUI
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from mainGUI import Ui_Form


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# todo -----------------------------------------------------
Name = "AI Virtual Assistant"
from Listen import Listen
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution


def Main():
    sentence = Listen()
    query = str(sentence)

    if sentence == "bye":
        Say("Going to sleep,Thank You")
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                # reply => RandomResponse by Model, query => str(sentence) == Command by user

                # Task Implementation----
                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "day" in reply:
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    InputExecution(reply, sentence)

                elif "alarm" in reply:
                    InputExecution(reply, query)

                elif "random advice" in reply:
                    NonInputExecution(reply)

                elif "translate" in reply:
                    InputExecution(reply, query)

                elif "internet speed" in reply:
                    NonInputExecution(reply)

                elif "movie" in reply:
                    InputExecution(reply, tag)

                elif "news" in reply:
                    InputExecution(reply, query)

                elif "temperature" in reply:
                    InputExecution(reply, query)

                elif "open" in reply:
                    InputExecution(reply, query)

                elif "close" in reply:
                    InputExecution(reply, query)

                elif "search on google" in reply:
                    InputExecution(reply, query)

                elif "search on youtube" in reply:
                    InputExecution(reply, query)

                elif "whatsapp" in reply:
                    InputExecution(reply, query)

                elif "change password" in reply:
                    InputExecution(reply, query)

                elif "screenshot" in reply:
                    NonInputExecution(reply)

                elif "take my photo" in reply:
                    NonInputExecution(reply)

                elif "ai image" in reply:
                    InputExecution(reply, query)

                elif "game" in reply:
                    NonInputExecution(reply)

                elif "ip address" in reply:
                    NonInputExecution(reply)

                elif "set schedule" in reply:
                    InputExecution(reply, query)

                elif "show my schedule" in reply:
                    InputExecution(reply, query)

                elif "shutdown system" in reply:
                    NonInputExecution(reply)

                elif "play" in reply:
                    NonInputExecution(reply)

                elif "pause" in reply:
                    NonInputExecution(reply)

                elif "mute" in reply:
                    NonInputExecution(reply)

                elif "unmute" in reply:
                    NonInputExecution(reply)

                elif "volume up" in reply:
                    NonInputExecution(reply)

                elif "volume down" in reply:
                    NonInputExecution(reply)

                elif "remember that" in reply:
                    NonInputExecution(reply)

                elif "do you remember anything" in reply:
                    NonInputExecution(reply)

                elif "send email" in reply:
                    InputExecution(reply, query)


                else:
                    Say(reply)

class Main_thread(QThread):
    def __init__(self):
        super(Main_thread, self).__init__()
        print("setting up GUI")

    def run(self):
        self.runjarvis()


    def runjarvis(self):
        if verify_password():
            while True:
                Main()


startExecution = Main_thread()

class GUi_jarvis(QWidget):
    def __init__(self):
        super(GUi_jarvis, self).__init__()
        self.ui = loadUi("mainGUI.ui", self)

        self.ui.StartButton.clicked.connect(self.runAllMovies)
        self.ui.ExitButton.clicked.connect(self.close)
        self.ui.enterButton.clicked.connect(self.manualCodeFromTerminal)



    def runAllMovies(self):
        try:
            # arc gif in center (always in running state)
            self.ui.movie = QtGui.QMovie("C:\\Users\\anish\\Desktop\\Ai_Virtual_Assistant\\GuiFinal\\arc.gif")
            self.ui.arcLabelCenter.setMovie(self.ui.movie)
            self.ui.movie.start()
            # mic
            self.ui.movie = QtGui.QMovie("C:\\Users\\Administrator\\PycharmProjects\\AiVirtualAssistant\\GuiFinal")
            self.ui.micLabel.setMovie(self.ui.movie)
            self.ui.movie.start()
            # earth
            self.ui.movie = QtGui.QMovie("C:\\Users\\Administrator\\PycharmProjects\\AiVirtualAssistant\\GuiFinal\\Earth.gif")
            self.ui.Earth.setMovie(self.ui.movie)
            self.ui.movie.start()
            # wave
            self.ui.movie = QtGui.QMovie("C:\\Users\\Administrator\\PycharmProjects\\AiVirtualAssistant\\GuiFinal\\Speak.gif")
            self.ui.Wave.setMovie(self.ui.movie)
            self.ui.movie.start()
            # ironman
            self.ui.movie = QtGui.QMovie("C:\\Users\\Administrator\\PycharmProjects\\AiVirtualAssistant\\GuiFinal\\ironman1.gif")
            self.ui.ironman.setMovie(self.ui.movie)
            self.ui.movie.start()

            startExecution.start()

        except Exception as e:
            window.terminalPrint("error found in Run all jarvis")
            window.terminalPrint(e)

    def updateMoviesDynamically(self, state):
        try:
            if state == "listening":
                self.ui.micLabel.raise_()
                self.ui.micLabel.show()
                self.ui.Wave.hide()
                self.ui.Earth.hide()

            elif state == 'speaking':
                self.ui.micLabel.hide()
                self.ui.Wave.raise_()
                self.ui.Wave.show()
                self.ui.Earth.hide()

            elif state == 'recognizing':
                self.ui.micLabel.hide()
                self.ui.Wave.hide()
                self.ui.Earth.show()
                self.ui.Earth.raise_()
        except Exception as e:
            window.terminalPrint("error found in updateMoviesDynamically")
            window.terminalPrint(e)

    def terminalPrint(self, text):
        self.ui.aiOutput.appendPlainText(text)

    def manualCodeFromTerminal(self):

        cmd = self.ui.userInput.text()
        if cmd:
            self.ui.userInput.clear()
            self.ui.userInput.appendPlainText(f"You just typed >> {cmd}")

            if cmd == "exit":
                window.close()

            elif cmd == 'help':
                self.terminalPrint("I can Perform various task Which is Programmed inside me By -A.R.A-")

            else:
                pass
        else:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUi_jarvis()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")