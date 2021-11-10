from django.db import models

# Create your models here.


class AirCraft(models.Model):
    model_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    seats = models.IntegerField()
    a_stat_list = [(0, 'operational'), (1, 'under maintenance'), (2, 'suspended')]
    a_status = models.IntegerField(blank=False, choices=a_stat_list, default=0)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    a_id = models.ForeignKey('AirCraft', on_delete=models.CASCADE)
    path = (models.ForeignKey('Airport', on_delete=models.CASCADE), models.ForeignKey('Airport', on_delete=models.CASCADE))
    time = (models.DateTimeField(), models.DateTimeField())
    fare = models.IntegerField()
    fl_stat_list = [('S', 'Scheduled'), ('A', 'Active'), ('L', 'Landed'), ('C', 'Cancelled')]
    fl_status = models.CharField(blank=False, choices=fl_stat_list, max_length=1, default='S')


class Airport(models.Model):
    city = models.CharField(max_length=30)
    run_c = models.IntegerField()
    ap_m_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Department(models.Model):
    ap_id = models.ForeignKey('Airport', on_delete=models.CASCADE)
    dept_list = [('A', 'Air traffic control'), ('M', 'Maintenance'), ('E', 'Emergency crew'), ('S', 'Security')]
    d_name = models.CharField(blank=False, choices=dept_list, max_length=1)
    d_head_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ap_id) + ' ' + str(self.d_name)


class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    d_id = models.ForeignKey('Department', blank=True, null=True, on_delete=models.CASCADE)
    super = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    age = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    ps_id = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    fl_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    seat_n = models.IntegerField()
    total_fare = models.IntegerField()
    statuses = [(0, 'Confirmed'), (1, 'Pending')]
    status = models.IntegerField(blank=False, choices=statuses, default=1)
