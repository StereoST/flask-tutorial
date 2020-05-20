#!python3

from flask import Flask, request, render_template
import BalanceSheet
import pandas as pd

app = Flask(__name__)

bs = pd.DataFrame()

@app.route('/', methods=['GET','POST']) #decorator to specify: if you visit the website at root, you will get this message
def bs_table():
    if request.method == 'POST' and 'stock_input' in request.form:
        stock = request.form.get('stock_input')
        global bs
        bs = BalanceSheet.bsimport(stock)
    return render_template('index.html',tables = [bs.to_html(classes='data', header="true")])

app.run()