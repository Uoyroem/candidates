from django.db import models


class Responsible(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        app_label = 'task'

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'


class Counterparty(models.Model):
    bin = models.CharField(max_length=12, unique=True, null=True)
    name = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'task'


class Document(models.Model):
    documentno = models.TextField()
    name = models.TextField()
    dateinvoiced = models.TextField(null=True)
    nscheta = models.TextField(null=True)
    dogovor = models.TextField(null=True)
    datascheta = models.TextField(null=True)
    coment = models.TextField(null=True)
    status = models.TextField(null=True)
    postavshik = models.ForeignKey(Counterparty, on_delete=models.PROTECT)
    bin = models.TextField(null=True)
    accountno = models.TextField(null=True)
    bank = models.TextField(null=True)
    totallines = models.TextField(null=True)
    payamt1c = models.TextField(null=True)
    notpayamt1c = models.TextField(null=True)
    otvzakup = models.ForeignKey(Responsible, on_delete=models.PROTECT, related_name='purchases')
    utverditel = models.TextField(null=True)
    gruppa_proekrov = models.TextField(null=True)
    valyuta = models.TextField(null=True)
    napravlenie = models.TextField(null=True)
    error_txt = models.TextField(null=True)
    sumpaid = models.TextField(null=True)
    dname = models.TextField(null=True)
    docstatus = models.TextField(null=True)
    paydate1c = models.TextField(null=True)
    icname = models.TextField(null=True)
    chname = models.TextField(null=True)
    createdby = models.TextField(null=True)
    nomdocument1 = models.TextField(null=True, blank=True)
    datadoc = models.TextField(null=True, blank=True)
    komment = models.TextField(null=True, blank=True)
    nepredorigdoc = models.TextField(null=True)
    isattached = models.TextField(null=True)
    factnumdoc = models.TextField(null=True)
    doc_number = models.TextField(null=True)
    site = models.TextField(null=True)
    c_currency_id = models.TextField(null=True)
    refundamt = models.TextField(null=True)
    daterefund = models.TextField(null=True, blank=True)
    actdocno = models.TextField(null=True)
    docserviceact = models.TextField(null=True)
    docdate = models.TextField(null=True)
    dateprocessed = models.TextField(null=True)
    quantity = models.TextField(null=True)
    amount = models.TextField(null=True)
    region = models.TextField(null=True)
    invoiceamount = models.TextField(null=True)
    security_agreed = models.TextField(null=True)
    refundamtkzt = models.TextField(null=True)
    totallineskzt = models.TextField(null=True)
    payamt1ckzt = models.TextField(null=True)
    notpayamt1ckzt = models.TextField(null=True)
    notpayamt1ckztcross = models.TextField(null=True)
    unclosedbalance = models.TextField(null=True)
    c_invoice_id = models.IntegerField(null=True)

    class Meta:
        app_label = 'task'
