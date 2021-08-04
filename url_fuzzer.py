import requests
from requests import status_codes
import time
url = input("Pls input your url here:")
wordlists = input("input wordlist here:")
slsh =  '/'
word = open(wordlists,"r")
line = word.readlines()

for a in line:
    b = a.rstrip('\n')
    r = requests.get(url+slsh+b)
    if r.status_code !=404:
        print(url+slsh+b+"--"+str(r.status_code),end="\n")
 
## BY SahotaSkywalker




