from django.db import models


class Counteragent(models.Model):
    name = models.CharField(max_length=255)
    bin = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.name


class Responsible(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=1020)
    last_name = models.CharField(max_length=1020)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"


class Document(models.Model):
    documentno = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=1020)
    dateinvoiced = models.DateTimeField(null=True, blank=True)
    nscheta = models.CharField(max_length=20, null=True, blank=True)
    dogovor = models.CharField(max_length=20, null=True, blank=True)
    datascheta = models.DateTimeField(null=True, blank=True)
    coment = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=510, null=True, blank=True)
    postavshik = models.ForeignKey(Counteragent, on_delete=models.CASCADE, null=True, blank=True, related_name='documents')
    bin = models.CharField(max_length=12, null=True, blank=True)
    accountno = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=1020, null=True, blank=True)
    totallines = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    payamt1c = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notpayamt1c = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    otvzakup = models.CharField(max_length=50, null=True, blank=True)
    utverditel = models.ForeignKey(Responsible, on_delete=models.CASCADE, null=True, blank=True, related_name='utverditel_documents')
    gruppa_proekrov = models.CharField(max_length=1020, null=True, blank=True)
    valyuta = models.CharField(max_length=3, null=True, blank=True)
    napravlenie = models.CharField(max_length=1020, null=True, blank=True)
    error_txt = models.TextField(null=True, blank=True)
    sumpaid = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    dname = models.CharField(max_length=510, null=True, blank=True)
    docstatus = models.CharField(max_length=100, null=True, blank=True)
    paydate1c = models.DateField(null=True, blank=True)
    icname = models.CharField(max_length=510, null=True, blank=True)
    chname = models.CharField(max_length=1020, null=True, blank=True)
    createdby = models.CharField(max_length=1020, null=True, blank=True)
    nomdocument1 = models.CharField(max_length=510, null=True, blank=True)
    datadoc = models.DateField(null=True, blank=True)
    komment = models.TextField(null=True, blank=True)
    nepredorigdoc = models.CharField(max_length=100, null=True, blank=True)
    isattached = models.CharField(max_length=1, null=True, blank=True)
    factnumdoc = models.CharField(max_length=100, null=True, blank=True)
    doc_number = models.CharField(max_length=210, null=True, blank=True)
    site = models.CharField(max_length=510, null=True, blank=True)
    c_currency_id = models.IntegerField(null=True, blank=True)
    refundamt = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    daterefund = models.DateField(null=True, blank=True)
    actdocno = models.CharField(max_length=210, null=True, blank=True)
    docserviceact = models.CharField(max_length=210, null=True, blank=True)
    docdate = models.DateTimeField(null=True, blank=True)
    dateprocessed = models.DateTimeField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    region = models.CharField(max_length=510, null=True, blank=True)
    invoiceamount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    security_agreed = models.CharField(max_length=510, null=True, blank=True)
    refundamtkzt = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    totallineskzt = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    payamt1ckzt = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notpayamt1ckzt = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notpayamt1ckztcross = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    unclosedbalance = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    c_invoice_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.documentno