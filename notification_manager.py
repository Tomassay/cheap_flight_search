import os
from twilio.rest import Client


account_sid = 'ACbd9813b45569690fde904d382b0a9f20'
auth_token = 'd5ad31f0b570896a764eed751ef94d40'
my_phone = 'YOURNUMBER'
virtual_twilio = 'YOURVIRTUALNUMBER'


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages \
                        .create(
                             body=message,
                             from_= virtual_twilio,
                             to= my_phone
                         )

        print(message.sid)