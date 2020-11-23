from pydantic import BaseModel

class TrainParameters(BaseModel):
    model: str
    path: str
    testsize: float