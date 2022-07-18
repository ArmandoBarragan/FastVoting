import uvicorn

from settings import PORT, DEBUG, HOST

if __name__ == "__main__":
    uvicorn.run('app:app',
                host=HOST,
                port=PORT,
                )
