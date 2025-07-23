
# 🤖 LLM Role-Based Assistant API

A FastAPI-based backend service that lets users interact with an LLM using different role personas like Developer, Manager, Analyst, and Student.

---

## 📦 Installation

```bash
git clone https://github.com/Ariba-Sameen-Ansari/llm-role-based-assistant.git
cd llm-role-based-assistant
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux

pip install -r requirements.txt
uvicorn main:app --reload

```

🔐 Environment Setup
Create a .env file in the project root.

Copy the contents of .env.example into it.

Replace the placeholder with your actual OpenAI API key:

env
Copy
Edit
OPENAI_API_KEY=your_real_openai_key_here
📂 Project Structure
css
Copy
Edit
llm-role-based-assistant/
├── main.py
├── role_logic.py
├── .env.example
├── requirements.txt
├── README.md
├── LICENSE
└── screenshots/
    ├── 1_swagger_ui.png
    ├── 2_post_request_input.png
    ├── 2_post_request_response.png
    ├── 3_valid_response.png
🖼️ Screenshots
🔹 1. Swagger UI Home

🔹 2. POST Request Input

🔹 2. POST Request Response

🔹 3. Valid Role-Based LLM Response

🛠️ Technologies Used
FastAPI

Uvicorn

OpenAI API

Pydantic

Python-dotenv

🧠 Author
Ariba Sameen Ansari
Cybersecurity Analyst | FastAPI Developer | AI + Security Enthusiast
🌐 GitHub

📎 License
This project is licensed under the Apache License 2.0.
See the LICENSE file for more details.