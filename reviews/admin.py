from django.contrib import admin
from .models import (
    ReviewCycle,
    StudentEnrollment,
    ReviewAssignment,
    Review,
    LecturerGrade,
)


# Register your models here.
class ReviewCycleAdmin(admin.ModelAdmin):
    list_display = ["course", "name", "start_date", "end_date"]


admin.site.register(Review)
admin.site.register(ReviewAssignment)
admin.site.register(ReviewCycle, ReviewCycleAdmin)
admin.site.register(StudentEnrollment)
admin.site.register(LecturerGrade)
