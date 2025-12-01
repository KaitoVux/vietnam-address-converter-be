from fastapi import APIRouter, HTTPException
from models.schemas import AddressInput, FullAddressInput, ConversionResponse
from services.converter import convert_old_to_new, convert_new_to_old

router = APIRouter(prefix="/api/convert", tags=["conversion"])

def parse_full_address(address: str) -> dict:
    """Parse comma-separated full address into components.

    Expected formats:
    - Old format (4 parts): street, ward, district, province
    - New format (3 parts): street, ward, province
    - Without street (3 parts): ward, district, province
    - Without street (2 parts): ward, province
    """
    parts = [part.strip() for part in address.split(',')]

    if len(parts) == 4:
        # Full address with street: street, ward, district, province
        return {
            'street': parts[0],
            'ward': parts[1],
            'district': parts[2],
            'province': parts[3]
        }
    elif len(parts) == 3:
        # Could be: street, ward, province (new) OR ward, district, province (old)
        # We'll assume street, ward, province for now
        return {
            'street': parts[0],
            'ward': parts[1],
            'district': '',
            'province': parts[2]
        }
    elif len(parts) == 2:
        # ward, province
        return {
            'street': '',
            'ward': parts[0],
            'district': '',
            'province': parts[1]
        }
    else:
        raise ValueError("Invalid address format. Expected 2-4 parts separated by commas.")

@router.post("/old-to-new", response_model=ConversionResponse)
async def convert_address_old_to_new(address: AddressInput):
    """Convert address from old (63 provinces) to new (34 provinces) format."""
    try:
        result = convert_old_to_new(
            province=address.province,
            district=address.district,
            ward=address.ward,
            street=address.street
        )
        return ConversionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/new-to-old", response_model=ConversionResponse)
async def convert_address_new_to_old(address: AddressInput):
    """Convert address from new (34 provinces) to old (63 provinces) format."""
    try:
        result = convert_new_to_old(
            province=address.province,
            district=address.district,
            ward=address.ward,
            street=address.street
        )
        return ConversionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quick/old-to-new", response_model=ConversionResponse)
async def quick_convert_old_to_new(input_data: FullAddressInput):
    """Quick convert from old to new format using full address string."""
    try:
        parsed = parse_full_address(input_data.address)
        result = convert_old_to_new(
            province=parsed['province'],
            district=parsed['district'],
            ward=parsed['ward'],
            street=parsed['street'] or None
        )
        return ConversionResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quick/new-to-old", response_model=ConversionResponse)
async def quick_convert_new_to_old(input_data: FullAddressInput):
    """Quick convert from new to old format using full address string."""
    try:
        parsed = parse_full_address(input_data.address)
        result = convert_new_to_old(
            province=parsed['province'],
            district=parsed['district'],
            ward=parsed['ward'],
            street=parsed['street'] or None
        )
        return ConversionResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
