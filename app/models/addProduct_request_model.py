from pydantic import BaseModel
from typing import List

class ProductAddRequest(BaseModel):
    contractId: str
    productName: str
    quantity: int
    quality: str
    farmerIds: List[str]
    offTakerID: str
    logisticID: str
    deliveryStatus: str
