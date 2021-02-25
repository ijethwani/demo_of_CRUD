from django.db import models
posts = (
    ("CEO","CEO"),
    ("CTO","CTO"),
    ("Branch-Manager","Branch-Manager"),
    ("Project-Manager","Project-Manager"),
    ("Sales-Manager","Sales-Manager"),
    ("System-Manager","System-Manager"),
    ("Back-end Developer","Back-end Developer"),
    ("Front-end Developer","Front-end Developer"),
    ("Adminstrator","Adminstrator"),
)

class Employee(models.Model):
    emp_id = models.PositiveIntegerField(auto_created=True)
    name = models.CharField(max_length=100,verbose_name="Name Of Employee")
    age  = models.PositiveIntegerField(verbose_name="Age")
    address = models.CharField(max_length=200,verbose_name="Address")
    post = models.CharField(max_length=150,choices=posts,verbose_name="Post")
    exp = models.PositiveIntegerField(verbose_name="Experience in year")

    def __str__(self):
        return self.emp_id,"-",self.name

    class Meta:
        ordering = ["emp_id"]

    
