from django.db import models
from django.contrib.auth.models import User

class IssueGameTicket(models.Model):
    qa_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qa_testers')
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game_issues')
    issue_title = models.CharField(max_length=190)
    bug_description = models.CharField(max_length=3190)
    expected_result = models.CharField(max_length=13490)
    repeat_step = models.CharField(max_length=1990)
    file_proof = models.FileField(upload_to='uploads/') 