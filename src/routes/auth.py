""" Create user, Edit user, Delete user, Log in, Log out"""
from fastapi import APIRouter


router = APIRouter()


@router.get('/users/{user_id}',
            tags=['auth'])
async def get_user(user_id: int):
    """ Get user
    Returns user's data:
    - Name.
    - Last Name """
    return user_id


@router.post('/users/create',
             tags=['auth'])
async def create_user():
    return "User created"


@router.delete('/users/',
               tags=['auth'])
async def delete_user():
    return "User deleted"


@router.put('/users/',
            tags=['auth'])
async def edit_user():
    return 'User edited'


@router.post('/users/login',
             tags=['auth'])
async def login():
    return "Logged in"


@router.post('/users/logout',
             tags=['auth'])
async def logout():
    return "Logged out"
