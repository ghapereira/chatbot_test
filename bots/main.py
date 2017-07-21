import requests
import json

def send_command(command):
    my_url = 'https://msging.net/commands'
    my_username = ''
    my_key = 'Key Z2h0ZXN0Ym90OnFHa1dkemNrbG1JaFBXZkh5dVpl'
    r = requests.post(my_url, auth=(my_username, my_key))


