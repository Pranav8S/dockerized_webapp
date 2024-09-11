from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB, Query

# Non-persistant database and buffer 
with open ('db.json', 'a+') as f:
    with open ('db.history', 'a+') as r:
        r.write(f.read())
    f.seek(0)
    f.truncate(0)

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Set up TinyDB
db = TinyDB('db.json')

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit/")
async def submit_form(
    request: Request,
    name: str = Form(...),
    dob: str = Form(...),
    location: str = Form(...),
    feedback: str = Form(...)
):
    db.insert({"name": name, "dob": dob, "location": location, "feedback": feedback})
    return templates.TemplateResponse("form.html", {"request": request, "message": "Feedback submitted successfully!"})

@app.get("/view-feedbacks/", response_class=HTMLResponse)
async def view_feedbacks(request: Request):
    feedbacks = db.all()  # Retrieve all feedback entries from the database
    return templates.TemplateResponse("feedbacks.html", {"request": request, "feedbacks": feedbacks})

 
