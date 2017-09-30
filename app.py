import sys
import feedparser

from colorama import init
from colorama import Back, Style
init(autoreset=True)

# print(Fore.RED + 'some red text')
# print('automatically back to default color again')


def latest():
    d = feedparser.parse(url)
    print (Back.RED + "Title:") + (Style.RESET_ALL + " " + d.entries[0].title)
    print (Back.YELLOW + "Link:") + (Style.RESET_ALL + " " + d.entries[0].link)


def latest_five():
    d = feedparser.parse(url)
    i = 0
    for i in range(0, 5):
        print (Back.CYAN + str(i + 1) + ")" + Style.RESET_ALL + " " +
               Back.RED + "Title:" +
               (Style.RESET_ALL + " " + d.entries[i].title))
        print (' '*(len(str(i+1))) + '  ' + Back.YELLOW + "Link:" +
               (Style.RESET_ALL + " " + d.entries[i].link))
        # print "Content: " + d.entries[i]['content']


def show(title, link, desc):
    print str(title)
    # print str(date)
    print str(link)
    print str(desc)


def menu():
    print "What do you wish to do now?"
    print "1. Access the most recent item from your feed"
    print "2. Access the 5 most recent items from your feed."
    opt = int(raw_input('Choice: '))
    if opt == 1:
        latest()
    elif opt == 2:
        latest_five()
    else:
        print "Not a valid choice"
        exit(0)


def check_args():
    if len(sys.argv) != 2:
        print "Usage: python app.py input_RSS_URL\n"
        exit(0)
    if not sys.argv[1].endswith('xml'):
        print 'Your URL should point to an XML file.'
        print 'Usage: python app.py input_RSS_URL\n'
        exit(0)


if __name__ == "__main__":
    check_args()
    url = sys.argv[1]
    menu()
