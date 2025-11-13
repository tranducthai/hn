"""Score data models"""
from typing import Optional

from pydantic import BaseModel, Field, conlist
from typing import List


class ROI(BaseModel):
    """Return on investment data"""

    times: float = Field(..., description="ROI multiplier")
    currency: str = Field(..., description="Currency")
    percentage: float = Field(..., description="ROI percentage")
    
class Score(BaseModel):
    id: List[float] = Field(
        ..., 
        min_items=8, 
        max_items=8, 
        description="Mảng gồm đúng 8 số (float)"
    )