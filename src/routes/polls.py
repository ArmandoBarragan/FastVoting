""" List polls, Poll detail, Create poll, Answer Poll, Delete poll"""
from fastapi import APIRouter

router = APIRouter()


@router.get('/',
            tags=['polls'])
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


@router.get('/polls/{poll_id}',
            tags=['polls'])
async def poll_detail(poll_id):
    """ Poll detail
    Returns the details of the polls. The data it returns is:
    - Title
    - Group
    - Expiring date
    - Description
    - Options
    """
    return {
        "poll": poll_id
    }


@router.post('/polls/{group_id}',
             tags=['polls'])
async def create_poll(group_id: int):
    return "Poll created"


@router.post('/polls/{poll_id}/{answer_id}',
             tags=['polls'])
async def answer_poll(poll_id: int, answer_id: int):
    """Answer poll"""
    return "Poll answered"


@router.delete('/polls/{poll_id}',
               tags=['polls'])
async def delete_poll(poll_id):
    """ Delete poll """
    return "Poll deleted"


@router.put('/polls/{poll_id}',
            tags=['polls'])
async def edit_poll(poll_id):
    """ Edit poll"""
    return poll_id
