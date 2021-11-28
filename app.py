import uvicorn
from fastapi import FastAPI
from router import artical
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse

app = FastAPI(
    title="artical API",
    description="This is my homework i am trying",
    version="0.0.1",
    terms_of_service="http://localhost:5000"
)
app.include_router(artical.router)


@app.get("/")
def root():
    return {"title": "Hello World ,Hi Alice"}


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)

origins = [
    'http://localhost:3000'
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_method=["*"],
#     allow_headers=['*']
# )
