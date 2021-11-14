from pydantic import BaseModel


class Item(BaseModel):
    sku: str
    description: str
    image_url: str
    regerernce: str
    quantity: int
