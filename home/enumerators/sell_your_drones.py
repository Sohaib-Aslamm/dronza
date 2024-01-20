from django.db import models


class DRONE_CATEGORY(models.TextChoices):
    METAL = 'metal', 'Metal'
    FABRIC = 'fabric', 'Fabric'
    PLASTIC = 'plastic', 'Plastic'
    TITANIUM = 'titanium', 'Titanium'
    PARTS = 'parts', 'Parts'
    OTHER = 'other', 'Other'


class SOLD_STATUS(models.TextChoices):
    AVAILABLE = 'available', 'Available'
    SOLD = 'sold', 'Sold'


class DRONE_COLOR(models.TextChoices):
    WHITE = 'white', 'White'
    BLUE = 'blue', 'Blue'
    RED = 'red', 'Red'
    BLACK = 'black', 'Black'
    CUSTOM = 'custom', 'Custom'


class DRONE_CONDITION(models.TextChoices):
    EXCELLENT = 'excellent', 'Excellent'
    MINT = 'mint', 'Mint'
    GOOD = 'good', 'Good'


class DRONE_BRAND(models.TextChoices):
    DJI = 'dji', 'Dji'
    DRONZA = 'dronza', 'Dronza'
    MKT = 'mkt', 'Mkt'
    