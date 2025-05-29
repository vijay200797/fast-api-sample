from model import models, schemas, database
from model import database
from fastapi import FastAPI,Depends
from pydantic_settings import BaseSettings
import uvicorn
from sqlalchemy.orm import Session

get_db = database.get_db

models.Base.metadata.create_all(database.engine)
models.Base.metadata.reflect(database.engine)


app = FastAPI(root_path = "/",
    version = "0.1.0",
   )

@app.post('/people')
def create(request: schemas.People, db: Session = Depends(get_db)):
    new_people = models.People(age=request.age, name=request.name)
    db.add(new_people)
    db.commit()
    db.refresh(new_people)
    return new_people


@app.get('/people')
def get_peoples(db: Session = Depends(get_db)):
    print("Load Peoples")
    peoples = db.query(models.People).filter(models.People.age > 20).all()
    return peoples
    
# Use Below Command to Open API
# uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000" )
    




