import uvicorn

from src.settings.settings import PORT, DEBUG, HOST

if __name__ == "__main__":
    uvicorn.run('src.app:app',
                host=HOST,
                port=PORT,
                reload=DEBUG
                )
#
# if __name__ == "__main__":
#     uvicorn.run('src.app:app',
#                 host='0.0.0.0',
#                 port=8000,
#                 reload=True
#                 )
