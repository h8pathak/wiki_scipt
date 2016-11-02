import requests
from bs4 import BeautifulSoup
import re


def find_sentence(wiki_text):

    print ("Enter the citation no:")
    n = input()
    lis = []

    while 1:
    
        match = re.search(r'([^].!?\[]+[.!?]?)\[' + n + ']', wiki_text.strip())
        if match:
            result = match.group(1)
        else:
            break

        if result not in lis:
            lis.append(result)

        pos = wiki_text.find(result)
        new_start = pos + len(result)

        wiki_text = wiki_text[new_start:]
        
    print ("Result:")
    for l in lis:
        print (l)

def find_citation(wiki_text):

    print ("Enter the sentence to find its citation number:")
    sentence = input()

    pos = wiki_text.find(sentence)+len(sentence)+1
    lis = []
    
    while 1 :
        
        result = ""
        result += wiki_text[pos]
        while 1:
              pos += 1
              try:
                  temp = int(wiki_text[pos])
                  result += str(temp)
              except:
                  break
                        
        lis.append(result)

        pos += 2
        
        try:
            temp = int(wiki_text[pos])
        except:
            break

    print ("Result:")
    for l in lis:
        print (l)

        


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

    c='y'
    while c=='y':

        print ("What do you want to do?")
        print("""Enter \n1. Get the sentence with a citation number\n2. Get the citation number of a sentence:""")

        option = int(input())

        if option == 1:
            find_sentence(wiki_text)
        elif option == 2:
            find_citation(wiki_text)
        else:
            print ("Invalid Entry")

        print ("Wanna enter more (y/n):")
        c = input()
