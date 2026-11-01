# LLM-Based Research Paper Summarization and Intelligent Question Answering System

<p align="center">
  <strong>Transforming Academic Research into Structured, Searchable, and Actionable Knowledge Using Large Language Models and Retrieval-Augmented Generation</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/LLM-Generative%20AI-purple" />
  <img src="https://img.shields.io/badge/RAG-Implemented-success" />
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-orange" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit" />
</p>

## 1. Project Overview

Academic research involves processing large volumes of scientific literature to understand research contributions, methodologies, experimental findings, limitations, and emerging research directions.

However, manually reviewing multiple research papers is time-consuming and makes it difficult to efficiently identify relationships between studies, extract relevant information, and investigate research gaps.

This project presents an **LLM-Based Research Paper Summarization and Intelligent Question Answering System** designed to streamline the academic literature analysis process using Natural Language Processing, Large Language Models, semantic embeddings, and Retrieval-Augmented Generation (RAG).

The system enables users to upload research papers in PDF format, automatically extract and process their contents, generate structured summaries, identify important research information, and interact with the documents through contextual question answering.

Unlike conventional summarization tools, the framework integrates document understanding, semantic retrieval, and research-oriented analysis into a unified pipeline.

**Primary Objective:** Develop an intelligent research assistant that reduces the effort required to understand academic literature while enabling structured information extraction and context-aware exploration of research papers.

## 2. Key Features

| Feature | Description |
|---|---|
| PDF Research Paper Ingestion | Upload and process academic research papers. |
| Automated Text Extraction | Extract textual content from PDF documents using PyMuPDF. |
| Document Preprocessing | Clean extracted content and organize research-paper sections. |
| Intelligent Summarization | Generate structured summaries in different formats. |
| Keyword Extraction | Identify important terms and concepts. |
| Topic Classification | Identify major research topics. |
| Citation Extraction | Extract citation-related information from research documents. |
| Research Gap Identification | Generate potential research-gap insights. |
| Semantic Search | Retrieve relevant document chunks using embeddings and FAISS. |
| RAG-Based Question Answering | Ask contextual questions and retrieve answers grounded in uploaded papers. |
| Section Analysis | Explore the structure and organization of research papers. |
| Report Generation | Export processed research information. |

## 3. System Architecture

The framework follows a modular architecture consisting of document ingestion, preprocessing, semantic representation, intelligent analysis, and retrieval-based question answering.

### Overall Workflow

```text
              User Uploads Research Paper
                         |
                         v
                 PDF Document
                         |
                         v
                Text Extraction
                  (PyMuPDF)
                         |
                         v
               Text Preprocessing
                         |
                         v
               Section Detection
                         |
                         v
                 Text Chunking
                         |
                         v
              Embedding Generation
             (Sentence Transformers)
                         |
                         v
                FAISS Indexing
                         |
              +----------+----------+
              |                     |
              v                     v
       Structured Analysis     RAG Retrieval
              |                     |
              v                     v
       Keyword Extraction      User Question
       Topic Classification          |
       Citation Extraction           v
       Research Gap Analysis   Semantic Retrieval
       Section Analysis              |
              |                      v
              |                Context Selection
              |                      |
              |                      v
              |                LLM Generation
              |                      |
              +----------+-----------+
                         |
                         v
                Research Insights
                         |
                         v
                Generated Reports
```

## 4. Technical Methodology

### 4.1 PDF Ingestion and Text Extraction

The system accepts academic research papers in PDF format through a FastAPI endpoint.

PyMuPDF is used to extract textual content from uploaded documents.

The extracted content is subsequently passed through preprocessing stages to prepare it for downstream NLP and language-model operations.

### 4.2 Document Preprocessing and Section Detection

Research papers generally follow a structured organization consisting of sections such as:

- Abstract
- Introduction
- Related Work
- Methodology
- Methods
- Results
- Discussion
- Conclusion
- References

The system processes extracted content and identifies relevant academic sections to facilitate structured analysis.

Section detection also helps organize document content for subsequent summarization and retrieval.

### 4.3 Semantic Chunking and Embedding Generation

Long research papers cannot always be processed efficiently as a single input.

Therefore, the extracted text is divided into smaller chunks to support efficient semantic representation and retrieval.

Sentence Transformer models generate dense vector representations of the text chunks.

These embeddings capture semantic information and enable similarity-based retrieval.

### 4.4 Vector Indexing and Semantic Retrieval

FAISS is used to support efficient similarity search over generated document embeddings.

When a user submits a question, the system compares its semantic representation with indexed document chunks to identify relevant contextual information.

This enables retrieval based on semantic similarity rather than relying exclusively on exact keyword matching.

### 4.5 LLM-Based Research Summarization

The system supports structured research-paper summarization.

The analysis pipeline generates different types of research insights, including:

- Paper summaries.
- Important keywords.
- Research topics.
- Research gaps.
- Citation-related information.

The objective is to provide a more organized understanding of research papers rather than presenting only a generic summary.

### 4.6 Retrieval-Augmented Generation (RAG)

The RAG component enables contextual question answering over uploaded research papers.

The process follows these stages:

1. Receive a user question.
2. Retrieve the corresponding document information.
3. Identify relevant chunks using semantic similarity.
4. Provide retrieved context to the language model.
5. Generate a context-informed response.
6. Return the answer along with relevant source information.

This approach helps ground generated responses in the uploaded research material.

### 4.7 Research Gap and Topic Analysis

The framework includes additional NLP-based analytical capabilities to explore the research content.

These include:

- Keyword extraction.
- Research topic classification.
- Citation extraction.
- Novelty scoring against a supplied collection of abstracts.
- Research gap identification.
- Research section graph generation.

These capabilities extend the system beyond conventional summarization towards structured academic literature analysis.

## 5. API Architecture

The backend is implemented using FastAPI and exposes modular endpoints for document processing, summarization, analysis, retrieval, and report generation.

| HTTP Method | Endpoint | Functionality |
|---|---|---|
| POST | `/upload_paper` | Upload a research paper |
| GET | `/get_summary/{paper_id}/{summary_type}` | Retrieve a selected summary |
| GET | `/get_keywords/{paper_id}` | Retrieve extracted keywords |
| GET | `/get_topics/{paper_id}` | Retrieve identified research topics |
| GET | `/get_research_gap/{paper_id}` | Retrieve research-gap analysis |
| POST | `/rag_query` | Perform contextual question answering |
| POST | `/analyze-paper` | Perform structured research analysis |
| GET | `/download_report/{paper_id}` | Download the generated report |
| GET | `/` | Backend health check |

For interactive API exploration, FastAPI provides automatically generated API documentation.

Once the backend is running, access:

`http://127.0.0.1:8000/docs`

## 6. Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Frontend Framework | Streamlit |
| PDF Processing | PyMuPDF |
| Natural Language Processing | NLP, Transformers |
| Language Models | Hugging Face Transformers |
| Text Embeddings | Sentence Transformers |
| Vector Search | FAISS |
| Machine Learning | Scikit-learn |
| Data Processing | NumPy, Pandas |
| Data Storage and Caching | SQLite |
| API Server | Uvicorn |

## 7. Repository Structure

```text
research-summarizer/
│
├── backend/
│   └── app/
│       ├── api/
│       │   ├── upload.py
│       │   ├── summary.py
│       │   ├── query.py
│       │   ├── analyze.py
│       │   └── download.py
│       │
│       ├── cache/
│       ├── core/
│       ├── nlp/
│       └── workers/
│
├── benchmarks/
│
├── data/
│   └── processed/
│
├── evaluation/
│
├── frontend/
│   └── streamlit_app.py
│
├── reports/
│
├── results/
│
├── scripts/
│
├── src/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

## 8. Installation and Execution

### Prerequisites

- Python 3.10 or later.
- pip.
- Git.

### Step 1: Clone the Repository

```bash
git clone https://github.com/ChiragR12624/research-summarizer.git

cd research-summarizer
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment.

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start the FastAPI Backend

```bash
uvicorn backend.app.main:app --reload --port 8000
```

### Step 5: Launch the Streamlit Frontend

Open another terminal, activate the virtual environment, and execute:

```bash
streamlit run frontend/streamlit_app.py
```

The application provides an interface for interacting with the research-paper processing system.

## 9. Experimental Development and Evaluation

The project includes dedicated directories for benchmarking, evaluation, and generated results.

The development and evaluation workflow focuses on examining document-processing performance, semantic retrieval, and research-analysis capabilities.

The system has been tested with academic research papers, covering document extraction, section identification, chunk creation, embedding generation, and contextual retrieval.

A representative processing run successfully extracted approximately 25,905 characters from a research paper, generated five text chunks, and produced five corresponding embeddings.

The implementation also supports testing the retrieval pipeline through contextual questions and inspecting the returned source information.

Further quantitative evaluation can examine:

- Document extraction completeness.
- Section detection effectiveness.
- Retrieval relevance.
- Question-answering quality.
- Summarization quality.
- Processing time and resource utilization.

## 10. Research and Engineering Contributions

The project explores the integration of several AI and NLP capabilities into a unified academic research assistant.

Its key contributions include:

1. Development of an automated academic PDF ingestion and preprocessing pipeline.
2. Integration of semantic embeddings and FAISS-based retrieval.
3. Implementation of LLM-based structured research summarization.
4. Development of contextual question answering using Retrieval-Augmented Generation.
5. Integration of research-oriented NLP analysis, including keyword extraction, topic classification, citation extraction, and research-gap identification.
6. Development of modular REST APIs using FastAPI.
7. Integration of a Streamlit interface for user interaction.

## 11. Limitations and Future Research

Although the system provides several capabilities for academic literature analysis, there are opportunities for further improvement.

Potential research directions include:

- Improving section detection for diverse academic publishing formats.
- Investigating advanced document-aware chunking strategies.
- Evaluating alternative embedding architectures.
- Exploring hybrid retrieval combining dense and lexical search.
- Introducing reranking techniques to improve retrieval relevance.
- Developing systematic evaluation benchmarks for summarization and RAG.
- Improving source attribution and factual consistency in generated responses.
- Extending the framework towards multi-document comparative analysis.
- Exploring knowledge graphs for representing relationships between research papers.

## 12. Intended Applications

The framework can support several academic and research-oriented activities:

- Understanding unfamiliar research papers.
- Reviewing academic literature.
- Extracting methodological information.
- Identifying research themes and potential research gaps.
- Exploring relationships between research findings.
- Performing contextual question answering over scientific documents.

## 13. Author

**Chirag R. Gowda**

Research Interests:

Machine Learning | Natural Language Processing | Large Language Models | Retrieval-Augmented Generation | Generative AI

GitHub: https://github.com/ChiragR12624

---

This project is developed for academic and research-oriented exploration of Large Language Models, semantic retrieval, and intelligent scientific document analysis.

Contributions, feedback, and research discussions are welcome.
