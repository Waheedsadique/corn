from fastapi import APIRouter, FastAPI

from fastapi_utils.tasks import repeat_every
import time
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


cronjob = APIRouter()

@cronjob.on_event("startup")
@repeat_every(hours=24)
def sample_cron():
    try:
        print("cron job is running")
        with open("dummyfile.txt", "a") as f:
            time = datetime.now()
            f.write(
                f"Hi this line was written by cronjob at {time} \n")
            f.close()
    except Exception as e:
        print("error in running cronjob")

app.include_router(cronjob)