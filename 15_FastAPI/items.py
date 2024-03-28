from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/items/{item_id}',
            status_code=200,
            tags=['itemes', 'payment'],
            summary='특정 아이템 가져오기',
            description='item 모델에서 item_id 값을 가지고 특정 아이템을 조회한다.'
            )
def get_item(item_id: int):
    return {'items': item_id}