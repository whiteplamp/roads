import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,  # WHAT A TYPE PLS FASTAPI FIX IT?????
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8000, )
