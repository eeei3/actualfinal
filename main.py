import json
import os
from spider import SentenceSpider, KeywordSpider
from queue import Queue


class Main:
    def __init__(self):
        self.browsers = []
        self.threadmax = 0
        self.pagemax = 0
        self.citestyle = ""
        self.skeywords = []
        self.ssentence = ""


    def startup(self):
        try:
            with open("config.json", "r") as configfile:
                settings = json.loads(configfile.read())
            self.browsers = settings["browsers"]
            self.threadmax = settings["threadmax"]
            self.pagemax = settings["pagemax"]
            self.citestyle = settings["citestyle"]
            os.makedirs("results")
            queue = os.path.join("results", "queue.txt")
            pages = os.path.join("results", "pages.txt")
            with open(queue, "x") as file:
                file.write("")
            with open(pages, "x") as file:
                file.write("")

        except:
            with open("config.json", "x") as configfile:
                settings = {
                    "browsers":["google", "duckduckgo"],
                    "threadmax":8,
                    "pagemax":50,
                    "citestyle":"MLA"
                }
                dump = json.dumps(settings)
                configfile.write(dump)
                self.browsers = settings["browsers"]
                self.threadmax = settings["threadmax"]
                self.pagemax = settings["pagemax"]
                self.citestyle = settings["citestyle"]

    def keywords(self, keyword):
        self.skeywords = keyword.split(",")
        for keyword in self.skeywords:
            return

        return 0

    def sentence(self, ssentance):
        FOLDER_NAME = "user-search"
        queue = Queue()
        SentenceSpider(self.ssentence, self.browsers)
        return 0

    def start(self):
        self.startup()
        print("Search by keyword or by sentence?")

        choice = input(":\t").lower

        if choice == "keyword":
            print("What are your keywords? (Seperate them with commas)")

            keyword = input(":\t")
            self.keywords(keyword)

        elif choice == "sentence":
            print("What is your sentence?")

            ssentance = input(":\t")
            self.sentence(ssentance)


main = Main()
main.start()
