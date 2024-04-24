from django.db import models

# Create your models here.


# participant 项目参加人
class Participant(models.Model):
    PERSON_TYPE = (
        ("ZB", "在编"),
        ("LP", "临聘"),
        ("XS", "学生"),
        ("SW", "所外"),

    )

    name = models.CharField('姓名', max_length=20)
    phone = models.CharField('电话', max_length=20)
    person_type = models.CharField('人员类型', max_length=2, choices=PERSON_TYPE)
    organ = models.ForeignKey('organ.Org', verbose_name='所属机构', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)
