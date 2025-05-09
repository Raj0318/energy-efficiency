from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    energy1 = None
    energy2 = None
    appliance1_name = None
    appliance2_name = None
    history = []

    if request.method == "POST":
        # Get appliance data from the form
        appliance1_name = request.form["appliance1"]
        power1 = float(request.form["power1"])
        hours1 = float(request.form["hours1"])
        days1 = float(request.form["days1"])

        appliance2_name = request.form["appliance2"]
        power2 = float(request.form["power2"])
        hours2 = float(request.form["hours2"])
        days2 = float(request.form["days2"])

        # Calculate energy consumption in kWh for both appliances
        energy1 = (power1 * hours1 * days1) / 1000  # Convert watts to kWh
        energy2 = (power2 * hours2 * days2) / 1000  # Convert watts to kWh

        # Create the result message
        result = f"{appliance1_name} uses {energy1:.2f} kWh per week and {appliance2_name} uses {energy2:.2f} kWh per week."

        # Add comparison to history
        history.append({
            'appliance1': appliance1_name,
            'appliance2': appliance2_name,
            'result': result,
            'energy1': energy1,
            'energy2': energy2
        })

    return render_template("index.html", result=result, energy1=energy1, energy2=energy2, appliance1_name=appliance1_name, appliance2_name=appliance2_name, history=history)

if __name__ == "__main__":
    app.run(debug=True)
