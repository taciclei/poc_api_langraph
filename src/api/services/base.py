from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.base import Base
from ..models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)

class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        return await db.get(self.model, id)

    async def get_all(self, db: AsyncSession) -> List[ModelType]:
        result = await db.execute(select(self.model))
        return result.scalars().all()

    async def create(self, db: AsyncSession, **kwargs) -> ModelType:
        db_obj = self.model(**kwargs)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, id: int, **kwargs) -> Optional[ModelType]:
        db_obj = await self.get(db, id)
        if db_obj:
            for key, value in kwargs.items():
                setattr(db_obj, key, value)
            await db.commit()
            await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int) -> bool:
        db_obj = await self.get(db, id)
        if db_obj:
            await db.delete(db_obj)
            await db.commit()
            return True
        return False
