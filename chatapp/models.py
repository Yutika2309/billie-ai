from django.db import models

# Create your models here.
class ClassDetails(models.Model):
    GRADE = (
                ('eleventh', '11th'),
                ('twelfth', '12th')
            )

    SUBJECT = (
                ('physics','Physics'),
                ('math', 'Math'),
                ('history', 'History'),
                ('geography', 'Geography'),
                ('english', 'English'),
                ('computer science', 'Computer Science'),
                ('chemistry', 'Chemistry'),
                ('biology', 'Biology')
            )

class TopicDetails(models.Model):
    pass