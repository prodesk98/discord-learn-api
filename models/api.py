from typing import Optional, List
from pydantic import BaseModel, Field, AnyUrl


class UpsertResponse(BaseModel):
    success: Optional[bool] = True

class UpsertRequest(BaseModel):
    content: Optional[str] = Field(..., max_length=4000)
    username: Optional[str] = Field(None, max_length=56)
    namespace: Optional[str] = Field("default", max_length=32)

class QueryResponse(BaseModel):
    success: Optional[bool] = True
    responses: Optional[List[dict]] = []

class AnswerResponse(BaseModel):
    success: Optional[bool] = True
    response: Optional[str] = None

class TextToVoiceRequest(BaseModel):
    content: Optional[str] = Field(..., max_length=256)

class TextToVoiceResponse(BaseModel):
    success: Optional[bool] = True
    path: Optional[str] = None
    url: Optional[str] = None

class AnswerRequest(BaseModel):
    q: Optional[str] = Field(..., max_length=256)
    username: Optional[str] = Field("Anonymous", max_length=32)
    namespace: Optional[str] = Field("default", max_length=32)
    personality: Optional[str] = Field(None, max_length=350)
    swear_words: Optional[List[str]] = Field(None, max_items=20)
    informal_greeting: Optional[List[str]] = Field(None, max_items=20)

class GenQuizRequest(BaseModel):
    theme: Optional[str] = Field(..., max_length=100)
    amount: Optional[int] = 100
    namespace: Optional[str] = Field("default", max_length=32)

class GenQuizResponse(BaseModel):
    success: Optional[bool] = True
    question: Optional[str] = None
    alternatives: Optional[List[str]] = []
    truth: Optional[int] = -1
    voice_url: Optional[AnyUrl] = None

class VectorFilterRequest(BaseModel):
    filter: dict = {}
    sort: Optional[dict] = {"_id": -1}
    skip: Optional[int] = 0
    limit: Optional[int] = 100

class VectorDeleteRequest(BaseModel):
    ids: List[str]

class VectorDeleteResponse(BaseModel):
    success: Optional[bool] = True

class VectorUsernamesDeleteRequest(BaseModel):
    usernames: List[str]

class VectorUsernamesDeleteResponse(BaseModel):
    success: Optional[bool] = True
