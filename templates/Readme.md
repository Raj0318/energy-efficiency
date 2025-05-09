🔌 Appliance Energy Consumption Comparator with AI Summary
This web app helps users compare the annual energy consumption of two appliances and also provides an AI-generated summary for better insights.

<!-- Optional: You can add a screenshot of your app -->

✨ Features
🧮 Calculates energy usage of two electrical appliances

🆚 Compares which appliance consumes more energy

🤖 Generates a smart AI summary using OpenAI API

🕶️ Toggle between Light and Dark Mode

💾 Service Worker support for offline usage (PWA-ready)

📜 History log of previous comparisons

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

AI Integration: OpenAI API (e.g., text-davinci-003)

Deployment Ready: PWA support, manifest, and service worker

🚀 Getting Started
Prerequisites
Python 3.x

OpenAI API Key

Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/energy-comparison-ai.git
cd energy-comparison-ai
Create a virtual environment and activate it

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your OpenAI API key

Add this to your terminal or create a .env file:

bash
Copy
Edit
export OPENAI_API_KEY="your-api-key-here"
Run the app

bash
Copy
Edit
python app.py
Visit the app

Open your browser and go to: http://127.0.0.1:5000

📂 Project Structure
pgsql
Copy
Edit
.
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── CSS/
│       └── style.css
├── manifest.json
├── service-worker.js
└── README.md
🤖 Using the AI Summary Feature
The app sends a custom prompt based on your appliance details to OpenAI and gets a natural language summary. Make sure your API key has enough quota!

🧠 Example Prompt to OpenAI
text
Copy
Edit
Compare energy consumption: Fan uses 70W for 8 hours over 300 days. AC uses 1500W for 4 hours over 180 days. Provide a simple summary.
📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
OpenAI

Flask

Google Fonts, PWA concepts, and developer community

