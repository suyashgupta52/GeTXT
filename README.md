#   GeTXT: Data Text Fetching and Cleaning System using Tweepy API and MongoDB Depaly on Heroku | Python3



## To deploy directly
1. Fork this repo
2. Go to Heroku Account 
3. Connect your Repo
4. Go to Setting tabb and Under `Config Vars` click on `Reveal Config Vars` then add environ as per var.py
```python
'key' => 'Value'
'C_KEY' => ' ' 
'C_SEC' => ' '
'A_TOKEN' => ' '
'A_SEC' => ' '
'MONGO_URI' => ' '
```
5. Deploy the main Branch



## How to run on Local

1. Clone this Repo
2. Make a key.py file in root dir for connecting database and Tweepy API(If want to push Record to Database)

3. Key.py File format

```python
    # Tweepy Cunsumer Key
    _consumer_key = ""
    _consumer_secret = ""
    # Tweepy Auth Key
    _auth_token = ""
    _auth_secret = ""
    # Mongo DB URI
    _mongo_uri = ""
```
4. Go to var.py and "_deployment_env = False"

5. Activate a virtual env
```python
pip install virtualenv
virtualenv env
env\Scripts\activate
```

6. Install Requirements by Running
```python
pip install -r requirements.txt
```

8. Run 
```pyhton
py app.py
```

10. Press Ctrl + c to stop the System Manually.

11. Once All Done. To close Virtual env:
```
deactivate
```


#### This source code is licensed under the GPL-style license found in the LICENSE file in the root directory of this source tree. 