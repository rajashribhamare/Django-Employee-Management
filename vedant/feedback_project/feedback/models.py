from django.db import models

# Create your models here.
class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=[(1, "Poor"),(2,"Fair" ),(3,"Good"),(4,"VeryGood"),(5,"Excellent")])


    def __str__(self):
        return f"{self.student_name} - {self.course_name}"