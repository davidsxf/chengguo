from django.db import models
import datetime
from organ.models import Org, Participant
from django.db.models import Count

# Create your models here.


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year

class Project(models.Model):

    PROJECT_TYPE = (
        ("JSFW", "技术服务"),
        ("JSZX", "技术咨询"),   
        ("JSKF", "技术开发（合作）"),
        ("JSKS", "技术开发（委托）"),
        ("JSZR", "技术转让（转让）"),
        ("JSXK", "技术转让（许可）"),
        ("OTHER", "其他"),
    )

    PRPJECT_STATUS = (
        ("Ongoing", "在研"),
        ("Conclusion", "结题"),
    )

    num = models.CharField('项目编号',max_length=100,blank=True, null=True)
    finance_num = models.CharField('财务编号',max_length=100,blank=True, null=True)
    name = models.CharField('项目名称',max_length=100,unique=True)
    project_type = models.CharField('项目类别',max_length=30,choices=PROJECT_TYPE,blank=True, null=True)
    sign_date = models.DateField('签约日期',default=datetime.date.today,blank=True, null=True)
    start_date = models.DateField('开始日期',default=datetime.date.today,blank=True, null=True)
    end_date = models.DateField('计划结项日期',blank=True, null=True)
    authorize_units = models.ForeignKey(Org,verbose_name='委托单位',on_delete=models.SET_NULL,blank=True,null=True)
    source = models.CharField('资金来源',max_length=100,blank=True, null=True)
    director = models.ForeignKey(Participant, verbose_name='项目负责人', blank=True,
                                 null=True, on_delete=models.SET_NULL, related_name='directors')
    contract_fund = models.DecimalField('合同经费(万元)',max_digits=7, decimal_places=2,default=0)

    
    participant = models.ManyToManyField(Participant,verbose_name='项目参与人',through='Participantion',related_name='participants')
    enter_year = models.IntegerField('登记年度',default=current_year,blank=True, null=True)
    enter_info = models.CharField('登记情况',max_length=50,blank=True, null=True)
    end_info = models.CharField('结项情况',max_length=50,blank=True, null=True)
    doc_transfer = models.CharField('档案移交情况',max_length=50,blank=True, null=True)
    context = models.TextField('备注',blank=True, null=True)


    achievement_info = models.CharField('成果简介',max_length=50,blank=True, null=True)
    
    status = models.CharField('项目状态',max_length=10,choices=PRPJECT_STATUS,default='Ongoing',blank=True, null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'
        


class Participantion(models.Model):

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name='项目')

    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, verbose_name='项目参与人')
    order = models.IntegerField('项目参与顺序', default=0)

    def save(self, *args, **kwargs):
        '''
        自动设置项目参与顺序
        '''
        item_count = Participantion.objects.filter(project=self.project).count()
        self.order = item_count + 1
        super(Participantion, self).save(*args, **kwargs)

    def __str__(self):
        return "项目： {}, 项目参与人： {},项目参与顺序： {}".format(self.project.name, self.participant.name, self.order)

    class Meta:
        verbose_name = '项目参与'
        verbose_name_plural = '项目参与'
        unique_together = [['project', 'participant']]


class FundState(models.Model):
    num = models.IntegerField('序号')
    project = models.ForeignKey(Project,verbose_name='项目',on_delete=models.CASCADE)
    in_date = models.DateField('到账日期',default=datetime.date.today)
    in_fund = models.DecimalField('到账经费(万元)',max_digits=7, decimal_places=2)
    # claim = models.BooleanField('是否认领',default=False).
    tc_fund = models.DecimalField('统筹经费(万元)',max_digits=7, decimal_places=2)
    claim_date = models.DateField('认领日期',blank=True, null=True,default=datetime.date.today)

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name='经费到账统筹'
        verbose_name_plural='经费到账统筹'

    

class Performance(models.Model):
    num = models.IntegerField('序号')
    project = models.ForeignKey(Project,verbose_name='项目',on_delete=models.CASCADE)
    date = models.DateField('提取绩效日期',default=datetime.date.today)
    fund = models.DecimalField('提取绩效(万元)',max_digits=7, decimal_places=2)

    class Meta:
        verbose_name='提取绩效'        
        verbose_name_plural='提取绩效'