from fastapi import APIRouter
from app.route.candidates import service
from app.models.candidates import CandidatesORM
from app.route.candidates.schema import CandidateRegistrationRequest

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{candidate_id}")
async def get_candidates(candidate_id: int):
    """
    후보자 정보 조회
    """
    res = service.get_candidate_record(candidate_id)
    return res

@router.get("/")
async def list_candidates():
    """
    후보자 정보 리스트 조회
    """
    return {"Hello": "World"}

@router.post("/")
def add_candidate(register_request: CandidateRegistrationRequest):
    """
    후보자 정보 추가
    """
    res = service.create_candidate_record(register_request)
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