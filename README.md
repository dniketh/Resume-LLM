# **Resume-LLM**

**Resume-LLM** is a **Proof-of-Concept (POC) model** developed for a **project proposal** to analyze and rank resumes based on specific job descriptions using **Retrieval-Augmented Generation (RAG)**. By integrating **Large Language Models (LLMs) with vector databases**, this tool enhances the recruitment process by providing **context-aware resume evaluations**.

## **Features**
- **Automated Resume Analysis**: Evaluates resumes against job descriptions to determine relevance.  
- **Context-Aware Ranking**: Uses **LLMs** and **vector search** (FAISS/Pinecone/OpenSearch) to rank resumes based on content and context.  


## **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dniketh/Resume-LLM.git
   cd Resume-LLM
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**
1. **Data Ingestion**: Load and preprocess resumes and job descriptions.  
   ```bash
   python ingest.py --resumes /path/to/resumes --job_descriptions /path/to/job_descriptions
   ```
2. **Start the Application**: Run the main script to process and rank resumes.  
   ```bash
   python app.py
   ```
3. **Retrieve Ranked Resumes**: Use the retriever module to fetch rankings for a given job description.  
   ```bash
   python retriever.py --job_description /path/to/job_description
   ```

## **Configuration**
Modify `constants.py` to update **paths, model configurations, embedding parameters, and API settings**.

## **Project Scope**
This model was developed as a **Proof-of-Concept (POC) for a project proposal**, showcasing the feasibility of **AI-driven resume ranking using LLMs and vector databases**.

## **Contributing**
Contributions are welcome! Please **fork the repository** and submit a pull request with improvements.

