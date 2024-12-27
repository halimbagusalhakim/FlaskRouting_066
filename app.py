from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Ambil data dari form
    nama = request.form.get('nama')
    kelas = request.form.get('kelas')
    nim = request.form.get('nim')
    
    # Render hasil ke template HTML
    return render_template('result.html', nama=nama, kelas=kelas, nim=nim)

if __name__ == '__main__':
    app.run(debug=True)
