from django.db import models
from django.utils import timezone
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # skills_used = models.ManyToManyField(Skill)
    project_desc = models.TextField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.name

    # def add_skills(self, skill):
        # self.skills_used.add(skill)
        # self.save()


class ProjectTeam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # leader = models.ForeignKey(User, on_delete=models.CASCADE)
    # current_members = models.ManyToManyField(User)
    vacancies = models.PositiveSmallIntegerField(default=3)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # def add_member(self, member):
        # self.current_members.add(member)
        # self.save()


class ProjectTeamRequest(models.Model):
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    create_date = models.DateField(default=timezone.now)
    status_choices = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('R', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=status_choices, default='P')

    def __str__(self):
        return self.sender.username + ' --> ' + self.team.name

    def accept(self):
        self.status = 'A'
        self.save()

    def reject(self):
        self.status = 'R'
        self.save()


class Skill(models.Model):
    skill = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.skill


class Hackathon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon_desc = models.TextField(max_length=500)
    link = models.URLField()
    hackathon_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class HackathonTeam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # leader = models.ForeignKey(User, on_delete=models.CASCADE)
    # current_members = models.ManyToManyField(User)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    vacancies = models.PositiveSmallIntegerField(default=3)
    closed = models.BooleanField(default=False)
    cut_off_date = models.DateField(default=timezone.now)
    skills_required = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


class HackathonTeamRequest(models.Model):
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(HackathonTeam, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    skills = models.ManyToManyField(Skill)
    create_date = models.DateField(default=timezone.now)
    status_choices = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('R', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=status_choices, default='P')
