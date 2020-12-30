from flask import Flask
from flask import request
from markupsafe import escape
import requests, html
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return 'Type in "/api?text=" and then some text.<br>You can also change the dialect to American by adding "&dialect=am" after the text.'

@app.route('/api')
def toipa():
    try:
        text = request.form['text']
    except:
        try:
            text = request.args.get('text', '')
        except:
            return 'Type in "/api?text=" and then some text.<br>You can also change the dialect to American by adding "&dialect=am" after the text.'
    try:
        dialect = request.form['dialect']
    except:
        try:
            dialect = request.args.get('dialect', '')
        except KeyError:
            dialect = 'br'
    try:
        prebracket = request.form['prebracket']
    except:
        try:
            prebracket = request.args.get('prebracket', '')
        except KeyError:
            prebracket = ''
    try:
        postbracket = request.form['postbracket']
    except:
        try:
            postbracket = request.args.get('postbracket', '')
        except KeyError:
            postbracket = ''
    data = {"text_to_transcribe": text, "submit": "", "output_dialect": dialect, "output_style": "only_tr", "preBracket": prebracket, "postBracket": postbracket, "speech_support": "1"}
    response = requests.post("https://tophonetics.com/", data=data).text
    soup = BeautifulSoup(response, features="html5lib")
    tag = str(soup.find(id='transcr_output')).replace('<br/>','\n')
    result = ''.join(BeautifulSoup(tag, features="html5lib").findAll(text=True))
    return html.unescape(result).strip().replace(u'\xa0', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
