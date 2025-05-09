from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # or any available LLM model
        prompt=prompt,
        max_tokens=150  # or adjust based on your need
    )
    return response.choices[0].text.strip()


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

@app.route('/generate-summary', methods=['POST'])
def generate_summary():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'summary': 'No prompt provided.'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes energy consumption in simple terms."},
                {"role": "user", "content": prompt}
            ]
        )
        summary = response['choices'][0]['message']['content']
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'summary': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
