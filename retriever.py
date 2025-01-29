from llama_index.core import StorageContext
from llama_index.core.indices import load_index_from_storage
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.memory import ChatMemoryBuffer
from constants import VECTOR_STORE_DIR, EMBED_MODEL
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

class ResumeRetriever:
    def __init__(self):
        # Load storage context
        storage_context = StorageContext.from_defaults(
            persist_dir=VECTOR_STORE_DIR
        )
        
        # Load index using updated method
        self.index = load_index_from_storage(
            storage_context=storage_context,
            embed_model=HuggingFaceEmbedding(model_name=EMBED_MODEL)
        )
        
        # Configure retriever
        self.retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=5,
        )
        
        # Configure local LLM via Ollama
        self.llm = Ollama(
            model="llama3.2",
            base_url="http://localhost:11434",
            temperature=0.1,
            request_timeout=300.0
        )

        # Add memory for chat history
        self.memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        
        self.chat_engine = self.index.as_chat_engine(
            chat_mode="condense_plus_context",
            llm=self.llm,
            memory=self.memory,
            context_prompt = """You are a helpful HR assistant analyzing resumes for a job description.
            Use the context from resumes to answer questions thoroughly.
            Provide detailed analysis of the resumes found from the database, and if no relevant resumes are found, say so and no more information is available""",
            verbose=True
        )
              
        self.query_engine = RetrieverQueryEngine.from_args(
            retriever=self.retriever,
            response_mode="tree_summarize",
            llm=self.llm,
            system_prompt="""You are a helpful HR assistant analyzing resumes for a job description.
            Use the context from resumes to answer questions thoroughly.
            Provide detailed analysis of the resumes, and if no relevant resumes are found, say so            
            """
        )

        print("Initial memory state:", self.memory.get_all())
        print("Chat engine mode:", self.chat_engine.chat)

    def reset_state(self):
        """Method to explicitly reset all stateful components"""
        self.memory.reset()
        self.chat_engine.reset()
    
    def chat(self, message: str) -> str:
        """Handle chat messages with context from previous interactions"""
        print(f"\nReceived message: {message}")
        print("Current memory:", self.memory.get_all())
        response = self.chat_engine.chat(message)
        print("Response generated:", response)
        return str(response) 