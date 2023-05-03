#!/usr/bin/env python3

import sys
import os
import requests

from config import SERVER_URL


def log_in(user_name: str, user_token: str) -> str:

    server_response = requests.get(
        f'{SERVER_URL}/log_in/{user_name}/{user_token}')
    status = response.status_code

    if status == 200:

        if response.content == b'true':
            try:
                os.system('cls')
            except:
                os.system('clear')
            print('Welcome!')

        else:
            print('There is no account with this username/usertoken!')

    else:
        print('Check if you are connected to the network/ if the server is available on the official website')
        print(f'Request status {status}')


try:
    name = str(sys.argv[1])
    token = str(sys.argv[2])

    log_in(name, token)


except Exception as err:
    print(f"{err}\nYou must enter correctly: <username> <usertoken>")
