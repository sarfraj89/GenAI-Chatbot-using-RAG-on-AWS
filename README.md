# 📄 GenAI Document Analysis Chatbot using RAG on AWS

A **production-ready Generative AI chatbot** built using the **Retrieval-Augmented Generation (RAG)** approach on **AWS**, powered by **Amazon Bedrock**.  
The application answers user questions by retrieving relevant information from documents and generating grounded, context-aware responses.

---

## 🚀 Project Overview

Large Language Models (LLMs) are powerful but often hallucinate when answering questions without external knowledge.  
This project solves that problem by implementing a **RAG pipeline**, where relevant document context is retrieved before response generation.

The chatbot is designed to analyze **market study documents** and provide accurate answers using a scalable, cloud-native architecture.

---

## ✨ Features

- 📚 Document-based question answering
- 🔍 Semantic search using vector embeddings
- 🧠 Context-aware responses with LLMs
- ☁️ Fully deployed on AWS
- 🐳 Dockerized application
- 📈 Scalable & production-ready setup
- 🖥️ Simple and interactive UI using Gradio

---

## 🏗️ Architecture Diagram
![architecure_diagram](https://github.com/user-attachments/assets/c6b26306-abbf-4b5f-ab2d-f584136caa39)

---

## 🧩 Tech Stack

### Frontend
- **Gradio** – Web-based chatbot UI

### Backend
- **Python**
- **LlamaIndex** – RAG orchestration (retrieval + generation)

### AWS Services
- **Amazon Bedrock**
  - Knowledge Bases
  - Foundation Models (LLMs)
- **Amazon S3** – Document storage
- **Amazon OpenSearch** – Vector similarity search
- **Amazon ECR** – Container registry
- **AWS App Runner** – Application deployment
- **IAM & Parameter Store** – Security & configuration

### DevOps
- **Docker**

---

## 🔄 RAG Pipeline Breakdown

1. **Document Ingestion**
   - Documents are uploaded to Amazon S3
   - Files are chunked for efficient retrieval

2. **Embedding Generation**
   - Amazon Bedrock generates vector embeddings
   - Embeddings are stored in a vector database

3. **Query Processing**
   - User submits a query via the Gradio UI
   - Query is converted into an embedding

4. **Context Retrieval**
   - Similar document chunks are retrieved using vector search

5. **Answer Generation**
   - Retrieved context + user query is sent to an LLM
   - LLM generates a grounded response

6. **Response Delivery**
   - Final answer is returned to the user

---


### 🔹 UI
<img width="1449" height="831" alt="Screenshot from 2026-01-30 20-00-28" src="https://github.com/user-attachments/assets/73809c81-4884-45e4-a38f-1c8453b2ce39" />

---

## 🙌 Acknowledgements

This project was built by learning from and leveraging the following tools and resources:

- **Amazon Bedrock & AWS Documentation** – For GenAI services, Knowledge Bases, and cloud architecture
- **LlamaIndex** – For building and orchestrating the Retrieval-Augmented Generation (RAG) pipeline
- **Gradio** – For creating a simple and effective chatbot user interface

---

## 📬 Contact

If you’d like to discuss this project, collaborate on **GenAI**, **Cloud**, or **DevOps** work, or share feedback:

- 💼 Connect with me on LinkedIn  
- 💬 Open an issue or discussion in this repository  

I’m always open to learning, collaboration, and building production-ready AI systems

---







