#!/usr/bin/env python3

import sys
import os
import requests
from rich.console import Console
from rich.table import Table

from config import SERVER_URL

console = Console()

image ="""                                                                                                                                                                                         
               .                                                                                                                                                                                        
             ~PBJ.                                                                                                                                                                                      
            ?#&&&G~                                                                                                                                                                                     
          .5&&###&#!                .:^^^:.                                                                                                                                                             
          Y&#&&&&#&#~            ^JYYJ???JYY?^                                                                                        :^                                                                
         ~###B5YP##&G.         :55!.       :7PY.                                                                                      YG                                                                
         ?&&B^   7&##^        ^B?             5G.       :!7777~.         .~!777!^      .!..~!777^   .~777!^          .~7777!:      .!!PB!!!:       :!777!~.       :! .~!7!   ^~ :~777!:   ^!777!:       
         ?&##J^:~5&##^       .GY              .!:     !5Y7~^^~?5J:      ?P?~^^^!Y5^    ^#JJ7~^^!YP^?J!~^^!YP^      :Y5?~^^~7Y5~    .~~5B~~~:     !5Y7~^^!?5J:     !#?Y7~~^   JB?J!^^~7PY^Y?~^^~7PY.     
         !&##&##&&###:       ~#^                     JG^        ?B^    !&:       !!    :#Y       ?&?       YG     ~B?        ~GJ      YG        JP^        ?G^    !&?        ?&!      .GB^      .B?     
         ^#########&B.       !#:                    !#:          JG.   :GY^.           :#~       ~#^       !#:   .B?          ^#!     YG       !#:          5G    !#:        ?G        YP        P5     
         .G&#######&P        ^#~                    YG           ^#^    .!JYJJ?7~.     :#~       ~#^       !#:   ^#^           GY     YG       YBJJJJJJJJJJ?Y5.   !#:        ?G        YP        P5     
       .7.5&#######&Y:7.      YP              ^5^   ?B.          !#:        .:^~?P?    :#~       ~#^       !#:   :#!          .B?     YG       ?B.                !#:        ?G        YP        P5     
      !B&~?&#######&7!&B7     .5P^           ~GJ    .GY         ^B?    ~^        7&:   :#~       ~#^       !#:    JG:         YG.     YG       .GJ          :     !#:        ?G        YP        P5     
      J&&J^&&&&&&&&&^J&&?       7PY!^.. ..^755~      .55!:.  .^?P7     7G7:.  .:!PJ    :&~       ~&^       !#:     7P?^.  .:!5Y.      !B!...    :55!:.  .:!5Y.    !#:        JB        YG        P5     
      ~#B?.JGGBBBGGJ.7P#~         ^7JJJJJJJ7^          ^?JJJJJJ!.       :?JJJJJJ?^     :Y:       ^Y:       ^Y.      .!JJJJJJ7^         ^JJJJ.     ^7JJJJJJ?^      ^Y.        !J        7?        ??     
       :.   7JJJJ??    .                                                                                                                                                                                
            :J7~!Y^                                                                                                                                                                                     
            ~B:  P?                                                                                                                                                                                     
            ~G! ~G7                                                                                                                                                                                     
             :J5Y^                                                                                                                                                                                                                                                                                                                                                                                      

"""

def log_in(user_name: str, user_token: str) -> str:
    
    
    server_response = requests.get(
        f'{SERVER_URL}/log_in/{user_name}/{user_token}')
    status = server_response.status_code

    if status == 200:

        if server_response.content == b'true':
            try:
                os.system('cls')
            except:
                os.system('clear')

            console.print("                                                Welcome", style="green")
            table = Table(title="")
            table.add_column("Menu", justify="right", style="cyan", no_wrap=True)
            table.add_column("                                                                                                                       ", style="magenta")

            table.add_row("Account")
            table.add_row("")
            table.add_row("Wall")
            table.add_row("")
            table.add_row("Settings" )
            table.add_row("")
            table.add_row("Exit")
            table.add_row("")
            table.add_row("")
            table.add_row("")
            table.add_row("")

            console.print(table)

            command = input('Press any buttons...')
                    

            

        else:
            print('There is no account with this username/usertoken!')

    else:
        print('Check if you are connected to the network/ if the server is available on the official website')
        print(f'Request status {status}')




try:
    os.system('mode con: cols=200 lines=40')
    print(image)
    print('Hello!')
    name = str(input('Enter your account name '))
    token = str(input('Enter your account token: '))
    # name = str(sys.argv[1])
    # token = str(sys.argv[2])
    log_in(name, token)
    


except Exception as err:
    print(f"{err}\nYou must enter correctly: <username> <usertoken>")