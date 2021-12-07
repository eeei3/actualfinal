import os
from os import system
import json
from main import SpiderMain


class Main:

    def __init__(self, directory):
        self.directory = directory
        self.queue = os.path.join(directory, "queue.txt")
        self.crawled = os.path.join(directory, "crawled.txt")
        self.settingsdir = os.path.join(directory, "configs.json")
        self.configs = {
            "threads" : 8,
            "outside_sites" : False,
            "max_links" : [False, 0]
        }
        if not os.path.exists(directory):
            os.mkdir(directory)
            with open(self.queue, 'x') as f:
                f.close()
            with open(self.crawled, 'x') as f:
                f.close()
            with open(self.settingsdir, 'x') as f:
                f.write(json.dumps(self.configs))
                f.close()
        else:
            with open(self.crawled, 'w') as f:
                f.write("")
                f.close()
            with open(self.settingsdir, 'r') as f:
                self.configs = json.loads(f.read())

    @staticmethod
    def clear_screen():
        _ = system('cls')

    # /***************************************************************************************
    #  Function that calls the crawler
    # ***************************************************************************************\
    def start(self):
        url = input("Url to crawl:")
        spidermain = SpiderMain(
            self.directory, url,
            self.configs["threads"],
            self.configs["outside_sites"],
            self.configs["max_links"][0],
            self.configs["max_links"][1], 0)
        spidermain.kick_start()

    # /***************************************************************************************
    #  Main function (Gets user input)
    # ***************************************************************************************\
    def main(self):
        print("Please input your choice.\nChoices\n-------------------\n1.Start crawling\n2.Change Settings\n3.Exit")
        choice = input("")
        choice = choice.lower()
        if choice == "1" or choice == "start":
            self.start()
        elif choice == "2" or choice == "settings":
            self.settings()
        elif choice == "3" or choice == "exit":
            quit()
        else:
            pass

    def settings(self):
        main.clear_screen()
        print("Which element do you want to change?\n1.Threads\n2.Crawl outside sides\n3.Max amount to crawl")
        setting_to_change = input("Type in the number\n")
        if setting_to_change == "1":
            print("How many threads do you want?")
            print("Current amount of threads: " + str(self.configs["threads"]) + "\n")
            self.configs["threads"] = int(input(""))

        elif setting_to_change == "2":
            print("Do you want the spider to crawl external sides?")
            print("Enter 'yes' or 'no'\n")
            temp = input()
            temp = temp.lower()
            if temp == "yes":
                self.configs["outside_sites"] = True
            elif temp == "no":
                self.configs["outside_sites"] = False

        elif setting_to_change == "3":
            print("Do you want a limit to the amount of pages crawled?")
            print("Enter 'yes' or 'no'\n")
            temp = input()
            temp = temp.lower()
            if temp == "yes":
                self.configs["max_links"][0] = True
                print("What do you want the limit to be?\n")
                temp = int(input())
                self.configs["max_links"][1] = temp
            elif temp == "no":
                self.configs["max_links"][0] = False
        else:
            main.clear_screen()
            print("I didn't understand that")
            self.settings()

        with open(self.settingsdir, 'w') as f:
            f.write(json.dumps(self.configs))
            f.close()
        main.clear_screen()
        self.main()


main = Main("results")
main.main()