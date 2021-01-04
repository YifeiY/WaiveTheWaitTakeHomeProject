from django.shortcuts import render,HttpResponse
from .database_simulation import main as database_simulator
from threading import Thread
DATABASE_FILENAME = 'database.db'



# TODO: follw up with Dan about the rest frontend, candidates will have to display info via that page. Bonus will be allocated if they can either update that page to be real time, or make a new websocket that can handle real time updates from the rest api. If Dan has no time however, then the candidates will be using the console.
def show_database(request):
    '''
    Please read the entire description and finish the tasks
    Please make a virtual environment for this project, package requirements are in requirements.txt
    Run python3 manage.py runserver 8080 in /WaiveTheWaitTakeHomeProject to run the server on port 8080 after activating the virtual environment

    Task:
    1. Make a simple web response function
    1.1. The database is updated by database_simulation.py. Which simulates different user behaviour over time
    1.2. The HTML will retrieve the database content every two seconds, and display them.
    1.3. Fill in the api_appointments, and the api_people to return the content of the database.
    When http://localhost:8000 is opened, templates/index.html is loaded to be the webpage.
    1.4 This one is evaluated by a) the correctness and cleanness of implementation,
    and BONUS b) the responsiveness of the updates, i.e. how long will it take for changes to the database to be reflected on the webpage
    For b), dont hesitate to modify database_simulation.py, and/or the frontend (index.html, or any other scripts you decide to make)

    2. Make either a bash/cmd script or an executable to start the django program, and open up http://localhost:8080 when opened.
    2.2 For starting a Django server on port 8080, please use python3 manage.py runserver 8080
    2.3 The DEBUG field in the settings file should remain True, you are not required to make a production ready service
    2.4 This one will be evaluated on Windows 10 OS, or MacOS/Linux 18.04, depending on the type of the script you made.

    3. The program is set to work with database.db. Please make a simple field in settings.py so the program can switch to another database easily, for example, the new_database.db
    3.1 For 3, you will probably need to change some fields in database_simulation.py that are related to the filenames
    3.2 This one will be evaluated for correctness and ease of switching to another new database with the same schemata

    Files that you should/might be modifying:
    1. views.py
    2. database_simulation.py
    3. settings.py
    4. urls.py
    5. any files under templates
    6. any files added by you

    Email yifei@waivethewait.com if you have problems setting the program up. Good luck!
    '''

    thread = Thread(target=database_simulator,args=())
    thread.setDaemon(True)
    thread.start()
    return render(request,'index.html')

def api_appointments(request):
    return HttpResponse({'content':'sample data'})

def api_people(request):
    return HttpResponse({'content':'sample data'})


