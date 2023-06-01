from django.db import models


partCategory = (
    ('Frame', 'Frame'),
    ('Motor', 'Motor'),
    ('ESC', 'ESC'),
    ('FC Board', 'FC Board'),
    ('Propeller', 'Propeller'),
    ('Transmitter', 'Transmitter'),
    ('Battery', 'Battery'),
    ('Cables', 'Cables'),
    ('Camera', 'Camera'),
    ('Gears', 'Gears'),
)

Featured = (
    ('Featured', 'Featured'),
    ('Not_Featured', 'Not_Featured'),

)

inStock = (
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
)


class droneParts(models.Model):
    name = models.CharField(max_length=255, default="")
    cPrice = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=partCategory, default="")
    color = models.CharField(max_length=100, default="")
    currency = models.CharField(max_length=100, default="")
    availability = models.CharField(max_length=100, choices=inStock, default="")
    featured = models.CharField(max_length=100, choices=Featured, default="")
    label1 = models.CharField(max_length=100, default="")
    label2 = models.CharField(max_length=100, default="")
    label3 = models.CharField(max_length=100, default="")
    label4 = models.CharField(max_length=100, default="")
    label5 = models.CharField(max_length=100, default="")
    label6 = models.CharField(max_length=100, default="")
    input1 = models.CharField(max_length=100, default="")
    input2 = models.CharField(max_length=100, default="")
    input3 = models.CharField(max_length=100, default="")
    input4 = models.CharField(max_length=100, default="")
    input5 = models.CharField(max_length=100, default="")
    input6 = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    image = models.FileField(upload_to='DroneParts/Thumbnail', default="")


class dronePartsImages(models.Model):
    def upload_design_to(self, filename):
        return f'DroneParts/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(droneParts, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_design_to)