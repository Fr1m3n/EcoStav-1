from django.db import models


# Create your models here.


def upload_path(instance, filename):
    return 'data/{0}'.format(filename)


class Image(models.Model):
    image = models.ImageField(upload_to=upload_path, null=True, default=None)
    datetime_published = models.DateTimeField(auto_now=True)
    coordinates = models.CharField(max_length=256, default='')
    neuro_result = models.CharField(max_length=1000, default='None')
    path_toResult = models.CharField(max_length=256, default='None')

    def __str__(self):
        out = str(self.datetime_published.day) + ':' + str(self.datetime_published.month) + ':' + str(
            self.datetime_published.year) + ' ' + str(self.datetime_published.hour) + ':' + str(
            self.datetime_published.minute)
        return out

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
