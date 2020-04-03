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
print("Redirect URL is", redirect_url)
client = OAuthZoomClient(client_id, client_secret, redirect_url, browser_path)

user_response = client.user.get(id='me')
user = json.loads(user_response.content)
print(user)
print('\n')

# ids below are used for test
test_channel_id = "109ab13498c64fd5911a42be1076ea6b"
my_channel_id = "e00a1405fc5a4dc0980fa3c6dfed5989"
yl_channel_id = "c1e85cd0e22844baaaa9cb2bf55f7704"
yl_member_id = "s4fjawkhrtcwcpvxbhxtqw"
flag = True

while flag:
    print("Please test the functions following this sequence: 1-2-3-4-6-7-8-9-5-0")
    print("---Options---")
    print("1. list channel numbers")
    print("2. creat a channel")
    print("3. get a channel")
    print("4. update a channel")
    print("5. delete a channel")
    print("6. invite a member to a channel")
    print("7. remove a member from a channel")
    print("8. join to a channel")
    print("9. leave from a channel")
    print("0. exit")
    option = input("Enter a option number:")
    if option == "1":
        channel_id = input("input channel id(use 'e00a1405fc5a4dc0980fa3c6dfed5989' for test):")
        response = json.loads(client.chat_channels.list_members(channelId=my_channel_id).content)
        print(response)
    elif option == "2":
        channel_name = input("input channel name:")
        email = input("input members' emails(separate with comma):")
        email = email.split(",")
        tmp = []
        for e in email:
            tmp.append({"email": e})
        response = json.loads(client.chat_channels.create(name=channel_name, type=1, members=tmp).content)
        print(response)
    elif option == "3":
        channel_id = input("input channel id(use 'e00a1405fc5a4dc0980fa3c6dfed5989' for test):")
        response = json.loads(client.chat_channels.get(channelId=channel_id).content)
        print(response)
    elif option == "4":
        channel_id = input("input channel id(use 'e00a1405fc5a4dc0980fa3c6dfed5989' for test):")
        new_name = input("input a new name for channel:")
        response = client.chat_channels.update(channelId=channel_id, name=new_name)
        print("update status code: " + str(response.status_code))
    elif option == "5":
        channel_id = input("input channel id(use 'e00a1405fc5a4dc0980fa3c6dfed5989' for test):")
        response = client.chat_channels.delete(channelId=channel_id)
        print("delete status code: " + str(response.status_code))
    elif option == "6":
        channel_id = input("input channel id(use 'e00a1405fc5a4dc0980fa3c6dfed5989' for test):")
        email = input("input members' emails(use 'tjuwangyilin@163.com' for test):")
        email = email.split(",")
        tmp = []
        for e in email:
            tmp.append({"email": e})
        response = json.loads(client.chat_channels.invite(channelId=channel_id, members=tmp).content)
        print(response)
    elif option == "7":
        channel_id = input("input channel id(use 'e00a1405fc5a4dc0980fa3c6dfed5989' for test):")
        member_id = input("input member id(use 's4fjawkhrtcwcpvxbhxtqw' for test):")
        response = client.chat_channels.remove(channelId=channel_id, memberId=member_id)
        print("remove status code: " + str(response.status_code))
    elif option == "8":
        channel_id = input("input channel id(use 'c1e85cd0e22844baaaa9cb2bf55f7704' for test):")
        response = json.loads(client.chat_channels.join(channelId=channel_id).content)
        print(response)
    elif option == "9":
        channel_id = input("input channel id(use 'c1e85cd0e22844baaaa9cb2bf55f7704' for test):")
        response = client.chat_channels.leave(channelId=yl_channel_id)
        print("leave status code: " + str(response.status_code))
    else:
        flag = False
