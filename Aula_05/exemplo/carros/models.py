from django.db import models

class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME') # Field name made low er-case.
    mpg = models.FloatField(db_column='MPG') # Field name made lower-case.
    cyl = models.IntegerField(db_column='CYL') # Field name made lower-case.
    disp = models.FloatField(db_column='DISP') # Field name made lower-case.
    hp = models.IntegerField(db_column='HP') # Field name made lower-case.
    wt = models.FloatField(db_column='WT') # Field name made lower-case.
    qsec = models.FloatField(db_column='QSEC') # Field name made lower-case.
    vs = models.IntegerField(db_column='VS') # Field name made lower-case.
    am = models.IntegerField(db_column='AM') # Field name made lower-case.
    gear = models.IntegerField(db_column='GEAR') # Field name made lower-case.

    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        return self.name