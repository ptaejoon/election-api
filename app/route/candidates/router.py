from fastapi import APIRouter
from app.route.candidates import service
from app.models.candidates import CandidatesORM

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{candidate_id}")
async def get_candidates(candidate_id: int):
    res = service.get_candidate_record(candidate_id)
    return res

@router.get("/")
async def list_candidates():
    return {"Hello": "World"}

@router.post("/")
def add_candidate():
    res = service.create_candidate_record(name="김철수")
    return res

@router.delete("/{candidate_id}")
async def delete_candidate(candidate_id: int):
    return {"Hello": "World"}

@router.put("/")
async def update_candidate():
    return {"Hello": "World"}