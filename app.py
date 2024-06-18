from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        product_name = request.form['product_name']
        cursor.execute("SELECT * FROM products WHERE name LIKE?", ('%' + product_name + '%',))
        products = cursor.fetchall()
        conn.close()
        return render_template('index.html', products=products, search_query=product_name)
    conn.close()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host= '192.168.1.3',port=9000,debug=True, threaded=True)