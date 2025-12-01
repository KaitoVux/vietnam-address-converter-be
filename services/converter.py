from vietnamadminunits import convert_address
from vietnamadminunits.parser.objects import AdminUnit
from typing import Dict, Optional

def format_address(street: Optional[str], ward: str, district: str, province: str) -> str:
    """Format address components into a single string."""
    parts = []
    if street:
        parts.append(street)
    parts.extend([ward, district, province])
    return ", ".join(parts)

def convert_old_to_new(province: str, district: str, ward: str, street: Optional[str] = None) -> Dict:
    """Convert address from old (63 provinces) to new (34 provinces) format."""
    try:
        # Construct address string
        old_address_str = format_address(street, ward, district, province)
        
        # Perform conversion
        # convert_address returns an AdminUnit object
        new_unit: AdminUnit = convert_address(old_address_str)
        
        # Extract new components
        # Note: AdminUnit might return None for some fields if not found
        new_province = new_unit.province or ""
        new_district = new_unit.district or ""
        new_ward = new_unit.ward or ""
        new_street = new_unit.street or street # Preserve street if not returned? Library seems to keep it.
        
        new_address_str = new_unit.get_address()

        return {
            "success": True,
            "old_address": old_address_str,
            "new_address": new_address_str,
            "message": "Conversion successful"
        }
    except Exception as e:
        return {
            "success": False,
            "old_address": None,
            "new_address": None,
            "message": f"Conversion failed: {str(e)}"
        }

def convert_new_to_old(province: str, district: str, ward: str, street: Optional[str] = None) -> Dict:
    """Convert address from new (34 provinces) to old (63 provinces) format."""
    return {
        "success": False,
        "old_address": None,
        "new_address": None,
        "message": "Reverse conversion (New to Old) is not currently supported by the underlying library."
    }
