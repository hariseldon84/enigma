#!/usr/bin/env python3
"""
Document Indexer for Enigma
Creates semantic embeddings of all documents for fast retrieval.

Usage:
    python3 scripts/index_documents.py
"""

import os
from pathlib import Path
import chromadb
from chromadb.config import Settings

# Enigma paths
ENIGMA_ROOT = Path(__file__).parent.parent
CHROMA_DIR = ENIGMA_ROOT / "data" / "chromadb"
GROUND_TRUTH_DIR = ENIGMA_ROOT / "99_GroundTruth"
SYSTEMS_DIR = ENIGMA_ROOT / "02_Systems"
PROJECTS_DIR = ENIGMA_ROOT / "03_Projects"
MEMORY_DIR = ENIGMA_ROOT / "04_Memory"

def chunk_document(content, filename, chunk_size=1000, overlap=200):
    """Split document into overlapping chunks."""
    chunks = []
    words = content.split()

    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append({
            'content': chunk,
            'filename': filename,
            'chunk_id': f"{filename}_chunk_{len(chunks)}"
        })

    return chunks

def load_markdown_files(directory, layer):
    """Load all markdown files from a directory."""
    documents = []

    if not directory.exists():
        print(f"⚠️  Directory not found: {directory}")
        return documents

    for file_path in directory.rglob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

                # Skip if empty
                if not content.strip():
                    continue

                # Chunk the document
                chunks = chunk_document(content, file_path.name)

                for chunk in chunks:
                    documents.append({
                        'id': chunk['chunk_id'],
                        'content': chunk['content'],
                        'metadata': {
                            'filename': chunk['filename'],
                            'layer': layer,
                            'path': str(file_path.relative_to(ENIGMA_ROOT))
                        }
                    })

                print(f"  ✅ {file_path.name}: {len(chunks)} chunks")

        except Exception as e:
            print(f"  ⚠️  Error reading {file_path.name}: {e}")

    return documents

def create_index():
    """Create or update the document index."""

    print("="*80)
    print("ENIGMA DOCUMENT INDEXER")
    print("="*80)
    print()

    # Create data directory if needed
    CHROMA_DIR.parent.mkdir(parents=True, exist_ok=True)

    # Initialize ChromaDB
    print("🔧 Initializing ChromaDB...")
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    # Delete existing collection if it exists
    try:
        client.delete_collection("enigma_knowledge")
        print("  ✅ Cleared existing index")
    except:
        pass

    # Create new collection
    collection = client.create_collection(
        name="enigma_knowledge",
        metadata={"description": "Enigma knowledge base"}
    )
    print("  ✅ Created new index\n")

    # Load documents from each layer
    all_documents = []

    print("📚 Loading Layer 1: Ground Truth...")
    all_documents.extend(load_markdown_files(GROUND_TRUTH_DIR, "Layer 1: Ground Truth"))

    print("\n📚 Loading Layer 2: Systems...")
    all_documents.extend(load_markdown_files(SYSTEMS_DIR, "Layer 2: Structured Reality"))

    print("\n📚 Loading Layer 2: Memory...")
    all_documents.extend(load_markdown_files(MEMORY_DIR, "Layer 2: Structured Reality"))

    print("\n📚 Loading Layer 3: Projects...")
    all_documents.extend(load_markdown_files(PROJECTS_DIR, "Layer 3: Working Knowledge"))

    print()
    print("="*80)
    print(f"📊 INDEXING SUMMARY")
    print("="*80)
    print(f"Total chunks to index: {len(all_documents)}")

    if not all_documents:
        print("\n❌ No documents found to index!")
        return

    # Add to ChromaDB
    print("\n🔍 Creating embeddings and indexing...")

    ids = [doc['id'] for doc in all_documents]
    contents = [doc['content'] for doc in all_documents]
    metadatas = [doc['metadata'] for doc in all_documents]

    collection.add(
        ids=ids,
        documents=contents,
        metadatas=metadatas
    )

    print("  ✅ Indexing complete!")

    # Show summary by layer
    print("\n📊 Documents by layer:")
    layer_counts = {}
    for doc in all_documents:
        layer = doc['metadata']['layer']
        layer_counts[layer] = layer_counts.get(layer, 0) + 1

    for layer, count in sorted(layer_counts.items()):
        print(f"  {layer}: {count} chunks")

    print()
    print("="*80)
    print("✅ INDEX CREATED SUCCESSFULLY")
    print("="*80)
    print(f"\nIndex location: {CHROMA_DIR}")
    print(f"Total indexed chunks: {len(all_documents)}")
    print("\nYou can now use: python3 scripts/smart_query.py")
    print()

if __name__ == "__main__":
    create_index()
