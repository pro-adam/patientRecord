from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    detail = models.TextField()
    precaution = models.TextField()
    visit_date = models.DateTimeField(auto_now_add=True)
    next_visit_date = models.DateTimeField()

    def __str__(self):
        return self.full_name
