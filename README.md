## pywater

### How to run it

First clone this repo, and navigate into the folder,

```
$ git clone https://github.com/PinYu1618/pywater.git
$ cd pywater
```

Then create virtual environment,

**Linux:**

```
$ python3 -m venv ./venv
$ source venv/bin/activate
(venv) $
```

**Windows:**

```
python -m venv venv
venv\Scripts\activate
```

Then install dependencies,

```
(venv) $ pip install -r requirements.txt
```

Run it.

```
(venv) $ python main.py
```

### Folder Structure

```
pywater/
|
|_ db/                 # db files
|_ pywater/
|  |_ __init__.py      # allow pywater to be a package
|  |_ app.py           # main window app
|  |_ notify.py        # notifier setup
|  |_ pywater.py
|  |_ models/
|  |_ views/
|_ tests/
|_ main.py
```

### LICENSE

GPL (required by package pyqt5)

### Credits

- [Fugue icon set by Yusuke Kamiyamane](https://p.yusukekamiyamane.com/)