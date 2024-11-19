from django.db import models
from courses.models import Course
from django.conf import settings


# Create your models here.


class ReviewCycle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StudentEnrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "student"},
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"


class ReviewAssignment(models.Model):
    review_cycle = models.ForeignKey(ReviewCycle, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviewer",
        limit_choices_to={"role": "student"},
    )
    reviewee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviewee",
        limit_choices_to={"role": "student"},
    )
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} is reviewing {self.reviewee.username} in {self.review_cycle}"
