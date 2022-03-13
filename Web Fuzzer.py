
from pyfiglet import Figlet
custom_fig = Figlet(font='ivrit')
print(custom_fig.renderText('WEB FUZZER'))
def startmassage():
    print("#"+"*"*77+"#")
    print("| Name app : Web Fuzzer|")
    print("#"+"*"*77+"#")
    print("\n")
startmassage()


import requests

def load_dict():
    with open("dict.txt", "r") as dict_file:
        return dict_file.readlines()
wordlist = load_dict()
target = input("INGRESE PAGINA WEB: ") 

for word in wordlist:
    response = requests.get(target  + word.strip())
    if response.status_code in [200,301,302]:
        print("Encontrado: %s - %s" % (target + word.strip(), response.status_code))
