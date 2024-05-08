from fastapi import APIRouter, status

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
async def get_tools():
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_tool():
    pass


@router.get("/{tool_id}", status_code=status.HTTP_200_OK)
async def get_tool(tool_id: str):
    pass


@router.put("/{tool_id}", status_code=status.HTTP_200_OK)
async def update_tool(tool_id: str):
    pass
