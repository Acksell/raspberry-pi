import requests

from credentials import TOKEN, CLIENT_ID, channel

HEADER = {"Authorization":"Bot {}".format(TOKEN)}
BASE_URL = "https://discordapp.com/api/"

def post_message(msg="Det är mat nu!"):
	url = "{}channels/{}/messages".format(BASE_URL, channel)
	data = {"content":msg}
	return requests.post(url, data=data, headers=HEADER)

