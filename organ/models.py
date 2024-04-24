from django.db import models
from staff.models import Participant

# Create your models here.
class Org(models.Model):

    name = models.CharField(u"机构名称", max_length=100, unique=True)
    description = models.TextField(verbose_name="描述", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='机构'
        verbose_name_plural='机构'


class Department(models.Model):
    name = models.CharField(max_length=30,verbose_name="名称",null=True)
    org = models.ForeignKey(Org, verbose_name='所属机构', null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Participant, verbose_name='部门负责人', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='部门'
        verbose_name_plural='部门'


class Team(models.Model):
    num = models.IntegerField(verbose_name='序号',null=True)
    name = models.CharField(max_length=30,verbose_name="名称")
    department = models.ForeignKey(Department,verbose_name='部门', null=True,on_delete=models.SET_NULL)
    description = models.TextField(verbose_name="描述",null=True)
    director = models.OneToOneField(Participant,verbose_name='团队负责人',null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Participant, verbose_name='团队成员', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='团队'
        verbose_name_plural='团队'