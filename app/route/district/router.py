from fastapi import APIRouter
from app.route.district import service
from app.route.district.schema import DistrictRegistrationRequest

router = APIRouter(
    prefix="/district",
    tags=["district"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{district_id}")
async def get_district(district_id: int):
    """
    지역구 조회
    """
    res = service.get_district_record(district_id)
    return res


@router.get("/{parent_district}")
async def get_sub_districts(parent_district: str):
    """
    대형 구역의 하위 지역구 조회
    """
    res = service.get_sub_district(parent_district)
    return res

@router.post("/")
def add_district(register_request: DistrictRegistrationRequest):
    """
    후보자 정보 추가
    """
    res = service.create_district(register_request)
    return res

@router.delete("/{candidate_id}")
async def delete_candidate(candidate_id: int):
    """
    후보자 정보 삭제
    """
    return {"Hello": "World"}

@router.put("/")
async def update_candidate():
    """
    후보자 정보 수정
    """
    return {"Hello": "World"}