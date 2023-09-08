from django.db import models
from django.contrib.auth.models import User

class IssueGameTicket(models.Model):
    qa = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qa_testers')
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game_issues')
    issue_title = models.CharField(max_length=75)
    bug_description = models.TextField()
    expected_result = models.TextField()
    repeat_step = models.TextField()


# class ProofMediaGameIssue(models.Model):
#     qa_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qa_testers')
#     game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game_issues')
#     file_proof = models.FileField(upload_to='uploads/')