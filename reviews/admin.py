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


class LecturerGradeAdmin(admin.ModelAdmin):
    list_display = [
        "get_review_cycle_name",
        "get_reviewee_student_name",
        "graded_by",
        "grade",
    ]

    def get_review_cycle_name(self, obj):
        return obj.get_recycle_name()

    def get_reviewee_student_name(self, obj):
        return obj.get_reviewee_student_name()

    get_review_cycle_name.short_description = "Review Cycle Name"
    get_reviewee_student_name.short_description = "Reviewee Student"


admin.site.register(Review)
admin.site.register(ReviewAssignment, ReviewAssignmentAdmin)
admin.site.register(ReviewCycle, ReviewCycleAdmin)
admin.site.register(StudentEnrollment)
admin.site.register(LecturerGrade, LecturerGradeAdmin)
