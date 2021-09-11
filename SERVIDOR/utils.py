import json

def extract_route(string):
    a = string.split(" ")
    b = a[1]
    c = b[1:]
    return c

def read_file(string):
    a = str(string)
    h = a.split(".")
    if h[1] == "txt" or h[1] == "html" or h[1] == "css" or h[1] == "js":
        with open(a, 'r') as c:
            return c.read()
    else:
        with open(a, 'rb') as d:
            return d.read()

def load_data(string):
    a = "data/"+string
    with open(a, "rt",encoding="utf-8") as txt:
        b = txt.read()
        c = json.loads(b)
        return c 

def load_template(filePath):
    with open("templates/"+filePath) as file:
        content = file.read()
        file.close()
        return content 

# def add_note(new_note):
#     notes=load_data('notes.json')
#     notes.append(new_note)
#     with open('data/notes.json', 'w') as note_new:
#         json.dump(notes, note_new)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        return('HTTP/1.1 '+str(code)+' '+reason+'\n\n'+body).encode()
    return('HTTP/1.1 '+str(code)+' '+reason+'\n'+headers+'\n\n'+body).encode()
