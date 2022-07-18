import uvicorn

from src.settings import PORT, DEBUG, HOST

# if __name__ == "__main__":
#     uvicorn.run('app:app',
#                 host=HOST,
#                 port=PORT,
#                 )

if __name__ == "__main__":
    uvicorn.run('src.app:app',
                host='0.0.0.0',
                port='8000',
                )
