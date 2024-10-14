from django.db import models

class FormData(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)

    # Education
    college_name = models.CharField(max_length=255)
    year_of_study = models.CharField(max_length=20)

    # Academic Progress
    academic_progress = models.JSONField(default=list)  # List of dictionaries

    # Results
    result = models.CharField(max_length=50)

    # Lifestyle
    exercise_time = models.CharField(max_length=50)
    sleep_time = models.CharField(max_length=50)
    food = models.CharField(max_length=100)

    # Learning
    learned_from_friend = models.TextField()
    extra_activity = models.TextField()

    # Requests
    req_for_3_months = models.JSONField(default=list)  # List of dictionaries

    # Other Fields
    book_read = models.TextField()
    ladder_status = models.CharField(max_length=50)
    book_review = models.TextField()
    essay = models.TextField()
    action_for_next_month = models.TextField()
    difficulties = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
