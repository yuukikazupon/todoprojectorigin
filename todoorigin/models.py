from django.db import models

# PRIORITY = [["danger","high"],["success","normal"],["primary","low"]]
class TodoModel(models.Model) :
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
            max_length=100,
            # choices = PRIORITY
            choices = [["danger","high"],["success","normal"],["primary","low"]]

    )
    duedate = models.DateField()

    def __str__(self) :
        return self.title
