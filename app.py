
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()
app.include_router(api_router)

  
# if my_secret == "yes":
#   if __name__ == '__main__':
#     uvicorn.run(app,host="0.0.0.0",port="8080")