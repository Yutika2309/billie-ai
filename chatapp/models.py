from django.db import models

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
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology')
    )
    
    grade = models.CharField(max_length=20, choices=GRADE, null=False, blank=False)
    subject = models.CharField(max_length=20, choices=SUBJECT, null=False, blank=False)
    query_text = models.CharField(null=False, blank=False)
    chat_response = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.grade + "-" + self.subject + "-" + self.query_text + "-" + self.chat_response[:50]

