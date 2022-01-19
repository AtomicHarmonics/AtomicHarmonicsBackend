
Installation steps:
pip install virtualenv
virtualenv testEnv
source testEnv/bin/activate
pip install flask flask_marshmallow flask_cors sqlalchemy


Running the application steps:
You are going to have to activate your python virtualenvironment each time you want to run:
source testEnv/bin/activate (note you dont need to run the virtualenv command as done in the Installation steps, you only need to run the activate binary when you already setup your virtualenv)
python app.py


To exit:
press ctrl and C to exit the application
type 'deactivate' to exit your python virtualenvironment.


Server info:
There are various endpoints that the server is setup to use, almost all of which recieve and transmit data via JSON.