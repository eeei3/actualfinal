import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


class SpiderMain:

    limit_count = 0

    def __init__(self, folder_name, base_link, threads, external, max, maxnum, limit_count):

        self.FOLDER_NAME = folder_name
        self.BASE_LINK = base_link
        self.DOMAIN_NAME = get_domain_name(base_link)
        self.THREADS = threads
        self.EXTERNAL = external
        self.MAX = max
        self.MAXNUM = maxnum
        self.QUEUE_FILE = folder_name + '/queue.txt'
        self.CRAWLED_FILE = folder_name + '/crawled.txt'
        self.queue = Queue()
        self.limit_count = limit_count
        Spider(folder_name, base_link, self.DOMAIN_NAME, max, maxnum, external, 0)

    def create_threads(self):
        try:
            for _ in range(self.THREADS):
                t = threading.Thread(target=self.work)
                t.daemon = True
                t.start()
        except Exception as e:
            print(e)

    def work(self):
        while True:
            url = self.queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            self.queue.task_done()

    def create_jobs(self):
        for link in file_to_set(self.QUEUE_FILE):
            self.queue.put(link)
        self.queue.join()
        self.crawl()

    def crawl(self):
        queued_links = file_to_set(self.QUEUE_FILE)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + " links in the queue")
            self.create_jobs()

    def kick_start(self):
        self.create_threads()
        self.crawl()
