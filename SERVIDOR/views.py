from utils import load_data, load_template, build_response, extract_route, read_file
import urllib

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
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
        #add_note(params)
        return build_response(body=load_template('index.html').format(notes=notes),code=303, reason='See Other', headers='Location: /')
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)
    return build_response(body = load_template('index.html').format(notes=notes))

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...