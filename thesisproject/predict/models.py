from django.db import models

# Create your models here.
class PredResults(models.Model):

    floor_num = models.FloatField()
    floor_area = models.FloatField()
    column_area = models.FloatField()
    concrete_wall_areaNS = models.FloatField()
    concrete_wall_areaEW = models.FloatField()
    masonry_wall_areaNS = models.FloatField()
    masonry_wall_areaEW = models.FloatField()
    captive_column = models.BooleanField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
