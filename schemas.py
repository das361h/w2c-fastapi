from pydantic import BaseModel
from typing import List, Optional, Any

class RecipeBase(BaseModel):
    rid: str
    rname: str
    ribs: Any
    ringred: Any
    rtype: str
    rserving: int
    rcuisine: str
    roveralltime: str
    rstep: Any
    rimage: str

    class Config:
        orm_mode = True
