# flask-docker
Docker project that runs flask web app
**Dockerfile**-- that runs my web app  **run.py** and runs  **python:3.7-alpine** and  **requirements.txt** that conatins all the softwares needed to run flask web app. file that builds my app and pulls mysql into docker with building volumes in the container.
**docker-compose.yml**--builds my image and mysql conatiner.
**app folder**-- conatins my web app files like **routes.py**,**forms.py**,**models.py** and **__init__.py**
**templates folder**-- contains html files like **about.html**,**login.html**,**account.html**,**reegistration.html**
The main aim was to launch my flask web app into docker and pull up the login and registration webpage for the user to register and hover the site.
For this we have to 

```systemctl start docker```(Make sure docker installed in Redhat8)

```cd flask```(if you are in root directory)

```docker-compose build```(builds our image in Dockerfile and installs softwares in requirements.txt){Make sure you have installed docker-compose}

```docker-compose up``` or ```docker-compose up -d``` (runs your docker-compose.yml file)

5.Open web browser of our vm machine and type ```0.0.0.0:5000```(pulls up web app first page)

6.```docker-compose down```(stops the running app)
