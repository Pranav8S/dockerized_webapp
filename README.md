1. Application Overview

The application is a simple feedback system built using FastAPI, a fast web framework for building APIs with Python and TinyDB, a lightweight document-oriented database. This web app allows users to submit feedback through a web form and view all submitted feedbacks.


2. Application Structure

web_app/
├── __pycache__/
├── Include/
├── Lib/
├── Scripts/
├── templates/
│   └── form.html
│   └── feedbacks.html
├── db.json
├── Dockerfile
├── main.py
├── pyvenv.cfg
└── requirements.txt	


3. Implementation Details-

3.1 Virtual Environment
This web app uses a Python virtual environment in the directory 'web_app'. This isolates the project dependencies from the global Python installation. 
`python -m venv web_app`


3.2 FastAPI Application
The `main.py` file sets up the FastAPI application with the following features:
•	Initializes FastAPI and sets up Jinja2 templates
•	Creates a TinyDB instance for data storage
•	Defines three routes:
  	1. GET "/": Renders the feedback submission form
  	2. POST "/submit/": Handles form submission and stores data in TinyDB
  	3. GET "/view-feedbacks/": Retrieves and displays all submitted feedbacks

3.3 HTML Templates
•	`form.html`: Contains the feedback submission form
•	`feedbacks.html`: Displays all submitted feedbacks
Both templates use simple HTML structures with some Jinja2 templating for dynamic content.

3.4 Database
•	TinyDB is used as a lightweight, file-based JSON database. 
•	The database file (`db.json`) is created automatically when the first feedback is submitted.


4. Dependencies-
The `requirements.txt` file lists all necessary Python packages, including:
•	FastAPI (python-based web framework)
•	Uvicorn (bundled-in ASGI server)
•	Jinja2 (templating engine)
•	TinyDB (document datastore)
•	Python-multipart (for form handling)


5. Dockerization-
The application is containerized using Docker, as defined in the `Dockerfile` below:

FROM python:3.11
WORKDIR /web_app
COPY ./requirements.txt /web_app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /web_app/requirements.txt
COPY ./templates /web_app/templates
COPY ./main.py /web_app/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

•	Uses Python 3.11 as the base image
•	Sets the working directory to `/web_app`
•	Copies and installs the requirements
•	Installs Python packages from `requirements.txt` without caching and upgrades them to the latest versions within the Docker image.
•	Copies the application files (templates and `main.py`)
•	The command	 `CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]` 	specifies the default command that runs the Uvicorn server when a container starts


6. Building the container and running the Application
To set up and activate the virtual environment:
python -m venv web_app
source web_app/bin/activate  	# On Unix/Linux based OS
web_app\Scripts\activate.bat  	# On Windows

To build the Docker image:
1. Install Docker
   sudo yum/apt install docker

2. Create requirements file inside the project
   pip freeze > requirements.txt

3. Create a Dockerfile with the aforementioned statements which specifies the python setup, copies project files and the command to run the fast api application.

4. Create .dockerignore file to exclude any cache/logs or unncessary files from persisting in the docker image

5. Build the container  
   docker build -t vcc_assignment_web_app_lite
•	`-t` vcc_assignment_web_app_lite tags the image with the name "vcc_assignment_web_app_lite"
•	The `.` specifies the build context, which is the current directory


6. Test the Docker container:
   docker run -p 8000:8000 fastapi-feedback-app
•	`-p 8000:8000` maps port 8000 on the host machine to the port 8000 in the container.
•	vcc_assignment_web_app_lite is the name of the Docker image.
•	`docker ps` command will list all the current active containers with their respective image ids.
The application will be accessible at `http://localhost:8000`.

To run the application:
1. Pull image from Docker hub:
   docker pull pranav8s/vcc_assignment_web_app_lite

2. Run the Docker container using image
   docker run -d -p 8000:8000 --name vcc_assignment_web_app  vcc_assignment_web_app_lite
The application will be accessible at `http://localhost:8000`.


7. Conclusion
This FastAPI/TinyDB application demonstrates a simple web-app deployment using Docker. It showcases the use of FastAPI, TinyDB and containerization techniques.
