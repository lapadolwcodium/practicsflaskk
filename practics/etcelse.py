import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')


'''
@app.route('/', methods=['POST'])
def test_get():
    text = request.form['text']
    processed_text = text.upper()
    return "<form methods=['POST']> " + \
           "<input type='text' name='text' value='' >" + \
           "<input type='submit' value='do submit'> " + \
           "<div> " + processed_text + "</div> " + \
           "</form>"s

'''


@app.route('/', methods=['POST'])
def test():
    processed_text = ''

    for foldername, subfolders, filenames in os.walk('./', topdown=False):  # os.listdir(os.path.expanduser('~/')):  #
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.jpg'):
                processed_text = processed_text + "  " + foldername + "/" + filename + "</br>"

                #    processed_text = processed_text + "  " + foldername + "  " + name + "</br>"
                # for name in subfolders:
                #    processed_text = processed_text + "  " + foldername + "  " + name + " -</br>"

    return processed_text
