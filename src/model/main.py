from . import  models
from .database import engine

models.Base.metadata.create_all(engine)
models.Base.metadata.reflect(engine)