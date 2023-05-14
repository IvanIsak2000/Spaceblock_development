import socket
import os 

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


def client_program():

    os.system('mode con: cols=200 lines=40')
    print(image)
    host = input('Enter a IP: ')

    your_host = socket.gethostname()
    your_host=socket.gethostbyname(your_host)
    print(your_host)  
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()