from pydantic import BaseModel, Field
from typing import Optional

class AddressInput(BaseModel):
    province: str = Field(..., description="Province name")
    district: str = Field(..., description="District name")
    ward: str = Field(..., description="Ward name")
    street: Optional[str] = Field(None, description="Street address (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "province": "Hà Nội",
                "district": "Ba Đình",
                "ward": "Phúc Xá",
                "street": "123 Đường ABC"
            }
        }

class FullAddressInput(BaseModel):
    address: str = Field(..., description="Full address separated by commas")

    class Config:
        json_schema_extra = {
            "example": {
                "address": "123 Đường ABC, Phường Phúc Xá, Quận Ba Đình, Hà Nội"
            }
        }

class ConversionResponse(BaseModel):
    success: bool = Field(..., description="Whether conversion was successful")
    old_address: Optional[str] = Field(None, description="Address in old format")
    new_address: Optional[str] = Field(None, description="Address in new format")
    message: Optional[str] = Field(None, description="Error or info message")

    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "old_address": "123 Đường ABC, Phường Phúc Xá, Quận Ba Đình, Hà Nội",
                "new_address": "123 Đường ABC, Phường Phúc Xá, Quận Ba Đình, Thành phố Hà Nội",
                "message": "Conversion successful"
            }
        }
