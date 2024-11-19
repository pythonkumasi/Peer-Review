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


class Review(models.Model):
    assignment = models.ForeignKey(ReviewAssignment, on_delete=models.CASCADE)
    review_text = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.assignment.reviewer.username} for {self.assignment.reviewee.username}"


class LecturerGrade(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    graded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "lecturer"},
    )
    grade = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # can save from 999.99 to -999.99
    comments = models.TextField()
    graded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grade for {self.review.assignment.reviewee.username} by {self.graded_by.username}"
