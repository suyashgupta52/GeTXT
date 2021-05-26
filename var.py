# Import Libs
try:    
    from os import environ
    import random
except Exception as e:
    exit("Exception: " + str(e))

# Define Variables
_deployment_env = True

if _deployment_env:
   # Prod ENV
   # Debug
    _debug = True
    # Sleep
    _sleep_time_small = random.randint(1, 10)
    # tweepy 
    _tweet_max_count = 500
    _tweet_limit = 500
    _consumer_key =    environ['C_KEY']   
    _consumer_secret = environ['C_SEC']
    _auth_token =    environ['A_TOKEN']
    _auth_secret =  environ['A_SEC']
    _mongo_uri =   environ['MONGO_URI']
else:
    import key
    # Dev ENV
     # Debug
    _debug = True
    # Sleep
    _sleep_time_small = 0.5
    # tweepy 
    _tweet_max_count = 5
    _tweet_limit = 5
    # Define Variables Keys    
    _consumer_key =  key._consumer_key 
    _consumer_secret = key._consumer_secret
    _auth_token =  key._auth_token 
    _auth_secret =  key._auth_secret 
    _mongo_uri =  key._mongo_uri 
    
_min_text_len = 150    
_offset = random.randint(0, 1500)
# msg
_init_msg = " Initiated !!"
_complete_msg = " Completed!!"

#databse
_db_client = "tenet"
_db_name = "dataset"