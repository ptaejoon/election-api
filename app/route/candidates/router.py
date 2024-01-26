from fastapi import APIRouter

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{candidate_id}")
async def get_candidates(candidate_id: int):
    return {"Hello": "World"}

@router.get("/")
async def list_candidates():
    return {"Hello": "World"}

@router.post("/")
async def create_candidate():
    return {"Hello": "World"}

@router.delete("/{candidate_id}")
async def delete_candidate(candidate_id: int):
    return {"Hello": "World"}

@router.put("/")
async def update_candidate():
    return {"Hello": "World"}