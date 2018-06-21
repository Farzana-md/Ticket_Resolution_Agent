from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

"""This is the ticket Resolution web service which takes the user IT query as input from web browser and gives the solution to it in the web browser"""

app = Flask(__name__)

chatbot = ChatBot('Ticket_Resolution_Agent')
chatbot.set_trainer(ListTrainer)


for files in os.listdir('./hackathon_corpus'):
    file_name=os.path.join('./hackathon_corpus',files)
    data=open(file_name,'r').readlines()
    chatbot.train(data)

@app.route("/")
def home():
    return render_template("basic.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()

