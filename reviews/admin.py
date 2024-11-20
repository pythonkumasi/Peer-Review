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


class ReviewAssignmentAdmin(admin.ModelAdmin):
    list_display = ["reviewer", "reviewee", "review_cycle", "assignment_date"]


admin.site.register(Review)
admin.site.register(ReviewAssignment, ReviewAssignmentAdmin)
admin.site.register(ReviewCycle, ReviewCycleAdmin)
admin.site.register(StudentEnrollment)
admin.site.register(LecturerGrade)
