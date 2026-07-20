from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated, Optional

class Input(BaseModel):
    age: Annotated[int, Field(..., gt=0)]
    weight:Annotated[float, Field(..., gt=0)]
    height:Annotated[float, Field(..., gt=0)]
    income_lpa:Annotated[float, Field(..., gt=0)]
    smoker:Annotated[bool, Field(...)]
    city:Annotated[str, Field(...)]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner'
                                 , 'unemployed', 'private_job'], Field(...)]
    