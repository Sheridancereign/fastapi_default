from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column




class Model(DeclarativeBase):
    pass

engine = create_async_engine(
    "sqlite+aiosqlite:///./test.db"
)


new_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)

class TasksOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    is_completed: Mapped[bool] = mapped_column(default=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)