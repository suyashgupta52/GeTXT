try:
    import tweepy
    from tweepy import Stream
    from tweepy import OAuthHandler
    from tweepy.streaming import StreamListener
    from src.Database import MongoDB
    from src.DataCleaning import MTS
    from time import sleep    
    import var
    import json
except Exception as e:    
    exit("Exception: " + str(e))

# Listen to stream and return it
class StdOutListener(StreamListener):
    def __init__(self, _count):
        var._debug and print("Connecting Tweepy Stream...")
        super().__init__()
        self.__count = _count
        self.__max_tweets =  _count + var._tweet_max_count
        var._debug and print("Max: ", self.__max_tweets)
        self.__pre = MTS()
        self.__db = MongoDB(var._db_client, var._db_name)

    def on_connect(self):
        var._debug and print("Tweepy Stream Connection Success!!")
        pass
    
    def on_exception(self, exception):
        """Called when an unhandled exception occurs."""
        var._debug and print("Exception: ", exception)
        return True
    
    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        var._debug and print("Limit: ", track)
        return True
    
    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        var._debug and print("Error Code: ", status_code)
        return False

    def on_timeout(self):
        """Called when stream connection times out"""        
        var._debug and print("TimeOut!!")
        return True

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice
        Disconnect codes are listed here:
        https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/streaming-message-types
        """
        var._debug and print("Disconnect: ", notice)
        return True

    def on_data(self, _data):
        # Check Condition
        if(self.__count == self.__max_tweets):
            return False
        # Defining Local Var
        __text = ''
        __lang = 'hi'        
        
        # Scarpinh Data        
        try:
            raw_data = _data
            var._debug and print("Count: ", self.__count)
            try:
                data = json.loads(raw_data)            
                sleep(var._sleep_time_small) #small time
                __lang = data['lang']  
                __text = data['extended_tweet']['full_text']            
            except:
                __text = data['text']
                
            if len(__text) <= var._min_text_len:
                raise  Exception("Smaller Text!!")
            
            var._debug and print("Text: ", __text)            
            
            # Data Cleaning            
            
            var._debug and print("Text Cleaning...")            
            sleep(var._sleep_time_small) #small time                    
            _text = self.__pre._clean(__text)            
            
            
            var._debug and print("Text Demojis...")                        
            sleep(var._sleep_time_small) #small time                    
            _text = self.__pre._demojis(_text, True)            
            
            # var._debug and print("Text MTS...")                        
            # sleep(var._sleep_time_small) #small time                    
            # _translated_text = self.__pre._translator(_text, True)            
            # print(_translated_text)
            # print(_translated_text[0])
            
            # Object of data
            self.__count += 1
            var._debug and print("Document Count: ", self.__count)
            
            if len(_text) <= var._min_text_len:
                raise  Exception("Smaller Text!!")
            # , "_translated_text": _translated_text[0], "_translated_text_polarity": _translated_text[1]
            _obj = {"__text": _text, "lang": __lang, "_count": self.__count}
            var._debug and print("Inserting: ", _obj)                        
            sleep(var._sleep_time_small) #small time            
            self.__db._insert(_obj)            
        except Exception as e:
            var._debug and print("Exception: ",{e})            

        var._debug and print("Iteration Count: ", self.__count)
        return True        

# Fetch Tweets from Tweepy
class Tweepy(object):
    def __init__(self):
        # Variables that contain the user credentials to access Twitter API        
        self.__auth = OAuthHandler(var._consumer_key, var._consumer_secret)
        self.__auth.set_access_token(var._auth_token, var._auth_secret)               

    def _fetch(self, _track=["Call center Reviews", "New Product Review", "Product Complaints", "Customer Service Center","Customer HelpCenter", "Amazon Product Reviews", "Service Reviews", "Company’s Reputation", "Product Comment"]):
        var._debug and print("Connecting MongoDB...")                     
        _db = MongoDB(var._db_client, var._db_name)
        _count = _db._count()
        var._debug and print("Connecting Tweepy...")             
        sleep(var._sleep_time_small) #small time
        __stream = Stream(self.__auth, StdOutListener(_count))            
        __stream.filter(track=_track)
        sleep(var._sleep_time_small) #small time                    
        var._debug and print("Fetching"+ var._complete_msg)        