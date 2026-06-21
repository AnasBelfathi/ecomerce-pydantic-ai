"""
Pyndactic models for data validation and serialization.
"""

from pydantic import BaseModel
from typing import Optional, List

class Product(BaseModel):
    """Product model for the store inventory."""
    name: str
    description: str
    price: int
    category: str
    size: List[str]
    color: List[str]
    image: str 


class Order(BaseModel):
    """Order placement model."""
    user_email: str
    product_name: str
    quantity: int 

class CartItem(BaseModel):
    """Shopping cart item model."""
    user_email: str
    product_name: str 
    quantity: int 


