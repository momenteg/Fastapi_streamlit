from pydantic import BaseModel

class IrisIn(BaseModel):
    sepal_l: float
    sepal_w: float 
    petal_l: float
    petal_w: float

class IrisOut(BaseModel):
    type_class: str
    probability: float
