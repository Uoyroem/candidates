import json

from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ImportForm
from .models import Document, Counterparty, Responsible


def import_data(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            try:
                data = json.load(json_file)
                for item in data:
                    counterparty, created = Counterparty.objects.get_or_create(bin=item.get('bin'),
                                                                               name=item.get('postavshik'))
                    otvzakup_id = int(item.get('otvzakup').split(" - ")[0])
                    otvzakup_last_name = item.get('otvzakup').split(" - ")[1].split(" ")[0]
                    otvzakup_first_name = item.get('otvzakup').split(" - ")[1].split(" ")[1]

                    otvzakup = Responsible.objects.filter(id=otvzakup_id).first()

                    if not otvzakup:
                        otvzakup = Responsible.objects.create(id=otvzakup_id, last_name=otvzakup_last_name,
                                                                          first_name=otvzakup_first_name)

                    Document.objects.create(
                        documentno=item.get('documentno'),
                        name=item.get('name'),
                        dateinvoiced=item.get('dateinvoiced'),
                        nscheta=item.get('nscheta'),
                        dogovor=item.get('dogovor'),
                        datascheta=item.get('datascheta'),
                        coment=item.get('coment'),
                        status=item.get('status'),
                        postavshik=counterparty,
                        bin=item.get('bin'),
                        accountno=item.get('accountno'),
                        bank=item.get('bank'),
                        totallines=item.get('totallines'),
                        payamt1c=item.get('payamt1c'),
                        notpayamt1c=item.get('notpayamt1c'),
                        otvzakup=otvzakup,
                        utverditel=item.get('utverditel'),
                        gruppa_proekrov=item.get('gruppa_proekrov'),
                        valyuta=item.get('valyuta'),
                        napravlenie=item.get('napravlenie'),
                        error_txt=item.get('error_txt'),
                        sumpaid=item.get('sumpaid'),
                        dname=item.get('dname'),
                        docstatus=item.get('docstatus'),
                        paydate1c=item.get('paydate1c'),
                        icname=item.get('icname'),
                        chname=item.get('chname'),
                        createdby=item.get('createdby'),
                        nomdocument1=item.get('nomdocument1'),
                        datadoc=item.get('datadoc'),
                        komment=item.get('komment'),
                        nepredorigdoc=item.get('nepredorigdoc'),
                        isattached=item.get('isattached'),
                        factnumdoc=item.get('factnumdoc'),
                        doc_number=item.get('doc_number'),
                        site=item.get('site'),
                        c_currency_id=item.get('c_currency_id'),
                        refundamt=item.get('refundamt'),
                        daterefund=item.get('daterefund'),
                        actdocno=item.get('actdocno'),
                        docserviceact=item.get('docserviceact'),
                        docdate=item.get('docdate'),
                        dateprocessed=item.get('dateprocessed'),
                        quantity=item.get('quantity'),
                        amount=item.get('amount'),
                        region=item.get('region'),
                        invoiceamount=item.get('invoiceamount'),
                        security_agreed=item.get('security_agreed'),
                        refundamtkzt=item.get('refundamtkzt'),
                        totallineskzt=item.get('totallineskzt'),
                        payamt1ckzt=item.get('payamt1ckzt'),
                        notpayamt1ckzt=item.get('notpayamt1ckzt'),
                        notpayamt1ckztcross=item.get('notpayamt1ckztcross'),
                        unclosedbalance=item.get('unclosedbalance'),
                        c_invoice_id=item.get('c_invoice_id'),
                    )
            except json.JSONDecodeError as e:
                return render(request, 'import_form.html', {'form': form, 'error': f'Ошибка JSON: {str(e)}'})

            return redirect('table_view')
        else:
            return render(request, 'import_form.html', {'form': form})

    else:
        form = ImportForm()

    return render(request, 'import_form.html', {'form': form})


def table_view(request):
    documents = Document.objects.all()
    print(documents.count())
    query = request.GET.get('q')

    if query:
        documents = documents.filter(
            Q(documentno__icontains=query) |
            Q(name__icontains=query) |
            Q(bin__icontains=query)
        )

    return render(request, 'table_view.html', {'documents': documents, 'query': query})
