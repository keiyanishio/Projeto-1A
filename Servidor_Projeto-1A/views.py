import urllib
from utils import load_data, load_template, build_response
import json
from database import Database, Note


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    banco = Database('banco')
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        if len(partes) < 2 or len(partes[1].strip())==0:
            return -1
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")

        banco.add(Note(title=params['titulo'], content=params['detalhes']))

        
        note_template = load_template('components/note.html')
        notes_li=[]
        for dados in banco.get_all():
            notas=note_template.format(title=dados.title, details=dados.content, id=dados.id)
            notes_li.append(notas)
        notes = '\n'.join(notes_li)
        
        
        return build_response(code=303, reason='See Other', headers='Location: /')+load_template('index.html').format(notes=notes).encode()
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    
    notes_li=[]
    for dados in banco.get_all():
        notas=note_template.format(title=dados.title, details=dados.content, id=dados.id)
        notes_li.append(notas)
    notes = '\n'.join(notes_li)
    
    

    return build_response()+load_template('index.html').format(notes=notes).encode()

def deletar(request):
    banco = Database('banco')
    request.startswith('deletar')
    codigo = request.split("/")
    num_1 = codigo[2]
    num_2 = int(num_1[0]+num_1[1])
    banco.delete(num_2)

    note_template = load_template('components/note.html')
    notes_li=[]
    for dados in banco.get_all():
        notas=note_template.format(title=dados.title, details=dados.content, id=dados.id)
        notes_li.append(notas)
    notes = '\n'.join(notes_li)
    


    return build_response(code=303, reason='See Other', headers='Location: /')+load_template('index.html').format(notes=notes).encode()


    