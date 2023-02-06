from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    # company_po = models.ForeignKey(head_company.HeadCompany, po_company.POCompany, on_delete=Pro)
    # company_head = models.ForeignKey
