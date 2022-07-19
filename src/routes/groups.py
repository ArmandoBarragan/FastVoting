""" Create group, Personal groups, Public groups, Join Group, Exit group, Delete group,
Edit group"""
from fastapi import APIRouter

router = APIRouter()


@router.get('/groups/',
            tags=['groups'])
async def public_groups():
    return 'Groups'


@router.get('/groups/',
            tags=['groups'])
async def personal_groups(user_id: int):
    return user_id


@router.post('/groups/{group_id}/join',
             tags=['groups'])
async def join_group(group_id: int):
    return group_id


@router.post('/groups/{group_id}/exit',
             tags=['groups'])
async def exit_group(group_id:int):
    return group_id


@router.delete('/groups/{group_id}',
               tags=['groups'])
async def delete_group(group_id: int):
    return group_id


@router.put('/groups/{group_id}',
              tags=['groups'])
async def edit_group(group_id: int):
    return group_id
