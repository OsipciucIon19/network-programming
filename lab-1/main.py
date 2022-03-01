from OpenThroughSocket import OpenThroughSocket
from DownloadImages import DownloadImages


def choose_option(x):
    global host
    global port
    if x == 1:
        host = "me.utm.md"
        port = 80
    elif x == 2:
        host = "utm.md"
        port = 443
    else:
        print("Non-existent option")
        global option
        option = int(input("Enter the number of option: \n"))
        choose_option(option)


option = None
host = ""
port = 0

import os

print(os.path.join(os.getcwd(), "images"))

if __name__ == '__main__':
    print("1) me.utm.md : 80")
    print("2) utm.md    : 443")
    option = int(input("Enter your option: (1/2) \n"))

    choose_option(option)
    list_of_links = OpenThroughSocket(host, int(port)).get_links()
    print(list_of_links)
    DownloadImages(list_of_links, host, int(port)).start_multi_threading()
