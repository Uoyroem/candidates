import json
from json import JSONDecodeError
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import JSONImportForm
from .models import Document, Counteragent, Responsible


def upload_json(request):
    if request.method == 'POST':
        form = JSONImportForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                json_file = request.FILES['json_file']
                data = json.load(json_file)

                for item in data:
                    kontragent, _ = Counteragent.objects.get_or_create(
                        bin=item.get('bin'),
                        defaults={
                            'name': item.get('postavshik')
                        }
                    )
                    utverditel_data = item.get('utverditel')
                    if utverditel_data:
                        otvet_id, otvet_name = utverditel_data.split(' - ')
                    otvetchik, _ = Responsible.objects.get_or_create(
                        id=otvet_id,
                        defaults={
                            'first_name': otvet_name.split(' ')[1],
                            'last_name': otvet_name.split(' ')[0],
                        }
                    )
                    Document.objects.create(
                        documentno=item.get('documentno'),
                        name=item.get('name'),
                        dateinvoiced=item.get('dateinvoiced'),
                        nscheta=item.get('nscheta', ''),
                        dogovor=item.get('dogovor', ''),
                        datascheta=item.get('datascheta', ''),
                        coment=item.get('coment', ''),
                        status=item.get('status', ''),
                        postavshik=kontragent,
                        utverditel=otvetchik,
                        bin=item.get('bin'),
                        accountno=item.get('accountno', ''),
                        bank=item.get('bank', ''),
                        totallines=item.get('totallines', 0),
                        payamt1c=item.get('payamt1c', 0),
                        notpayamt1c=item.get('notpayamt1c', 0),
                        otvzakup=item.get('otvzakup', ''),
                        gruppa_proekrov=item.get('gruppa_proekrov', ''),
                        valyuta=item.get('valyuta', ''),
                        napravlenie=item.get('napravlenie', ''),
                        error_txt=item.get('error_txt', ''),
                        sumpaid=item.get('sumpaid', 0),
                        dname=item.get('dname', ''),
                        docstatus=item.get('docstatus', ''),
                        paydate1c=item.get('paydate1c', ''),
                        icname=item.get('icname', ''),
                        chname=item.get('chname', ''),
                        createdby=item.get('createdby', ''),
                        nomdocument1=item.get('nomdocument1', ''),
                        datadoc=item.get('datadoc', ''),
                        komment=item.get('komment', ''),
                        nepredorigdoc=item.get('nepredorigdoc', ''),
                        isattached=item.get('isattached', ''),
                        factnumdoc=item.get('factnumdoc', ''),
                        doc_number=item.get('doc_number', ''),
                        site=item.get('site', ''),
                        c_currency_id=item.get('c_currency_id', 0),
                        refundamt=item.get('refundamt', 0),
                        daterefund=item.get('daterefund', ''),
                        actdocno=item.get('actdocno', ''),
                        docserviceact=item.get('docserviceact', ''),
                        docdate=item.get('docdate', ''),
                        dateprocessed=item.get('dateprocessed', ''),
                        quantity=item.get('quantity', 0),
                        amount=item.get('amount', 0),
                        region=item.get('region', ''),
                        invoiceamount=item.get('invoiceamount', 0),
                        security_agreed=item.get('security_agreed', ''),
                        refundamtkzt=item.get('refundamtkzt', 0),
                        totallineskzt=item.get('totallineskzt', 0),
                        payamt1ckzt=item.get('payamt1ckzt', 0),
                        notpayamt1ckzt=item.get('notpayamt1ckzt', 0),
                        notpayamt1ckztcross=item.get('notpayamt1ckztcross', 0),
                        unclosedbalance=item.get('unclosedbalance', 0),
                        c_invoice_id=item.get('c_invoice_id', 0)

                    )
                return redirect('success_view')

            except JSONDecodeError:
                messages.error(request, 'Ошибка: загруженный файл не является допустимым JSON файлом.')
            except (AttributeError, KeyError) as e:
                messages.error(request, f'Ошибка обработки данных. Проверьте ваш JSON файл!')
            except Exception as e:
                messages.error(request, f'Неожиданная ошибка: {str(e)}')
    else:
        form = JSONImportForm()
    return render(request, 'jsonhandler/upload-form.html', {'form': form})


def success_view(request):
    query = request.GET.get('query', '')
    documents = Document.objects.all().select_related('postavshik', 'utverditel')

    if query:
        documents = documents.filter(name__icontains=query)

    grouped_documents = {}
    for doc in documents:
        kontragent_bin = doc.postavshik.bin
        otvetstvenny_id = doc.utverditel.id
        if kontragent_bin not in grouped_documents:
            grouped_documents[kontragent_bin] = {}
        if otvetstvenny_id not in grouped_documents[kontragent_bin]:
            grouped_documents[kontragent_bin][otvetstvenny_id] = []
        grouped_documents[kontragent_bin][otvetstvenny_id].append(doc)

    return render(request, 'jsonhandler/success_page.html', {'grouped_documents': grouped_documents, 'query': query})


