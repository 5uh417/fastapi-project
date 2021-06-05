from starlette.templating import Jinja2Templates
from starlette.requests import Request
import fastapi

templates = Jinja2Templates("templates")
router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})


@router.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
