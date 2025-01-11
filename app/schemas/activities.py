from pydantic import BaseModel


class OrganizationActivityBase(BaseModel):
    id: int
    name: str
