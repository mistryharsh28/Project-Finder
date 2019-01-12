from django.db import models
from datetime import date


class Skill(models.Model):
    skill = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.skill


class Hackathon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon_desc = models.TextField(max_length=500)
    link = models.URLField()
    hackathon_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class HackathonTeam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # leader = models.ForeignKey(User, on_delete=models.CASCADE)
    # current_members = models.ManyToManyField(User)
    hackathon = models.OneToOneField(Hackathon, on_delete=models.CASCADE)
    vacancies = models.PositiveSmallIntegerField(default=3)
    closed = models.BooleanField(default=False)
    cut_off_date = models.DateField(default=date.today)
    skills_required = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


class HackathonTeamRequest(models.Model):
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(HackathonTeam, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    skills = models.ManyToManyField(Skill)
    create_date = models.DateField(default=date.today)
    status_choices = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('R', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=status_choices, default='P')
