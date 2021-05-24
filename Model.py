import key
import threading
from time import sleep
from src.Database import MongoDB
from src.SentimentAnalysis import SentimentAnalysis
from src.Translate import MTS
# Model class


class OpinionMining(object):
    # init method
    def __init__(self):
        self.count = 0
        print("Model Loading...")

    def _run_heroku(self,  _obj=None):
        print("Heroku Running...")
        # db instance
        self.__db = MongoDB(key._db_name, key._db_document)
        # self._db = db.MongoDB(key._db_name, key._db_result)
        # Sentiment Score Instance
        self.sa = SentimentAnalysis()
        # Translator Instance
        self.trans_module = MTS()
        # Data Loop
        threads = []        
        for data in self.__db._sorted_find(_obj, key._tweet_limit):
            try:
                thread = threading.Thread(None, target=self.__middleware, args=(
                    data['tweet'], data['lang'], data['_id'],))
                thread.start()
                threads.append(thread)
                if len(threads) == 10:
                    for thread in threads:
                        thread.join()
                    threads = []
            except:
                print("Error here => ", e)
                sleep(30)
                continue
        print("Threads Running: ", threading.enumerate())

        for thread in threads:
            print("Active Thread Left => ", threading.active_count())
            thread.join()
        self.__db.__del__()
        # self._db.__del__()

        print("Active Thread => ", threading.active_count())

        print("Heroku Ends!!")
        sleep(key._sleep_time)
        print(threading.current_thread())
        self._run_heroku(_obj)

   