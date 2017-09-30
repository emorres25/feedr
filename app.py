import sys
import feedparser
import colorama

from colorama import init
from colorama import Back, Style, Fore
init(autoreset=True)

#Pages Used for Tests
#http://feeds.foxnews.com/foxnews/latest
#http://rss.cnn.com/rss/edition.rss

def latest(quant, opt):
    d = feedparser.parse(url)
    for i in range(0, quant):
        print("\n" + Fore.BLUE + str(i+1))
        title = d.entries[i].title
        date = d.entries[i].published if 'published' in d.entries[i] else ""
        link = d.entries[i].link
        desc = d.entries[i].description if 'description' in d.entries[i] else ""
        show(title, date, link, desc, opt)

#If don't have date or description, it won't generate a error
def show(title, date, link, desc, flag):
    print (Fore.BLUE + "Title: " + Style.RESET_ALL + Fore.GREEN + str(title.encode('utf-8')))
    print (Fore.BLUE + "Date: " + Style.RESET_ALL + Fore.GREEN + str(date.encode('utf-8')))
    print (Fore.BLUE + "Link: " + Style.RESET_ALL + Fore.GREEN + str(link.encode('utf-8')))
    if flag == 1:
        print (Fore.BLUE + "Description: " + Style.RESET_ALL + Fore.GREEN + str(desc.encode('utf-8')))

def menu():
    print("What do you wish to do now?")
    print("1. Read the latest issue.")
    print("2. Get the title of the latest 5 issues.")
    opt = int(raw_input('Option: '))
    if opt == 1:
        latest(1 , opt)
    elif opt == 2:
        latest(5 , opt)
    else:
        print("Not a valid choice")
        exit(0)

if __name__ == "__main__":
    url = sys.argv[1]
    menu()
