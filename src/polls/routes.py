from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def list_polls():
    """ List Polls
    This is the main view of the site. It brings up all the polls the user can participate in
    Returns a json with the polls important info:
    - Title
    - Group
    - Expiring date """
    return {
        "polls": {
            {
                "title": "Next book",
                "group": "Reading club",
                "expiring date": "07/19/2022"
            }
        }}


# @router.get('/polls/1')
# async def poll_detail():
#     """ Poll detail
#     Returns the details of the polls. The data it returns is:
#     - Title
#     - Group
#     - Expiring date
#     - Description
#     - Options
#     """
#     return {
#         "poll":
#             {
#                 "title": "Next book",
#                 "group": "Reading club",
#                 "expiring date": "07/19/2022",
#                 "description": "What book should we read next?",
#                 "options": ["The Lord of the Rings", "Harry Potter", "Frankenstein"]
#             }
#     }
