from fastapi import APIRouter
from src import models

Router = APIRouter()

@Router.post("/log")
def get_new_log(log: models.SrotasLogFormat):
    print(f"Received log: {log.log}")
    return log