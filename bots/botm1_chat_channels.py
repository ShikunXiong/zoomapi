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
print('---')

# ids below are used for test
test_channel_id = "109ab13498c64fd5911a42be1076ea6b"
my_channel_id = "e00a1405fc5a4dc0980fa3c6dfed5989"
yl_channel_id = "c1e85cd0e22844baaaa9cb2bf55f7704"
yl_member_id = "s4fjawkhrtcwcpvxbhxtqw"

# list channel members
response = json.loads(client.chat_channels.list_members(channelId=my_channel_id).content)
print("--list channel members--")
print(response)

# create a channel
response = json.loads(
    client.chat_channels.create(name="create_test", type=1, members=[{"email": "aa@gmail.com"}]).content)
print("--create a channel--")
print(response)

# get a channel
client.chat_channels.get(channelId=test_channel_id)
response = json.loads(client.chat_channels.get(channelId=test_channel_id).content)
print("--get a channel--")
print(response)

# update a channel
response = client.chat_channels.update(channelId=my_channel_id, name="new_name")
print("update status code: " + str(response.status_code))

# delete channel
# response = json.loads(client.chat_channels.delete(channelId=test_channel_id).content)
# print(response)

# invite
response = json.loads(
    client.chat_channels.invite(channelId=my_channel_id, members=[{"email": "tjuwangyilin@163.com"}]).content)
print("--invite response--")
print(response)

# remove
response = client.chat_channels.remove(channelId=my_channel_id, memberId=yl_member_id)
print("remove status code: " + str(response.status_code))

# join
response = json.loads(client.chat_channels.join(channelId=yl_channel_id).content)
print("--join a channel--")
print(response)

# leave
response = client.chat_channels.leave(channelId=yl_channel_id)
print("leave status code: " + str(response.status_code))
