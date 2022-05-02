# Security control panel

It's the internal repository for bank 'Siyaniye' employees. If you accidentally find this repository, you couldn't run it, because you haven't DB access, but you can to use code or look the requests implementation.

## How to install

Before run the script, create the `.env` file with your settings and put it into `project` folder. 

Settings you need to add in file:

```
SECRET_KEY='some secret key'

DB_HOST=DB host url
DB_PORT=DB port number
DB_NAME=DB name
DB_USER=login
DB_PASSWORD=password

DEBUG=False         #or True to enable Debug settings

ALLOWED_HOSTS=localhost, 127.0.0.1    #list of hosts allowed to run script
```

After creating file, open console and change current directory to programm main directory.

This script use old version of Django, you need to run virtual environment and setup and install modules from `requiremets.txt`.

Console command to install and run virtual environment:

```
python -m venv DIR_NAME    # creating new folder and put enviromnet files here

C:\...\DIR_NAME\Scripts\Activate   # activate virtual environment
```
 
After that, your console will looks like (example DIR_NAME == env_folder):

```
(env_folder) C:\...
```

Install modules:

```
pip install -r requirements.txt
```

## Run script

If you did everything right, you can run the script with your own settings:

```
-python manage.py runserver 0.0.0.0:8000

>>> System check identified no issues (0 silenced).
>>> April 28, 2022 - 00:02:56
>>> Django version 3.2.13, using settings 'project.settings'
>>> Starting development server at http://0.0.0.0:8000/
>>> Quit the server with CTRL-BREAK.
```

You can check it in your browser, open link `127.0.0.1:8000`

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
