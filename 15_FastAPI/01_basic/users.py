from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/users',
                   tags=['users'],
                   responses={
                       200:{'msg': 'Success to get data'},
                       400:{'msg': '404 not found'}
                   })

# api/v1/users/{user_id}
@router.get('/{user_id}')
def get_user(user_id: int):
    return {'dadta': user_id}