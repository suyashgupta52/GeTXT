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
        _db = MongoDB(var._db_client, var._db_name)
        _mts = MTS()                        
        
        for data in _db._sorted_find({"_translated_text_polarity": None}, var._tweet_limit, var._offset):
            text = data['__text']
            id = data['_id']
            var._debug and print(id ," Text: ", text)
            
            try:
                if len(text) <= var._min_text_len:
                    raise Exception("Small Text")
                _trans = _mts._translator(text, data['lang'])                
                var._debug and print("Translated Text: ", _trans[0])
                var._debug and print("Translated Polarity: ", _trans[1])
            except Exception as e:
                var._debug and print("Error: ", e)                
                print("Error for Id: ", id)
                _db._delete({"_id": id})                            
                continue
        
            _obj = {"$set": {"_translated_text": _trans[0], "_translated_text_polarity": _trans[1]}}
            var._debug and print("Updating: ", _obj)                        
            sleep(var._sleep_time_small) #small time                        
            _db._update({"_id": id}, _obj)
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