from django.db import models

# Create your models here.
class ClassDetails(models.Model):

    """
        @description: Model for basic class related information
        @created by: Yutika Rege
    """

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

    teacher_name = models.CharField(max_length=120, null=False, blank=False)
    grade = models.CharField(choices=GRADE, null=False, blank=False)
    subject = models.CharField(choices=SUBJECT, null=False, blank=False)

    def __str__(self):
        return self.grade + "-" + self.subject


# class Syllabus(models.Model):
#     """
#         @description: Model for topics for a subject for a certain grade
#         @created by: Yutika Rege
#     """
     
#     grade = models.ForeignKey(ClassDetails, on_delete=models.CASCADE, null=True, blank=True)
#     subject = models.ForeignKey(ClassDetails, on_delete=models.CASCADE, null=True, blank=True)
#     syllabus = model
    
#     def __str__(self):
