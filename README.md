# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    Tests are written with [pytest](https://docs.pytest.org/) and live in the `tests/` folder,
    organised by type: `tests/integration/` (one file per feature), `tests/functional/`
    (full user journey) and `tests/performance/` (Locust).

    Run the whole suite from the project root:

        pytest

    Measure code coverage (target: at least 60%):

        pytest --cov=server --cov-report=term-missing

    An HTML report can be generated with `--cov-report=html` and opened at `htmlcov/index.html`.

6. Performance testing

    Performance tests use [Locust](https://locust.io/). They require the server to be
    running. In a first terminal:

        flask --app server run

    In a second terminal:

        locust -f tests/performance/locustfile.py --host http://127.0.0.1:5000

    Then open http://localhost:8089 and start a test with 6 users (the default number
    required by the specifications). Requirements: page loads under 5 seconds,
    updates under 2 seconds.

7. Branch organisation

    * `master` — the original code as delivered, with its known bugs, kept as reference.
    * `qa` — the up-to-date branch combining every fix and feature. **Clone and use this one.**
    * `bug/*`, `fonctionnalite/*`, `amelioration/*` — one branch per fix or feature,
      each merged into `qa` through a pull request.

