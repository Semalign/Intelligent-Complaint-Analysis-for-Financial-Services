 # Intelligent Complaint Analysis for Financial Services

This repository is part of a Retrieval-Augmented Generation (RAG) pipeline project for **Intelligent Complaint Analysis for Financial Services**, a leading digital finance company in East Africa. The tool is designed to transform large volumes of raw, unstructured consumer complaints into actionable insights for internal teams like Product, Support, and Compliance.

---

## ✅ Project Goals

- Analyze and clean raw CFPB complaint data.
- Embed and store customer complaint narratives in a vector database.
- Power semantic search and intelligent Q&A across five financial products:
  - Credit Cards
  - Personal Loans
  - Buy Now, Pay Later (BNPL)
  - Savings Accounts
  - Money Transfers

---


---

##  Tasks Completed

###  Task 1: EDA & Preprocessing
- Loaded large CFPB complaint dataset in chunks (5GB+)
- Filtered to relevant products (BNPL, Loans, etc.)
- Cleaned and normalized complaint narratives
- Output saved to `data/processed/filtered_complaints.csv`

###  Task 2: Embedding & Indexing
- Split long narratives into chunks using `RecursiveCharacterTextSplitter`
- Embedded using `sentence-transformers/all-MiniLM-L6-v2`
- Stored in FAISS vector DB + saved complaint metadata for traceability

###  Task 3: RAG Pipeline & Evaluation
- Created prompt templates and retrieval logic
- Integrated LLM via Hugging Face transformers (can be swapped to Mistral or LLaMA)
- Evaluated system with real user queries (BNPL, transfers, loans, etc.)

###  Task 4: UI Interface
- Built with Streamlit
- Allows any internal stakeholder to ask questions like:  
  `"What complaints do users have about money transfers?"`  
- Displays both the **LLM response** and **source excerpts** for transparency

---

i_rag_chatbot — RAG-based chatbot for CFPB data
