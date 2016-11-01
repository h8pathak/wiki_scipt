import requests
from bs4 import BeautifulSoup
import re


def find_sentence(wiki_text):

    print ("Enter the citation no:")
    n = input()
    
    result = re.search(r'([^].!?\[]+[.!?]?)\[' + n + ']', wiki_text.strip()).group(1)
    print (result)

def find_citation(wiki_text):

    print ("Enter the sentence to find its citation number:")
    sentence = input()

    n = wiki_text[wiki_text.find(sentence)+len(sentence)+1]
    print(n)
  

if __name__ ==  "__main__":

    print ("Enter the url of the Wikipedia article:")
    url = input()
    #url = "https://en.wikipedia.org/wiki/Bermuda_Triangle"

    print ("Fetching the data in url...")
    try:
        source_code = requests.get(url)
    except:
        print ("Internet Error")
    
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    wiki_text = ""
    for link in soup.findAll('p'):
        wiki_text += link.text

    print ("What do you want to do?")
    print("""Enter \n1. Get the sentence with a citation number\n2. Get the citation number of a sentence:""")

    option = int(input())

    if option == 1:
        find_sentence(wiki_text)
    elif option == 2:
        find_citation(wiki_text)
    else:
        print ("Invalid Entry")
