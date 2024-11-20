from django.db import models
from courses.models import Course
from django.conf import settings
from django.utils import timezone


# Create your models here.


class ReviewCycle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    # TODO: add a logic that makes is_active true when start_date - today is less than 1.

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
        return f"{self.reviewer.username} is reviewing {self.reviewee.username} on {self.review_cycle}"


class Review(models.Model):
    assignment = models.ForeignKey(ReviewAssignment, on_delete=models.CASCADE)
    review_text = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assignment.reviewer.username} reviewed for {self.assignment.reviewee.username} on {self.assignment.review_cycle.name}"


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

    def get_recycle_name(self):
        return self.review.assignment.review_cycle.name

    def get_reviewee_student_name(self):
        """
        Returns the student object who the assignment was assigned to.
        This method retrieves the reviewee associated with the current review assignment.
        """
        return self.review.assignment.reviewee

    def __str__(self):
        return f"Grade for {self.review.assignment.reviewee.username} by {self.graded_by.username}"
