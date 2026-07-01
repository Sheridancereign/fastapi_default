from fastapi import APIRouter
from repo import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(
        task: STaskAdd
) -> STaskId:
    task_id = await TaskRepository.add_one_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> STask:
    tasks = await TaskRepository.get_all_tasks()
    return tasks
