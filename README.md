# 🏥 Medical Chatbot (RAG-Based GenAI Project)

An AI-powered Medical Chatbot built using Retrieval-Augmented Generation (RAG).  
This project allows users to ask medical-related questions based on document knowledge and get AI-generated responses.

---

## 🚀 Clone the Repository

```bash
git clone https://github.com/Shuklashivam123/1_PROJECT_MEDICAL_CHATBOT_MINE_RAG.git
cd 1_PROJECT_MEDICAL_CHATBOT_MINE_RAG
```

---

## 🐍 Create Virtual Environment

```bash
conda create -n medicalbot python=3.10
```

### ▶️ Activate Environment
```bash
conda activate medicalbot
```

### ❌ Delete Environment
```bash
conda remove -n medicalbot --all
```

### 📋 List All Environments
```bash
conda env list
```

---

## 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 📁 Automatic Project Structure Creation

Create a file named:

```
template.sh
```

Add the following commands:

```bash
mkdir -p src
mkdir -p static
mkdir -p research

touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch .env
touch setup.py
touch app.py
touch research/trials.ipynb
touch requirements.txt

echo "Directory and files created successfully!"
```

Run using Git Bash:

```bash
sh template.sh
```

---

## ⚙️ Tech Stack

- Python
- LangChain
- HuggingFace Embeddings
- Vector Database (Pinecone / FAISS)
- LLM Integration (Groq / Open Source Models)
- RAG Architecture

---

## 📌 Features

- Document-based Medical Question Answering
- Retrieval-Augmented Generation (RAG)
- Modular Project Structure
- Automatic Project Setup
- Custom Prompt Engineering
- Scalable AI Chatbot Architecture

---

## ▶️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:8080/
```

---

## 📜 License

This project is created for educational and learning purposes.

---

## 👨‍💻 Author

Shivam Shukla  
GitHub: https://github.com/Shuklashivam123