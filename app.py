from flask import Flask, redirect, render_template, request
import math


app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")

#TEMPERATURA
@app.route("/celsiusfa/")
def celsiusfa():
    return render_template('celsiusfa.html', titulo='')

@app.route("/celsiusfadata/", methods=['POST'])
def celsiusfadata():
    x = float(request.form['x'])
    y = str(x * 1.8 + 32)
    return render_template('celsiusfadata.html', y=y)

@app.route("/celsiuske/")
def celsiuske():
    return render_template('celsiuske.html', titulo='')

@app.route("/celsiuskedata/", methods=['POST'])
def celsiuskedata():
    x = float(request.form['x'])
    y = str(x + 273.15)
    return render_template('celsiuskedata.html', y=y)

@app.route("/kelvince/")
def kelvince():
    return render_template('kelvince.html', titulo='')

@app.route("/kelvincedata/", methods=['POST'])
def kelvincedata():
    x = float(request.form['x'])
    y = str(x + 273.15)
    return render_template('kelvincedata.html', y=y)

@app.route("/kelvinfa/")
def kelvinfa():
    return render_template('kelvinfa.html', titulo='')

@app.route("/kelvinfadata/", methods=['POST'])
def kelvinfadata():
    x = float(request.form['x'])
    y = str((x + 273.15) * 1.8 + 32)
    return render_template('kelvinfadata.html', y=y)

@app.route("/farenheitce/")
def farenheitce():
    return render_template('farenheitce.html', titulo='')

@app.route("/farenheitcedata/", methods=['POST'])
def farenheitcedata():
    x = float(request.form['x'])
    y = str((x - 32) * 5/9)
    return render_template('farenheitcedata.html', y=y)

@app.route("/farenheitke/")
def farenheitke():
    return render_template('farenheitke.html', titulo='')

@app.route("/farenheitkedata/", methods=['POST'])
def farenheitkedata():
    x = float(request.form['x'])
    y = str((x - 32) * 5/9)
    return render_template('farenheitkedata.html', y=y)

#VELOCIDADE
@app.route("/kmhms/")
def kmhms():
    return render_template('kmhms.html', titulo='')

@app.route("/kmhmsdata/", methods=['POST'])
def kmhmsdata():
    x = float(request.form['x'])
    y = str(x / 3.6)
    return render_template('kmhmsdata.html', y=y)

#kmhkms
@app.route("/kmhkms/")
def kmhkms():
    return render_template('kmhkms.html', titulo='')

@app.route("/kmhkmsdata/", methods=['POST'])
def kmhkmsdata():
    x = float(request.form['x'])
    y = str(x / 3600)
    return render_template('kmhkmsdata.html', y=y)

#mskmh
@app.route("/mskmh/")
def mskmh():
    return render_template('mskmh.html', titulo='')

@app.route("/mskmhdata/", methods=['POST'])
def mskmhdata():
    x = float(request.form['x'])
    y = str(x * 3.6)
    return render_template('mskmhdata.html', y=y)

#mskms
@app.route("/mskms/")
def mskms():
    return render_template('mskms.html', titulo='')

@app.route("/mskmsdata/", methods=['POST'])
def mskmsdata():
    x = float(request.form['x'])
    y = str(x / 1000)
    return render_template('mskmsdata.html', y=y)

#kmskmh
@app.route("/kmskmh/")
def kmskmh():
    return render_template('kmskmh.html', titulo='')

@app.route("/kmskmhdata/", methods=['POST'])
def kmskmhdata():
    x = float(request.form['x'])
    y = str(x * 3600)
    return render_template('kmskmhdata.html', y=y)

#kmsms
@app.route("/kmsms/")
def kmsms():
    return render_template('kmsms.html', titulo='')

@app.route("/kmsmsdata/", methods=['POST'])
def kmsmsdata():
    x = float(request.form['x'])
    y = str(x * 1000)
    return render_template('kmsmsdata.html', y=y)

#TEMPO
@app.route("/horamin/")
def horamin():
    return render_template('horamin.html', titulo='')

@app.route("/horamindata/", methods=['POST'])
def horamindata():
    x = float(request.form['x'])
    y = str(x * 60)
    return render_template('horamindata.html', y=y)

@app.route("/horaseg/")
def horaseg():
    return render_template('horaseg.html', titulo='')

@app.route("/horasegdata/", methods=['POST'])
def horasegdata():
    x = float(request.form['x'])
    y = str(x * 3600)
    return render_template('horasegdata.html', y=y)

@app.route("/minutoh/")
def minutoh():
    return render_template('minutoh.html', titulo='')

@app.route("/minutohdata/", methods=['POST'])
def minutohdata():
    x = float(request.form['x'])
    y = str(x / 60)
    return render_template('minutohdata.html', y=y)

@app.route("/minutoseg/")
def minutoseg():
    return render_template('minutoseg.html', titulo='')

@app.route("/minutosegdata/", methods=['POST'])
def minutosegdata():
    x = float(request.form['x'])
    y = str(x * 60)
    return render_template('minutosegdata.html', y=y)

@app.route("/segundoh/")
def segundoh():
    return render_template('segundoh.html', titulo='')

@app.route("/segundohdata/", methods=['POST'])
def segundohdata():
    x = float(request.form['x'])
    y = str(x / 3600)
    return render_template('segundohdata.html', y=y)

@app.route("/segundomin/")
def segundomin():
    return render_template('segundomin.html', titulo='')

@app.route("/segundomindata/", methods=['POST'])
def segundomindata():
    x = float(request.form['x'])
    y = str(x / 60)
    return render_template('segundomindata.html', y=y)

if __name__ == "__main__":
    app.run(debug=True)





