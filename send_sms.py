import os
from twilio.rest import Client

def send_sms(phone_number, content):

    account_sid = "AC575b69ac8f724dc34ssc3ca8861587ccca"
    auth_token = "c0e91528d69026188c5ss0f7e5c0e66424"

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=content,
                        from_='+12243750856',
                        to=phone_number
                    )

# if __name__ == '__main__':
#     send_sms("+14705339352"‬, "test")