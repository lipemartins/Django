from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Pergunta

# Create your views here.

def index(request):
    #return HttpResponse('Ola Mundo!!! Como vai voce?')
    lista_ultima_pergunta = Pergunta.objects.order_by('-dt_pub')[:5]
    #output = ','.join([p.txt_pergunta for p in lista_ultimas_perguntas])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    context = {'lista_ultima_pergunta': lista_ultima_pergunta, }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detalhe (request, pergunta_id):

    '''try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNoExist:
        raise Http404('Pergunta nao existe!')'''
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'polls/detalhe.html', {'pergunta': pergunta})

def resultados (request, pergunta_id):
    response = 'Voce esta olhando para o resultado das perguntas %s.'
    return  HttpResponse(response % pergunta_id)

def voto (request, pergunta_id):
    return HttpResponse('Voce votou na questao %s.' % pergunta_id)


