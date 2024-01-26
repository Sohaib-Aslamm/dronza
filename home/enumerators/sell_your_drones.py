from django.db import models


class PRODUCT_TYPE(models.TextChoices):
    DRONE = 'drone', 'Drone'
    PARTS = 'parts', 'Parts'


class PRODUCT_CATEGORY(models.TextChoices):
    A1 = 'a1', 'A1 250-900g'
    A2 = 'a2', 'A2 4kg'
    A3 = 'a3', 'A3 25kg'


class SOLD_STATUS(models.TextChoices):
    AVAILABLE = 'available', 'Available'
    SOLD = 'sold', 'Sold'


class SPEED_MODE(models.TextChoices):
    LOW_SPEED = 'low_speed', 'Low-speed'
    HIGH_SPEEED = 'high_speed', 'High-speed'


class WING_TYPE(models.TextChoices):
    MULTI_ROTOR = 'multi_rotor', 'Multi-rotor'
    FIXED_WING = 'fixed_wing', 'Fixed-wing'


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
    