import sys, os
filename = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(1, filename)
from zoomapi import OAuthZoomClient

import json
from configparser import ConfigParser
from pyngrok import ngrok

parser = ConfigParser()
parser.read("bot.ini")
client_id = parser.get("OAuth", "client_id")
client_secret = parser.get("OAuth", "client_secret")
browser_path = parser.get("OAuth", "browser_path")
print(f'id: {client_id} secret: {client_secret} browser: {browser_path}')

redirect_url = ngrok.connect(4000, "http")
# redirect_url = "http://52416004.ngrok.io"
print("Redirect URL is", redirect_url)

client = OAuthZoomClient(client_id, client_secret, redirect_url, browser_path)

user_response = client.user.get(id='me')
user = json.loads(user_response.content)
print(user)
print('---')
cid = "c1e85cd0e22844baaaa9cb2bf55f7704"
stop = False
while not stop:
    print("----------------Options:------------------")
    print("1. Send a Message")
    print("2. Delete Most Recent Message")
    print("3. Update Most Recent message")
    print("4. List All Messages")

    option = input("Enter options")
    if option == '1':
        message = input("Enter message: ")
        print(type(message))
        print(client.chat_messages.post(to_channel=cid, message=message))
        if message == "stop":
            stop = True
    elif option == '2':
        posts = client.chat_messages.list(user_id="me", to_channel=cid)
        print("-------------Printing Existing Messages--------------")
        ids = [message.get("id") for message in posts.json().get("messages")]
        messages = [message.get("message") for message in posts.json().get("messages")]
        print(ids)
        print(messages)
        print("-------------Deleting Last Message--------------")
        client.chat_messages.delete(messageId=ids[0], to_channel=cid)
        print("Completed!")
        print("-------------Printing Remaining Message--------------")
        posts = client.chat_messages.list(user_id="me", to_channel=cid)
        messages = [message.get("message") for message in posts.json().get("messages")]
        print(messages)
        print("-------------OVER--------------")
    elif option == '3':
        posts = client.chat_messages.list(user_id="me", to_channel=cid)
        ids = [message.get("id") for message in posts.json().get("messages")]
        newMessage = "I'm your new message!"
        client.chat_messages.update(ids[0], to_channel=cid, message=newMessage)
        i = 0
    elif option == '4':
        posts = client.chat_messages.list(user_id="me", to_channel=cid)
        ids = [message.get("id") for message in posts.json().get("messages")]
        messages = [message.get("message") for message in posts.json().get("messages")]
        print(ids)
        print(messages)
    else:
        print("Come on, man. You are better than this.")
