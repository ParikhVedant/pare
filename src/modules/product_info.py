"""
Product Information Module
Handles queries about PARE products.
"""

# Product information templates
PRODUCT_OVERVIEW = """
PARE offers a wide range of decorative panels to enhance walls, ceilings, and facades. 
Our products are designed for easy installation, durability, and aesthetic appeal.
"""

# Product categories information
WALL_PRODUCTS = """
PARE has an excellent selection of wall options, you may select from:
Linea, Pyramid, Arch which have wooden, marble and pastel shades
"""

CEILING_PRODUCTS = """
PARE has an excellent selection of ceiling options, you may select from:
Soffit, duo and louver panels which have wooden, marble and pastel shades
"""

FACADE_PRODUCTS = """
PARE has an excellent selection of facade options, you may select from:
Norma and Stretta panels
"""

# Specific product information
SPECIFIC_PRODUCTS = {
    "soffit": "Ideal for ceilings, offering a real wood appearance with a maintenance-free finish. Perfect for outdoor and indoor applications.",
    "easy+": "Wall panels that can be directly screwed onto walls, eliminating the need for plywood. Available in multiple shades and textures.",
    "dura+": "A robust façade solution that ensures long-lasting durability, UV resistance, and a wooden aesthetic.",
    "baffle": "A unique ceiling system that is lightweight, fire-retardant, and water-resistant, offering a sophisticated look to interiors."
}

# Brochure mapping
BROCHURE_MAPPING = {
    "wall": "easy+",
    "ceiling": "innov+",
    "facade": "dura+",
    "unsure": "company"
}

def get_product_overview() -> str:
    """Return general product overview."""
    return PRODUCT_OVERVIEW.strip()

def get_category_info(category: str) -> dict:
    """Get information about a specific product category."""
    message = ""
    brochure = None
    
    if category == "wall":
        message = WALL_PRODUCTS.strip()
        brochure = "easy+"
    elif category == "ceiling":
        message = CEILING_PRODUCTS.strip()
        brochure = "innov+"
    elif category == "facade":
        message = FACADE_PRODUCTS.strip()
        brochure = "dura+"
    elif category == "unsure" or category == "all" or category == "none":
        message = """
        PARE has an excellent selection for all, please check the company brochure
        for any products if it sparks up any ideas for you
        """.strip()
        brochure = "company"
    
    return {
        "message": message,
        "brochure": brochure
    }

def get_specific_product_info(product: str) -> str:
    """Get information about a specific product."""
    if product.lower() in SPECIFIC_PRODUCTS:
        return SPECIFIC_PRODUCTS[product.lower()]
    return None

def handle_product_query(category: str = None, specific_product: str = None) -> dict:
    """Handle a query about products."""
    response = ""
    brochure = None
    next_module = "lead_capture"
    
    if specific_product and specific_product.lower() in SPECIFIC_PRODUCTS:
        # Handle specific product query
        response = get_specific_product_info(specific_product.lower())
    elif category:
        # Handle category query
        category_info = get_category_info(category.lower())
        response = category_info["message"]
        brochure = category_info["brochure"]
    else:
        # General product overview
        response = f"{get_product_overview()}\n\nKindly mention the area you're interested in - Wall, ceilings or Facades or all/none?"
        next_module = "product_info"
    
    return {
        "message": response,
        "brochure": brochure,
        "next_module": next_module
    } 