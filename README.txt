New Installation steps:
1.) Modify paths in flaskServer-script, ffmpeg-script, to match current directory. Ex: change /home/mohammed/Desktop/projects/flaskLearning/flaskApplication to /home/yourComputer/projects/currentDirectory
2.) run init_setup ex: 'source init_setup.sh'
3.) run setupServices ex: 'source setupServices.sh'

You do not need to repeat above steps every time, only once.

Now installation is complete, to run the server and all other services, simply run : 'systemctl --user start flaskServer.service'.
To stop the server simply run: 'systemctl --user stop flaskServer.service'

to view current logs of the server, run: 'journalctl --user -f -u flaskServer.service'

You will also don't need to run the front end seperately, the backend will serve it for you, simply head over to 'http://localhost:4996/staticContent/static/html/index.html' on your webbrowser to see the web application.

Installation steps (OBSOLETE!):
-------------------------------------------
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
------------------------------------------------------

Server info:
There are various endpoints that the server is setup to use, almost all of which recieve and transmit data via JSON.
