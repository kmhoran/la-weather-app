from django.db import models
from datetime import datetime 


class Timestamps(models.Model):
    timestamp = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.timestamp = datetime.utcnow()
        return super(Timestamps, self).save(*args, **kwargs)

    def __str__(self):
        return "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{t.minute:02d}:{t.second:02d}".format( t=self.timestamp)


class Forecast(models.Model):
    timestamp = models.DateTimeField()
    temperatue = models.DecimalField(max_digits=12,decimal_places=2)
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = datetime.utcnow()
        return super(Forecast, self).save(*args, **kwargs)
