from time import sleep
from os import system
from subprocess import call

sleepTime = int(input("What do yo want change your IP? just write number [1,3600]: "))


def enable():
    system("systemctl enable tor.service")


def changeIP():
    while True:
        system("systemctl restart tor.service")
        # system('echo "IP: $(curl --socks5-hostname localhost:9050 https://api.ipify.org; echo)"')
        # system(
        #     'echo "IP : $(curl --socks5-hostname localhost:9050 https://api.ipify.org; echo)"'
        # )
        system('echo "IP : $(torsocks wget -qO - https://api.ipify.org; echo)"')
        sleep(sleepTime)


def main():
    changeIP()


main()
