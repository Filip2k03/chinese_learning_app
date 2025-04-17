from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
