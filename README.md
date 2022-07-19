# Fast Voting
This project was made to apply new knowledge acquired with Platzi's FastAPI course. It is
for usage of my reading club, where we vote for new books to read after finishing the last one.
---

## Installing for backend development 
After cloning this project, you will have to execute the following commands: </br>
<ol>
<li>Create a virtual environment: <code>python3 -m venv env</code></li>
<li>Activate the venv: <code>source env/bin/activate</code></li>
<li>Install requirements: <code>pip install -r requirements.txt</code></li>
</ol>
Now you can run <code>uvicorn src.app:main --reload</code> to develop as much as you can.


## Installing for deployment or use it as a frontend
You need to have docker and docker-compose installed in your computer.
Once you have it installed you can choose between installing the local 
version or the production version. The command to install the project 
would either be <code>docker-compose -f production.yml up --build -d</code>
or <code>docker-compose -f local.yml up --build -d</code>. It should install
the application along with a database for your computer. Whenever there is
an update, you will have to pull changes and do <code>docker-compose -f production.yml down</code>
or <code>docker-compose -f local.yml down</code> and then rebuild.
</br>
If you are going to deploy this project, you might want to change the example.env file,
to use a different key than the one that is in this repository.
## Using the API
Once you have the application up and running, you can just open your browser
and open 0.0.0.0:8000/docs (those are the default host and port), so you can
enter the documentation and see every endpoint that is registered in this app, 
along with its parameters, name, purpose and what it returns.