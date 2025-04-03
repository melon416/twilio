import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from main import Bot
from send_sms import send_sms

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    number = request.form['From']
    message_body = request.form['Body']
    print("numebr", number, message_body)
    command = message_body.split(' ')[0]
    username = ''
    if command.lower() == "create":
        username = message_body.split(' ')[1]
        print("username:",username)
        if username != '':
            # start the account creation automation
            bot = Bot()
            res = bot.main(username)
            if res == "success":
                print("successsss")
                # resp = MessagingResponse()
                # resp.message("Account has been successfully created. Password:123123")
                content = "Account has been successfully created. Password:123123" + "\n" + "Text the word <load> to add Firekirin Credits"
                send_sms(number, content)
                print("message sent")
            elif res == "exist":
                content = "Username already exists. Please use another!"
                send_sms(number, content)
            else:
                print("failll")
                content = "Sth went wrong. Please try it again!"
                send_sms(number, content)
        else:
            content = "Please send us the username!" + "\n" + "Example: Create Mark2021"
            send_sms(number, content)
    elif command.lower() == "load":
        content = "https://commerce.coinbase.com/checkout/54fe4b21-7261-4e36-9dab-912b2dd0c200"
        send_sms(number, content)
    elif command.lower() == "/help" or command.lower() == "redeem" or command.lower() == "cashout" or command.lower() == "cash out":
        content = "Text 9512264826 for personal assistant"
        send_sms(number, content)
    else:
        content = "Start with create and username to create account!" + "\n" + "Example: Create Mark2021"
        send_sms(number, content)

    return "ok"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")