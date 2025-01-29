from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from constants import DATA_DIR, VECTOR_STORE_DIR, EMBED_MODEL
from data_loader import load_resumes

def ingest_resumes():
    # Initialize models
    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)
    
    # Load and parse resumes
    documents = load_resumes(DATA_DIR)
    
    # Create nodes with metadata
    node_parser = SimpleNodeParser.from_defaults()
    nodes = node_parser.get_nodes_from_documents(documents)
    
    # Create and persist index
    storage_context = StorageContext.from_defaults()
    index = VectorStoreIndex(
        nodes=nodes,
        storage_context=storage_context,
        embed_model=embed_model
    )
    
    # Persist index to disk
    index.storage_context.persist(persist_dir=VECTOR_STORE_DIR) 

if __name__ == "__main__":
    ingest_resumes()