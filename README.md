## pywater

### How to run it

1. First clone this repo, and navigate into the folder,
   ```
   $ git clone https://github.com/PinYu1618/pywater.git
   $ cd pywater
   ```
2. Create virtual environment,
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
3. Install dependencies,
   ```
   (venv) $ pip install -r requirements.txt
   ```
4. Run it.
   ```
   (venv) $ python main.py
   ```

### Folder Structure

```
pywater/
|
|_ db/
|_ pywater/
|  |_ __init__.py
|  |_ app.py
|  |_ notify.py
|  |_ pywater.py
|  |_ models/
|  |_ views/
|_ tests/
|_ README.md
|_ requirements.txt
```

### LICENSE

GPL (required by package pyqt5)

### Credits

- [Fugue icon set by Yusuke Kamiyamane](https://p.yusukekamiyamane.com/)