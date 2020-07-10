from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory='static'), name="static") # Mount static files, specify directory


templates = Jinja2Templates(directory='templates') #Template Directory


@app.get("/data/")
async def read_data(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)