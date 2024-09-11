# Feedback System Web Application

This project is a simple feedback system built using FastAPI, a high-performance web framework for Python, and TinyDB, a lightweight document-oriented database. The application allows users to submit feedback through a web form and view all submitted feedbacks.

## Application Structure

```
web_app/
├── pycache/
├── Include/
├── Lib/
├── Scripts/
├── templates/
│   ├── form.html
│   └── feedbacks.html
├── db.json
├── Dockerfile
├── main.py
├── pyvenv.cfg
└── requirements.txt
```

## Implementation Details

### Virtual Environment

This application uses a Python virtual environment to isolate project dependencies. Set up the virtual environment with:

```sh
python -m venv web_app
```

Activate the virtual environment:

- On Unix/Linux:

  ```sh
  source web_app/bin/activate
  ```

- On Windows:

  ```sh
  web_app\Scripts\activate.bat
  ```

### FastAPI Application

The `main.py` file sets up the FastAPI application with:

- FastAPI initialization and Jinja2 template setup
- TinyDB instance for data storage
- Routes:
  - `GET "/"`: Renders the feedback submission form
  - `POST "/submit/"`: Handles form submission and stores data in TinyDB
  - `GET "/view-feedbacks/"`: Retrieves and displays all submitted feedbacks

### HTML Templates

- `form.html`: Feedback submission form
- `feedbacks.html`: Displays all submitted feedbacks

Both templates use simple HTML structures with Jinja2 templating for dynamic content.

### Database

- **TinyDB**: Lightweight, file-based JSON database
- The database file (`db.json`) is created automatically when the first feedback is submitted.

### Dependencies

The `requirements.txt` file includes:

- **FastAPI**: Web framework for Python
- **Uvicorn**: ASGI server
- **Jinja2**: Templating engine
- **TinyDB**: Document datastore
- **python-multipart**: For form handling

### Dockerization

The application is containerized using Docker. The `Dockerfile` includes:

```Dockerfile
FROM python:3.11
WORKDIR /web_app
COPY ./requirements.txt /web_app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /web_app/requirements.txt
COPY ./templates /web_app/templates
COPY ./main.py /web_app/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- Uses Python 3.11 as the base image
- Sets the working directory to `/web_app`
- Copies and installs the requirements
- Copies application files (templates and `main.py`)
- Specifies the command to run the Uvicorn server

### Building and Running the Container

1. **Install Docker**:

   ```sh
   sudo yum install docker
   # or
   sudo apt install docker
   ```

2. **Create the requirements file**:

   ```sh
   pip freeze > requirements.txt
   ```

3. **Create a `.dockerignore` file** to exclude unnecessary files.

4. **Build the Docker image**:

   ```sh
   docker build -t vcc_assignment_web_app_lite .
   ```

5. **Test the Docker container**:

   ```sh
   docker run -p 8000:8000 vcc_assignment_web_app_lite
   ```

   The application will be accessible at [http://localhost:8000](http://localhost:8000).

6. **To pull and run the Docker image**:

   ```sh
   docker pull pranav8s/vcc_assignment_web_app_lite
   docker run -d -p 8000:8000 --name vcc_assignment_web_app pranav8s/vcc_assignment_web_app_lite
   ```

   The application will be accessible at [http://localhost:8000](http://localhost:8000).

## Conclusion

This FastAPI/TinyDB application demonstrates a basic web app deployment using Docker. It showcases the use of FastAPI, TinyDB, and containerization techniques.
