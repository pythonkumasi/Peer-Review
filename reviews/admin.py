from django.contrib import admin
from .models import (
    ReviewCycle,
    StudentEnrollment,
    ReviewAssignment,
    Review,
    LecturerGrade,
)

# Register your models here.
admin.site.register(Review)
admin.site.register(ReviewAssignment)
admin.site.register(ReviewCycle)
admin.site.register(StudentEnrollment)
