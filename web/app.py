from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.parser import fetch_data, parse_points
from src.decoder import build_grid
from src.renderer import save_as_image

app = FastAPI()

templates = Jinja2Templates(directory="web/templates")
app.mount("/static", StaticFiles(directory="web/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/decode", response_class=HTMLResponse)
def decode(request: Request, url: str = Form(...)):
    try:
        lines = fetch_data(url)
        points, max_x, max_y = parse_points(lines)
        grid = build_grid(points, max_x, max_y)

        # Convert grid to string for display
        grid_text = "\n".join("".join(row) for row in grid)

        # Save image
        image_path = "output/message.png"
        save_as_image(grid, image_path)

        return templates.TemplateResponse("index.html", {
            "request": request,
            "grid": grid_text,
            "image": "/" + image_path
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e)
        })
