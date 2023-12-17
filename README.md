## pywater

Health management app with python pyqt5.

### Gallery

#### Home Page

![Dashboard](./screenshots/app-home.png)

#### History Page

![History](./screenshots/app-history.png)

### How to run it

First clone the project, and navigate into the folder,

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

Install dependencies,

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
|_ db/                 # db csv files
|_ pywater/
|  |_ __init__.py      # allow pywater to be a package
|  |_ app.py           # main window app
|  |_ notify.py        # notifier setup
|  |_ pywater.py       # presenter class
|  |_ models/          # models
|  |_ views/           # ui
|_ tests/
|_ main.py
```

### LICENSE

GPL (required by package pyqt5)
