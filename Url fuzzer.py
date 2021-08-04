import requests
from requests import status_codes
url = input("Pls input the url you want to fuzz here:")
wordlists = input("input the path to wordlist here:")
slsh =  '/'
word = open(wordlists,"r")
line = word.readlines()

for a in line:
    b = a.rstrip('\n')
    r = requests.get(url+slsh+b)
    if r.status_code !=404:
        print(url+slsh+b+"--"+str(r.status_code),end="\n")
    




