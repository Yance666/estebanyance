from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def inicio():
    # Renderiza la plantilla "hola.html" con el nombre "Luis"
    return render_template("hola.html", nombre="Luis")

if _name_ == "_main_":
    app.run(debug=Tru