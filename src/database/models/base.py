from sqlalchemy.orm import registry
from database.db_manager import dal
mapper_registry = dal.mapper_registry

Base = mapper_registry.generate_base()
