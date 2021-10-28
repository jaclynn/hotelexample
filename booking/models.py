from django.db import models

'''
                                 OCEAN
------------------------------------------------------------------------
| 100 | 102 | 104 | 106 | 108 |ELEV| 110 | 112 | 114 | 116 | 118 | 120 |
------------------------------------------------------------------------
|STAIR|                         HALLWAY                          |STAIR|
------------------------------------------------------------------------
| 101 | 103 | 105 | 107 | 109 |ELEV| 111 | 113 | 115 | 117 | 119 | 121 |
------------------------------------------------------------------------
                               COURTYARD
'''

BASE_PRICE = 200.00
SUITE_UPCHARGE = 0.25
OCEAN_UPCHARGE = 0.40

# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    price = models.FloatField(default=BASE_PRICE)
    occupied = models.BooleanField(default=False)
    oceanside = models.BooleanField(default=False)
    suite = models.BooleanField(default=False)

    def __str__(self):
        return "Room #" + str(self.room_num)

class Employee(models.Model):
    first = models.CharField(max_length=20)
    last  = models.CharField(max_length=20)
    empid = models.IntegerField(default=-1)

    def __str__(self):
        return self.first + " " + self.last

class Guest(models.Model):
    MR = 'MR'
    MS = 'MS'
    DR = 'DR'
    OT = ''
    HONORIFIC_CHOICES = [
        (MR, 'Mr.'),
        (MS, 'Ms.'),
        (DR, 'Dr.'),
        (OT, '')
    ]
    honorific = models.CharField(max_length=2, choices = HONORIFIC_CHOICES, default=OT)
    first = models.CharField(max_length=100)
    last  = models.CharField(max_length=100)
    vip = models.IntegerField(default=-1)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first + " " + self.last

    def get_absolute_url(self):
        return '/guestlist'

class Stay(models.Model):
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.guestid.first + " " + self.guestid.last + " staying " + str(self.start.month) + " " + str(self.start.day)
