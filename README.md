# this is a server for the exercise of the course.

## requirments

1. python 3.6

## run
```bash
pip install pipenv

pipenv install
```

wait to finish

## run the server

```bash
pipenv shell

python server_main.py
```

the server runs on port 3002
in order to change it:
in server_main.py
change:


```python
def run_server():
    app.run(port=3002)
```
to whatever port you wish
