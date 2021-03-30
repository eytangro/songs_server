# song-server-swagger

This is swagger example for a song server.

## swagger configure
under sources folder change the config.ini file


## create a virtualenv
```
virtualenv venv --python=3.6
```

## activate the virtualenv
### windows
```
venv\Scripts\activate.bat
```

### linux
```
source venv/bin/activate
```

## install all requirements
```
pip install -r requirements.txt
```

## run the swagger server
```
python run_swagger.py
```

### if the server dosent run or showes errors try changing line 10 in run swagger.py file to the absolute path to the yaml file in sources


## when the server is up

go to
http://localhost:9090/ui
 to see the swagger ui
