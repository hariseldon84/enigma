#!/usr/bin/env python3
"""
Smart Query Script for Enigma
Uses semantic search to find relevant chunks before querying.
MUCH faster than simple_query.py because it only sends relevant context.

Usage:
    python3 scripts/smart_query.py "What are my core principles?"
"""

import sys
from pathlib import Path
import chromadb
import ollama

# Enigma paths
ENIGMA_ROOT = Path(__file__).parent.parent
CHROMA_DIR = ENIGMA_ROOT / "data" / "chromadb"

def search_knowledge(query, n_results=5):
    """Search for relevant document chunks."""

    if not CHROMA_DIR.exists():
        print("❌ Index not found. Please run: python3 scripts/index_documents.py")
        sys.exit(1)

    # Connect to ChromaDB
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    try:
        collection = client.get_collection("enigma_knowledge")
    except:
        print("❌ Index not found. Please run: python3 scripts/index_documents.py")
        sys.exit(1)

    # Search for relevant chunks
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results

def format_context(search_results):
    """Format search results into context string."""

    if not search_results['documents'][0]:
        return "No relevant information found in Enigma knowledge."

    context_parts = []

    for i, doc in enumerate(search_results['documents'][0]):
        metadata = search_results['metadatas'][0][i]
        filename = metadata.get('filename', 'Unknown')
        layer = metadata.get('layer', 'Unknown')

        context_parts.append(
            f"## Source: {filename} ({layer})\n\n{doc}\n"
        )

    return "\n---\n\n".join(context_parts)

def query_enigma(question, context, model="qwen3:8b"):
    """Send query to Ollama with context."""

    system_prompt = """You are Enigma, a personal cognitive operating system.

Your constitutional rules:
1. ONLY use information from the provided document excerpts
2. If information is not found, say "Not found in Enigma knowledge"
3. Always cite which document you're referencing
4. No hallucination - stick to facts in the documents
5. Voice: Professional + Casual (direct, no buzzwords, no fluff)
6. Structure responses clearly (use headings, bullets where appropriate)

When answering, cite sources like this: (from Personal_Doctrine.md) or (from Enigma_Constitution.md)
"""

    user_prompt = f"""Based ONLY on the following excerpts from Enigma documents, answer this question:

{question}

---

RELEVANT EXCERPTS:

{context}

---

Remember: Only use information from these excerpts. Cite your sources. Be clear and direct."""

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ]
        )

        return response['message']['content']

    except Exception as e:
        return f"❌ Error querying Ollama: {e}\n\nMake sure Ollama is running: ollama serve"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/smart_query.py \"Your question here\"")
        print("\nExample queries:")
        print('  python3 scripts/smart_query.py "What are my core principles?"')
        print('  python3 scripts/smart_query.py "How should Enigma handle uncertainty?"')
        print('  python3 scripts/smart_query.py "What is my writing style?"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    print("="*80)
    print("ENIGMA SMART QUERY (with semantic search)")
    print("="*80)
    print(f"\n❓ Question: {question}\n")

    # Search for relevant chunks
    print("🔍 Searching knowledge base...")
    search_results = search_knowledge(question, n_results=5)

    num_results = len(search_results['documents'][0])
    print(f"✅ Found {num_results} relevant chunks\n")

    # Show which documents were found
    print("📄 Sources:")
    seen_files = set()
    for metadata in search_results['metadatas'][0]:
        filename = metadata.get('filename', 'Unknown')
        if filename not in seen_files:
            layer = metadata.get('layer', 'Unknown')
            print(f"  - {filename} ({layer})")
            seen_files.add(filename)
    print()

    # Format context
    context = format_context(search_results)

    # Query Enigma
    print("🤔 Querying Enigma...")
    answer = query_enigma(question, context)

    # Display answer
    print()
    print("="*80)
    print("ENIGMA RESPONSE")
    print("="*80)
    print(f"\n{answer}\n")
    print("="*80)

if __name__ == "__main__":
    main()
