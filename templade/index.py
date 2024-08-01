from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            A = float(request.form['A'])
            B = float(request.form['B'])
            C = float(request.form['C'])
            
            if A > B and A > C:
                result = f"{A} es el mayor."
                result += f" {B} es el menor." if B < C else f" {C} es el menor."
            elif B > A and B > C:
                result = f"{B} es el mayor."
                result += f" {A} es el menor." if A < C else f" {C} es el menor."
            else:
                result = f"{C} es el mayor."
                result += f" {A} es el menor." if A < B else f" {B} es el menor."
        except ValueError:
            result = "Por favor, ingresa valores válidos."

    return render_template('DOCTYPE.HTML', result=result)

if __name__ == '__main__':
    app.run(debug=True)
