# SocialMitux

### Description
>**SocialMitux** is a project created by *Manuel Rubio* or *ManuelIsCoding* on **GitHub**.
This project is developed using __Python__ and his microframework __Flask__.

![SocialMitux]('assets/readme.png')

### Instructions
- **Clone the GitHub repository**

> **$** git clone <https://github.com/ManuelIscoding/SocialMitux.git>

- **Activate virtualenv**

> **$** cd SocialMitux

> **$** source flask_env/bin/activate

- **Install the requirements using pip**

> **$** (flask_env) python3 -m pip install -r requirements.txt

- **Access to mysql database on root and create the next user**

> **$** (flask env) mysql -u root -p

> **mysql>** CREATE USER 'sm'@'localhost';

> **mysql>** GRANT ALL PRIVILEGES ON \* . \* TO 'sm'@'localhost';

> *(Ctrl+d) to exit*.

- **Execute and try the app**

*if virutalenv is not activate, reactivate it*

> **$** (flask_env) python3 run.py

> _**or**_

> **$** (flask_env) export FLASK_APP=run.py

> **$** (flask_env) python3 -m flask run
