
# MICRO-SERVICE STARTING TEMPLATE

a FastAPI based template in order to start working on the building of Microservices backend. you are not allowed to change the root route, you can start working on API router, for your understanding a sample router with db operation given, you can delete the router if needed, but do take care the way how it's done.



### Pre-requists
Python 3, Docker, Git, Any Code editor.

## How to Setup?

**Step 1: Make the initial configuration**

Clone this repository using 

    $ git clone <link to this repository>

open the cloned floder in the terminal or a code editor which has terminal. then create a python virtual enviornment in root directory using following command

    $ python3 -m venv <virtual enviornment name>

activate the virtual enviornment with respect to your operating system and if the virtual enviornment name is not **venv** then add the name to the .gitignore file.

**Step 2: Install Dependencies**

after activating the virtual enviornment or pyenv run 
    $ pip install -r requirement.txt

on the root directory


**Step 3: Setup the enviornment variables**

in order to run the server you need to add one more file named **.env** in the 'app' directory, the conents for the file given in the *.envsample* file. You can copy and past it and replace the value. For the value you can [request here](mailto:deepak.ms@kireap.com?subject=GetDBCredentials)

**Step 4: Run the server**

For running the server, execute the following command:

    $ uvicorn app.main:app --reload --port <port number>


**Step 5: access the server**

you can access the server by going to the link 
```
https://localhost:<port number>
```

## Constrains

* You need to follow the coding standards preposed by SonarLint(SonarCube),Flake8 (You can user Ruff also.)

* Don't change the flow the code.
* You are not allowed to modify the codes in main.py, connectivity.py, scripts directory, docker files.(N.B.: You can change the container name in the docker-compose file if it is confilicting.)


## Authors

- [@Deepak M S](https://www.github.com/Deepak-coder80)

