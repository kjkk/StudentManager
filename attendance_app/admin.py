from django.contrib import admin
from attendance_app.models import total_attendance, Attendance

admin.site.register(total_attendance)
admin.site.register(Attendance)
