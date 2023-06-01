from django.db import models


class amazonProduct(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")


class amazonProductImages(models.Model):
    def upload_design_to(self, filename):
        return f'AmazonProducts/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(amazonProduct, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_design_to)