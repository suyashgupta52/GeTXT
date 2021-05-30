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
        var._debug and print("Data Cleaning" + var._init_msg)
        self._db = MongoDB(var._db_client, var._db_name)
        self.__count = 1

    def _remove_duplicates(self):
        res = self._db._aggregate([
            {'$group': {'_id': {'_translated_text': "$_translated_text"}, 'uniqueIds': {'$addToSet': "$_id"}, 'count': {'$sum': 1}}}, {'$match': {'count': {'$gte': 2}}}, {'$sort': {'count': -1}}, {'$limit': int(var._tweet_limit)}])
        for _res in res:
            _left_one = True
            for _id in _res['uniqueIds']:
                if _left_one:
                    _left_one = False
                    var._active_print and print("Saved Id: ", _id)
                    continue
                # Remove rest
                self._db._delete({"_id": _id})
                sleep(var._sleep_time_small)  # small time
                var._active_print and print("Removing Id: ", _id)
            sleep(var._sleep_time_small)  # small time
            var._active_print and print(
                "Text: ", _res['_id']['_translated_text'])
        var._active_print and print("Removing Done!!")

    def _cleaning(self, _obj):
        _mts = MTS()

        _total = int(self._db._count())
        var._active_print and print("Total Count: ", _total)
        _unprocessed = int(self._db._count(
            {"_translated_text_polarity": None}))
        var._active_print and print("Unprocessed Count: ", _unprocessed)
        self.__count = _total - _unprocessed
        var._active_print and print("Processed Count: ", self.__count)

        for data in self._db._sorted_find(_obj, var._tweet_limit, var._offset):
            text = data['__text']
            id = data['_id']
            var._debug and print(id, " Text: ", text)

            try:
                if len(text) <= var._min_text_len:
                    raise Exception("Small Text")
                _trans = _mts._translator(text, data['lang'])
                var._debug and print("Translated Text: ", _trans[0])
                var._debug and print("Translated Polarity: ", _trans[1])
            except Exception as e:
                var._debug and print("Error: ", e)
                print("Error for Id: ", id)
                self._db._delete({"_id": id})
                continue

            _obj = {"$set": {
                "_translated_text": _trans[0], "_translated_text_polarity": _trans[1], "__count": self.__count}}
            var._debug and print("Updating: ", _obj)
            sleep(var._sleep_time_small)  # small time
            self._db._update({"_id": id}, _obj)
            self.__count += 1
            var._debug and print("Data Ready for CSV Count: ", self.__count)

    def __del__(self):
        var._active_print and print("Processed Count: ", self.__count)
        var._debug and print("Data Cleaning" + var._complete_msg)


class DataCollection(object):
    # init method
    def __init__(self):
        var._debug and print("Data Collection" + var._init_msg)

    def _collect(self, _fetch_query=None):
        var._debug and print("Data Collecting!!")
        sleep(var._sleep_time_small)  # small time
        tweepy = Tweepy()
        tweepy._fetch(_fetch_query)
        sleep(var._sleep_time_small)  # small time
        var._debug and print("Data Collecting" + var._complete_msg)

    def __del__(self):
        var._debug and print("Data Collection" + var._complete_msg)
