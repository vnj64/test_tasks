from flask import Flask, render_template, request, make_response
import pandas as pd
from config import SECRET_KEY
from  db.init_db import init_db
from functions.functions import save_to_database, get_last_10_entries, transliterate

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    original = ""
    otc = ""
    if request.method == 'POST':
        if 'translate' in request.form:
            wrd = request.form.get("word")
            translit = transliterate(wrd)
            original = translit
            save_to_database(wrd, translit)
            return render_template('index.html', original=original)

        elif 'report' in request.form:
            data = get_last_10_entries()
            otc = data
            return render_template('index.html', otc=otc)

    return render_template('index.html')

@app.route('/report', methods=['GET'])
def report():
    data = get_last_10_entries()
    return render_template('report.html', data=data)

@app.route('/xls', methods=['GET'])
def xls():
    data = get_last_10_entries()
    df = pd.DataFrame(data, columns=['Text', 'Translit'])
    excel_file = df.to_excel('report.xlsx', index=False)
    with open('report.xlsx', 'rb') as file:
        data = file.read()
    response = make_response(data)
    response.headers['Content-Type'] = 'application/vnd.ms-excel'
    response.headers['Content-Disposition'] = 'attachment; filename=report.xlsx'
    return response


if __name__ == '__main__':
    init_db()
    app.run(debug=True)