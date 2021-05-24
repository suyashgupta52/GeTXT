try:
    import var
    import pymongo
except Exception as e:
    exit("Exception: " + str(e))

class MongoDB(object):
    def __init__(self, client="tenet", db= None):
        self.__client = pymongo.MongoClient(var._mongo_uri)
        self.__col = self.__client[client or var._db_client][db or var._db_name]        
        var._debug and print("MongoDB" + var._init_msg)

    def _insert(self, obj, _save=False):
        if _save == True:
            return self.__col.save(obj)
        self.__col.insert_one(obj)

    def _update(self, where_condition, set_data):
        self.__col.update_one(where_condition, set_data)

    def _count(self, obj = None):
        return self.__col.find(obj).count()

    def _find(self, obj=None, _limit=0, _offset=0):
        return self.__col.find(obj).skip(_offset).limit(_limit)

    def _sorted_find(self, obj=None, _limit=0, _offset=0 ,_sort= -1):        
        return self.__col.find(obj).skip(_offset).limit(_limit).sort("_id", _sort)

    def _delete(self, _obj):
        self.__col.delete_one(_obj)

    def __del__(self):
        self.__client.close()
        var._debug and print("MongoDB" + var._complete_msg)
