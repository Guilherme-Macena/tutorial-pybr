from pydantic import BaseModel


class Item(BaseModel):
    sku: str
    description: str
    image_url: str
    reference: str
    quantity: int


class HealthCheckResponse(BaseModel):
    status: str


class ErroResponse(BaseModel):
    message: str
