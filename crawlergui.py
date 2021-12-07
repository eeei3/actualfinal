import os
import shutil
import threading
from spider import Spider
from queue import Queue
from domain import *
from general import *
from urllib.request import urlopen
from link_finder import LinkFinder
import winsound
import sys
from finishedwindowc import CrawlerFinished
from concurrent import futures

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=5)

class CrawlerGUI:

    othersite = ''
    threads = 8
    limit = 0
    timerun = 0
    config = [0, 1, 0]

    


    def __init__(self, othersite, threads, xtralinks, limiter, timerun, config):
        CrawlerGUI.othersite = othersite
        CrawlerGUI.threads = threads
        CrawlerGUI.xtralinks = xtralinks
        CrawlerGUI.limit = limit
        CrawlerGUI.timerun = timerun
        CrawlerGUI.config = config



        
    def Start():
        thread_pool_executor.submit(CrawlerGUI.crawlerGUI)
    def crawlerGUI():           
        f = open("testfile.rac", "r")
        a = open("webfile.rac", "r")
        weblink = a.read()
                

        crawlerthreads = CrawlerGUI.threads.get()
        crawlerextras = CrawlerGUI.xtralinks.get()
        ignore = CrawlerGUI.ignorevar.get()
        spiderlimits = CrawlerGUI.limit.get()
        totalthreads = int(crawlerthreads)

        if spiderlimits == 0:
            spiderlimits = 99999999
        else:
            pass
            
        
        try:
            shutil.rmtree("projectele")
        except Exception as e:
            os.makedirs('projectele')
        g = open("limitfile.rac", "r")
        PROJECT_NAME = 'projectele'
        HOMEPAGE = weblink
        NUMBER_OF_THREADS = totalthreads
        print (NUMBER_OF_THREADS)
        DOMAIN_NAME = get_domain_name(HOMEPAGE)
        SPIDERLIMITS = spiderlimits
        print(SPIDERLIMITS)
        CHECKER = False
        LIMITER = 0
        IGNORE = ignore
        REASON = ''
        QUEUE_FILE = PROJECT_NAME + '/queue.txt'
        CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
        queue = Queue()
        try:
            Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, SPIDERLIMITS, CHECKER, LIMITER, IGNORE, REASON)
        except Exception as e:
            print(e)


        def create_workers():
            try:
                for _ in range(NUMBER_OF_THREADS):
                    t = threading.Thread(target=work)
                    t.daemon = True
                    t.start()
            except Exception as e:
                    print (e)


        def work():
            while True:
                url = queue.get()
                Spider.crawl_page(threading.current_thread().name, url)
                queue.task_done()


        def create_jobs():
            for link in file_to_set(QUEUE_FILE):
                queue.put(link)
                queue.join()
                crawl()

        def crawl():
            queued_links = file_to_set(QUEUE_FILE)
            if len(queued_links) > 0:
                print(str(len(queued_links)) + " links in the queue")
                create_jobs()
            else:
                if CrawlerGUI.timerun == 0:
                    try:
                        CrawlerGUI.completedgui(audiosetting = CrawlerGUI.config[2])
                    except Exception as e:
                        print(e)
                    CrawlerGUI.timerun = CrawlerGUI.timerun + 1
                else:
                    pass
        create_workers()
        crawl()



