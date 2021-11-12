import uvicorn
from fastapi import FastAPI
from .model.model import Classifier
from .Iris.Iris import IrisOut, IrisIn


clf = Classifier()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Fast api example to deploy a model for the iris classification"}


@app.get("/predict/", response_model=IrisOut)
async def score_model(iris: IrisIn):
    output = clf.predict(iris.dict())
    result = IrisOut(type_class=output['type'], probability=output['probability'])
    return result    
