from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Annotated, Literal, Optional


class Item(BaseModel):
    id: Annotated[int, Field(gt=0, description="The ID of the item, must be greater than 0")]
    name: Annotated[str, Field(min_length=1, description="The name of the item, must not be empty")]
    price: Annotated[float, Field(gt=0, description="The price of the item, must be greater than 0")]
    description: Annotated[str | None, Field(description="The description of the item")] = "NA"
    Note: Annotated[str | None, Field(description="Additional notes about the item")] = "NA"
    date_posted: Annotated[str, Field(description="The date the item was posted in YYYY-MM-DD format")]


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    description: str | None
    note: str | None
    date_posted: str


class DeleteResponse(BaseModel):
    message: str
    item: ItemResponse
