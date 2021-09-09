import json

def extract_route(response):
    response = response.split()[1]
    respon = response[1:]
    return respon

def read_f(path):
    extensoes = ["txt", "html", "css", "js"]
    path_str = str(path)
    file = path_str.split('.')[-1]
    if file in extensoes:
        with open(path, 'r') as text:
            return text.read().encode()
    else:
        with open(path, 'rb') as text:
            return text.read()

def load_data(path):
    with open("data/"+path, "r", encoding="utf-8") as file:
        file = json.load(file)
        return file
        
def load_template(path):
    with open("templates/"+path, "r", encoding="UTF-8") as file:
        content = file.read()
        file.close()
        return content

def build_response(body='', code=200, reason='OK', headers=''):
    response = "HTTP/1.1 "+str(code)+" "+reason
    if headers == '':
        response += "\n\n"+body
    else:
        response += "\n"+headers+"\n\n"
    
    return str(response).encode()

def read_file(path):
    with open(path, 'rb') as text:
        return text.read()