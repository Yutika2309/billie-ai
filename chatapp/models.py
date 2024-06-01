from django.db import models

class ClassDetails(models.Model):
    """
        @description: Model for class related information
        @created by: Yutika Rege
    """
    GRADE = (
        ('eleventh', '11th'),
        ('twelfth', '12th')
    )

    SUBJECT = (
        ('physics', 'Physics', 'https://cbseacademic.nic.in/web_material/CurriculumMain23/SrSec/Physics_SrSec_2022-23.pdf'),
        ('chemistry', 'Chemistry', 'https://cbseacademic.nic.in/web_material/CurriculumMain23/SrSec/Chemistry_SrSec_2022-23.pdf'),
        ('biology', 'Biology', 'https://cbseacademic.nic.in/web_material/CurriculumMain25/SrSec/Biology_SrSec_2024-25.pdf')
    )
    
    RECOMMENDED_SRC = (
        ('creative ideas', 'Ideas'),
        ('experiments', 'Experiments')
    )

    grade = models.CharField(max_length=20, choices=GRADE, null=False, blank=False)
    subject = models.CharField(max_length=20, choices=[(sub[0], sub[1]) for sub in SUBJECT], null=False, blank=False)
    subject_url = models.URLField(null=False, blank=True)
    topic = models.CharField(max_length=200, null=False, blank=False)
    recommended_src = models.CharField(max_length=20, choices=RECOMMENDED_SRC, null=False, blank=False)
    chat_response = models.TextField(max_length=1000, null=False, blank=False)

    def save(self, *args, **kwargs):
        for sub in self.SUBJECT:
            if sub[0] == self.subject:
                self.subject_url = sub[2]
                break
        super(ClassDetails, self).save(*args, **kwargs)

    def __str__(self):
        return self.grade + "-" + self.subject + "-" + self.topic + "-" + self.recommended_src + "-" +self.chat_response[:50]
