# 🐾 Juan – The Chatbot Cat

Juan is a friendly orange-and-white cat chatbot 🐱 designed to share engaging and insightful information about his human, Fabio Guerreiro. Integrated into [Fabio's portfolio](https://github.com/FGuerreir0/Portfolio.V2), Juan helps visitors get to know him in a fun and interactive way.

<p align="center">
  <img src="https://github.com/FGuerreir0/chatbot-juan/blob/main/assets/juan.webp" alt="Juan the Cat" width="300" height="300">
</p>

Powered by:
- 🐍 Python – the core language used to build Juan
- 🧠 [LangChain](https://www.langchain.com/) – to manage the reasoning and prompts
- 📚 RAG (Retrieval-Augmented Generation) – to provide smart, context-based answers
- 🐋 Docker – for easy deployment
- 🤖 [Ollama](https://ollama.com/) – local LLM inference

---

## 🚀 Features

- Serves a FastAPI endpoint for chat interactions
- Loads and processes contextual info using RAG
- Acts as a curious and cute AI cat named Juan
- Only answers what is asked, following a natural and concise tone

---

## 🐳 Docker Setup

### Build the image:

```bash
docker build -t juan .
docker run -d -p 8051:8051 juan
docker run juan
```

---

## 🧪 Example API Request:

```bash
GET http://localhost:8051/status
POST http://localhost:8051/juan/chat

body:
  {
    "message": "Tell me about Fabio's projects"
  }
```

---

## 📎 Notes

- Make sure you have Ollama running locally - (https://hub.docker.com/r/ollama/ollama)
- LangChain + RAG is used to fetch and ground responses using a knowledge base about Fabio.
- The chatbot try to avoid adding unnecessary info and responds directly based on user questions.

---

## 📬 Feedback or Contributions?

Open an issue or a PR if you want to contribute, or just say hi to Juan! 😸
