# 🚀 Augmented sales analytics dashboard

Turn natural language into SQL queries and get instant results from your dataset using the power of Generative AI.

---

## 🧠 About the Project

This project allows users to ask questions in plain English and automatically converts them into SQL queries, executes them on a SQLite database, and returns the results.

It demonstrates how Large Language Models (LLMs) can simplify database interactions—no SQL knowledge required.

---

## ✨ Features

* 🔤 Convert natural language → SQL queries
* 🗄️ Execute queries on SQLite database
* 📄 Load dataset dynamically from CSV file
* 🤖 LLM-powered (supports Gemini / Claude)
* ⚡ Lightweight and easy-to-understand structure

---

## 📁 Project Structure

```
TextToSqlQuery/
│
├── app.py              # 🚀 Main application entry point
├── llm.py              # 🤖 LLM integration (Gemini / Claude)
├── sql.py              # 🗄️ Database + query execution logic
├── data.csv            # 📄 Dataset file
│
├── .env                # 🔐 API keys (not committed)
├── requirements.txt    # 📦 Dependencies
├── README.md           # 📘 Documentation
```

---

## ⚙️ How It Works

```
User Input (Text)
        ↓
LLM (Text → SQL)
        ↓
SQLite Database
        ↓
Query Results
```

### 🪄 Step-by-step:

1. User enters a natural language query
2. LLM converts it into SQL
3. SQL query runs on SQLite database
4. Results are displayed

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd TextToSqlQuery
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

* Mac/Linux:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key 🔐

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

*(Or use Claude API if configured)*

---

### 5️⃣ Run the application

```bash
python app.py
```

---

## 💡 Example Queries

Try asking:

* "Show all cars with price greater than 20000"
* "Average selling price by state"
* "Top 5 most expensive cars"
* "Count cars by manufacturer"

---

## ⚠️ Notes

* Only `SELECT` queries are allowed for safety
* LLM output is cleaned before execution
* Ensure CSV column names match the schema

---

## 🧰 Tech Stack

* 🐍 Python
* 🗄️ SQLite
* 📊 Pandas
* 🤖 LLM APIs (Gemini / Claude)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Inspired by real-world GenAI + database integrations
* Built as a learning project for AI-powered data querying

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub and feel free to contribute!
