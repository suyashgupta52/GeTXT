try:    
    from src.Database import MongoDB
    from src.DataCleaning import MTS
    from src.Tweets import Tweepy
    from time import sleep    
    import var    
except Exception as e:
    exit("Exception: " + str(e))


class DataCleaning(object):
    # init method
    def __init__(self):        
        var._debug and print("Data Cleaning"+ var._init_msg)          

    def _cleaning(self):
        _db = MongoDB(var._db_name, var._db_client)                        
        _mts = MTS()                
        for data in _db._sorted_find({"_translated_text_polarity": None}, var._tweet_limit):
            text = data['__text']
            var._debug and print("Text: ", text)
            
            if len(text) <= var._min_text_len:
                var._debug and print("Small Text")
                _err = True
                
            try:
                _trans = _mts._translate(text, data['lang'])                
                var._debug and print("Translated Text: ", _trans[0])
                var._debug and print("Translated Polarity: ", _trans[1])
            except:
                var._debug and print("MTS Error!!")
                _err = True

            id = data['_id']
            if _err == True:
                # delete doc                
                print("Error for Id: ", id)
                self.__db._delete({"_id": id})                            
                continue
        
            _obj = {"_translated_text": _trans[0], "_translated_text_polarity": _trans[1]}
            var._debug and print("Updating: ", _obj)                        
            sleep(var._sleep_time_small) #small time                        
            self.__db._update({"_id": id}, _obj)
        var._debug and print("Data Claning" + var._complete_msg)
    
    def __del__(self):
        var._debug and print("Data Cleaning"+ var._complete_msg)


class DataCollection(object):
    # init method
    def __init__(self):
        var._debug and print("Data Collection"+ var._init_msg)          
    
    def _collect(self, _fetch_query = None):
        var._debug and print("Data Collecting!!")
        sleep(var._sleep_time_small) #small time                        
        tweepy = Tweepy()
        tweepy._fetch(_fetch_query)
        sleep(var._sleep_time_small) #small time                        
        var._debug and print("Data Collecting" + var._complete_msg)
        
    def __del__(self):
        var._debug and print("Data Collection"+ var._complete_msg)