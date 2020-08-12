from django.db import models
from django.utils import timezone
# from django.core.exceptions import ValidationError
import datetime


class Driver(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='drivers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    authorized = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    watchdog = models.DateTimeField(default=timezone.now)

    def update_watchdog(self):
        self.watchdog = timezone.now()

    def check_watchdog(self):
        if timezone.now() > self.watchdog + datetime.timedelta(minutes=5):
            self.is_online = False
        else:
            self.is_online = True

    def save(self, *args, **kwargs):
        # if self.watchdog is None:
        #     self.watchdog = timezone.now()
        self.check_watchdog()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return f'{self.name}'


class Device(models.Model):
    driver = models.ForeignKey(Driver, related_name='devices', on_delete=models.CASCADE)
    # room = models.ForeignKey(Room, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank=True, default='')
    is_online = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Talent(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey('auth.User', related_name='talents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    state = models.BooleanField(default=False)
    set_on = models.BooleanField(default=False)
    set_off = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} -- {self.device}'


class PanelStyle(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    talents = models.ManyToManyField(Talent)

    # def save(self, *args, **kwargs):
    #     print('I found this many talents: ', self.talents.count())
    #     if self.talents.count() < 7:
    #         return super(PanelStyle, self).save(*args, **kwargs)
    #     raise ValidationError("Too many talents mate")

    def __str__(self):
        return f'{self.name}'
