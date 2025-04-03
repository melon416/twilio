from flask import Flask, render_template, request
from main import Bot
from send_sms import send_sms

app = Flask(__name__)


@app.route('/create_account', methods=["POST", "GET"])
def start():
    data = request.json
    # attempted_username = request.form['username']
    # attempted_password = reques.form['password']
    print("okok", request.json)
    
    username = data['urname']
    phone_number = data['phone_number']
    print("here", username, phone_number)
    bot = Bot()
    res = bot.main(username)
    if res == "success":
        print("successsss")
        # resp = MessagingResponse()
        # resp.message("Account has been successfully created. Password:123123")

        content = "Account has been successfully created. Password:123123" + "\n" + "Text the word <load> to add Firekirin Credits"
        send_sms(phone_number, content)
        print("message sent")
    elif res == "exist":
        content = "Username already exists. Please use another!"
        send_sms(phone_number, content)
    else:
        print("failll")
        content = "Sth went wrong. Please try it again!"
        send_sms(phone_number, content)


    return 'YUP you got it!'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)