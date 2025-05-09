from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def compare():
    result = None
    energy1 = energy2 = 0
    appliance1_name = appliance2_name = ''
    history = []

    if request.method == 'POST':
        appliance1_name = request.form['appliance1']
        power1 = float(request.form['power1'])
        hours1 = float(request.form['hours1'])
        days1 = float(request.form['days1'])

        appliance2_name = request.form['appliance2']
        power2 = float(request.form['power2'])
        hours2 = float(request.form['hours2'])
        days2 = float(request.form['days2'])

        energy1 = round((power1 * hours1 * days1) / 1000, 2)
        energy2 = round((power2 * hours2 * days2) / 1000, 2)

        if energy1 > energy2:
            result = f"{appliance1_name} consumes more energy than {appliance2_name}."
        elif energy2 > energy1:
            result = f"{appliance2_name} consumes more energy than {appliance1_name}."
        else:
            result = "Both appliances consume the same amount of energy."

        # Add details to the history
        history.append({
            'name1': appliance1_name,
            'energy1': energy1,
            'name2': appliance2_name,
            'energy2': energy2,
            'result': result
        })

    return render_template("index.html", result=result,
                           appliance1_name=appliance1_name,
                           appliance2_name=appliance2_name,
                           energy1=energy1,
                           energy2=energy2,
                           history=history)

if __name__ == '__main__':
    app.run(debug=True)
