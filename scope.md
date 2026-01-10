# Enigma - Project Scope

## Vision

Enigma is not a chatbot. It is a **local, offline-capable cognitive operating system** - a personal intelligence substrate that operates as a governed system layer on top of macOS.

### Core Objectives

1. **Local Brain**: Offline LLM that can reason, write, summarize, restructure, and plan using only information from the Enigma folder
2. **Private Memory System**: Transform the Enigma folder into a living knowledge base with semantic search and structured memory
3. **Action Layer**: Automate Mac operations - open apps, read/write files, browse sites, extract information, execute workflows
4. **Controller/Orchestrator**: Decide what to read, which tools to use, what actions to take, and what to write back

## What Enigma Is NOT

- A casual chat interface
- A generic AI assistant
- An internet-connected service
- A tool for experimentation or model browsing

## What Enigma IS

- A governed cognitive system with constitutional boundaries
- An institutional memory with long-term recall
- An execution assistant with controlled automation
- A strategic thinking partner aligned to personal doctrine

## System Architecture

### Four Core Layers

```
You (Command)
   ↓
Enigma Controller (the brainstem)
   ↓
┌──────────────────────────────────────────┐
│           Cognitive Core                 │
│  (Local LLM + Reasoning + Planning)      │
└──────────────────────────────────────────┘
   ↓
┌──────────────────────────────────────────┐
│        Knowledge & Memory Engine         │
│ (Indexing, Retrieval, Versioned Memory) │
└──────────────────────────────────────────┘
   ↓
┌──────────────────────────────────────────┐
│          Action & Tool Layer             │
│ (Mac automation, web, documents, files) │
└──────────────────────────────────────────┘
   ↓
macOS, Filesystem, Apps, Browser
```

### 1. Enigma Controller (The Brainstem)

**Core Sub-systems:**
- **Intent Parser**: Classifies requests (thinking, writing, retrieval, automation, long task, monitoring)
- **Context Assembler**: Pulls relevant material from Enigma memory, enforces folder boundaries and instruction hierarchy
- **Planner**: Breaks tasks into steps, chooses tools, builds execution graphs
- **Execution Manager**: Calls tools, tracks state, handles failures, logs everything
- **Verifier**: Checks outputs, confirms sources, prevents hallucination, flags uncertainty

### 2. Cognitive Core (Local Intelligence)

**Responsibilities:**
- Reasoning and planning
- Writing and rewriting (English refinement)
- Summarization and synthesis
- Interpretation of instructions

**Critical Constraint:** It does NOT browse, touch files directly, or act. It only thinks. Everything it knows is explicitly provided.

### 3. Knowledge & Memory Engine

**Subsystems:**

**A. Ingestion Pipeline**
- Watches Enigma folder
- Reads: PDF, DOCX, PPT, TXT/MD, images (OCR), chat logs
- Chunks meaningfully
- Extracts metadata
- Versions everything

**B. Semantic Index**
- Meaning-based search (vector database)
- Cross-project linking
- Instruction tagging
- Timeline memory

**C. Structured Memory**
- Personal doctrine
- Systems documentation
- Project realities
- Decisions and rationales
- Stored in SQLite/DuckDB

**D. Ground Truth Store**
- Immutable reference documents
- Source-of-truth constraints
- Non-overwritable memories

### 4. Action & Tool Layer

**Categories:**

**A. File & Document Tools**
- Read/write Word, PDF, Markdown
- Versioning and auto-organization
- Report generation

**B. macOS Automation**
- Open apps, control UI
- Move files, trigger workflows
- Capture screenshots

**C. Browser & Data Tools**
- Navigate sites
- Extract content, fill forms
- Scrape structured data

**D. System Tools**
- Schedulers, background watchers
- Triggers and logging

**E. Custom Skills**
- Internal business workflows
- Reusable task modules

## The Enigma Constitution

### The Four Layers of Enigma Reality

**LAYER 1: Ground Truth (Immutable)**
- Folder: `99_GroundTruth/`
- Cannot be modified or contradicted by Enigma
- Contains: Core principles, doctrine, system blueprints, business truths, canonical definitions
- All reasoning must defer to this layer

**LAYER 2: Structured Reality (High Trust)**
- Folders: `02_Systems/`, `04_Memory/Decisions/`
- Modifiable only with explicit approval
- Contains: Systems documentation, project maps, decisions & rationales, operating procedures
- Treated as authoritative unless Ground Truth overrides

**LAYER 3: Working Knowledge (Evolving)**
- Folders: `01_Skills_And_Education/`, `03_Projects/`, `05_Tasks/`
- Freely writable and summarizable
- Contains: Notes, research, drafts, proposals, chat histories, experiments
- Must never be silently promoted to Layer 1 or 2

**LAYER 4: Derived Intelligence (Generated)**
- Folder: `06_Derived/`
- Never treated as truth by default
- Contains: Reports, briefs, plans, syntheses, drafts, analyses
- Promotion requires explicit human action

### Key Constitutional Principles

**Source Sovereignty:**
- Every factual answer must be traceable to Ground Truth, Structured Reality, or explicit documents
- If not found: "Not found in Enigma knowledge"
- May reason, but may not invent facts

**Instruction Hierarchy:**
1. Ground Truth
2. System Doctrine
3. Project Reality
4. Task Instructions
5. User Command

**Action Authority Tiers:**
- **Tier 0**: Thinking only (analysis, writing, synthesis)
- **Tier 1**: File-safe operations (read, write drafts, organize, summarize)
- **Tier 2**: Workflow operations (browsing, data capture, reporting, transformations) - requires confirmation
- **Tier 3**: System-level (automation, deletion, cross-system actions) - requires confirmation

**Memory Law:**
- All memory entries must include: source, date, layer classification, confidence level
- Cannot store as truth: guesses, hallucinations, emotional interpretations, speculative intent

## Technology Stack

### Decision: OLLAMA (Locked)

**Why Ollama over LM Studio:**
- Designed as a local model service, not a UI product
- Stable local HTTP API, headless by nature
- Easy to call from Python, schedulers, background services
- Behaves like local infrastructure, not a workstation
- Designed for automation, background processes, and orchestration

**Recommended Models:**
- Qwen 2.5 / Qwen 2.5-Instruct (strong reasoning, excellent writing)
- Llama 3.1 / 3.2 (stable, large ecosystem)
- Mixtral / Mistral (faster, good synthesis)

### Core Technology Components

**Knowledge & Memory:**
- Document ingestion: Unstructured, Apache Tika, Tesseract OCR
- Chunking & orchestration: LlamaIndex
- Vector store: Qdrant (local mode) or Chroma
- Structured memory: SQLite / DuckDB

**Controller:**
- Language: Python
- Frameworks: LangGraph (multi-step planners, state machines), Pydantic (schemas), FastAPI (local only)

**Action & Automation:**
- macOS control: AppleScript, Shortcuts, pyobjc, Keyboard Maestro (optional)
- Browser automation: Playwright
- Document handling: python-docx, pdfplumber, pymupdf, openpyxl
- File operations: Native Python, Watchdog (folder monitoring)

**Interface:**
- Start with: CLI + minimal desktop panel
- Future: Local web app (FastAPI + React) or Mac-native (Tauri/Electron)

### System Safeguards (Non-Negotiable)

- Execution approval layer
- Tool permission system
- Read-only memory zones
- Full activity logs
- Replayability

## Folder Structure

```
Enigma/
├── 00_Doctrine/              # Identity & style, philosophies, behavioral codes
├── 01_Skills_And_Education/  # Learning resources, books, research, reference
├── 02_Systems/               # System documentation, processes, frameworks
├── 03_Projects/              # Active project folders, proposals, scopes, working notes
├── 04_Memory/
│   ├── Decisions/            # Decision logs with rationale
│   ├── Learnings/            # Distilled insights and patterns
│   └── Experiments/          # Hypotheses and results
├── 05_Tasks/                 # Task lists, automation instructions, workflows, SOPs
├── 06_Derived/               # Enigma-generated reports, briefs, drafts, analyses
└── 99_GroundTruth/           # Immutable principles, doctrine, canonical definitions
```

## The First 7 Seed Documents

These foundational documents teach Enigma identity, law, voice, reality, judgment, focus, and intelligence:

1. **`99_GroundTruth/Personal_Doctrine.md`** - Non-negotiable principles, thinking style, decision filters, non-negotiables
2. **`99_GroundTruth/Enigma_Constitution.md`** - The constitutional framework (layered knowledge, source rules, action tiers, memory laws)
3. **`99_GroundTruth/Writing_Standard.md`** - Preferred tone, style, red flags, editing mandate
4. **`02_Systems/Systems_Map.md`** - Map of all major systems, their purpose, scope, and interrelations
5. **`04_Memory/Decisions/Master_Decision_Log.md`** - Decision entries with context, rationale, alternatives, risks
6. **`03_Projects/Active_Projects_Index.md`** - Current projects with objectives, phase, constraints, success definition
7. **`04_Memory/Learnings/Learning_Log.md`** - Distilled insights with trigger, insight, impact, behavior change

## Development Phases

### Phase 1: Enigma Brain (Offline Thinking Partner)

**Goals:**
- Local AI strictly reads Enigma folder
- Answers questions, improves English
- Writes documents, summarizes, creates structured outputs
- Trustworthy private intelligence

### Phase 2: Enigma Memory

**Goals:**
- Automatic ingestion of everything added
- Deep semantic retrieval
- Cross-project understanding
- Persistent long-term context
- External long-term memory

### Phase 3: Enigma Operator

**Goals:**
- File operations
- Document generation
- Research capture
- Controlled browsing
- Repeatable workflows
- Execution assistant

### Phase 4: Enigma System Intelligence

**Goals:**
- Personalities & principles become operating constraints
- Systems become active frameworks
- Culture becomes decision logic
- Goals drive task creation
- A true personal operating system

## What Makes Enigma Different

Most "local AI" setups are: **model + chat + documents**

Enigma is:
- **Doctrine-driven**: Operates within constitutional boundaries
- **Memory-structured**: Four-layer knowledge hierarchy with strict sovereignty
- **System-integrated**: Deep macOS integration for automation
- **Execution-capable**: Can act on the world, not just respond

## Key Success Criteria

1. **Offline Operation**: Works without internet connectivity
2. **Folder Sovereignty**: Uses ONLY information from Enigma folder
3. **English Excellence**: Strong writing and refinement capabilities
4. **Mac Automation**: Can operate desktop, files, browsers, workflows
5. **Constitutional Governance**: Respects layer boundaries and instruction hierarchy
6. **Auditability**: All actions logged, replayable, explainable
7. **Progressive Intelligence**: Evolves from document reader to analyst to operator to strategic assistant

## Critical Design Principles

1. **Foundations before features**: Constitution before automation
2. **Boring is good**: Stable, scriptable, composable over flashy
3. **Separation of concerns**: Thinking, memory, tools, interface remain distinct
4. **No silent knowledge**: Every fact traceable to source
5. **Explicit over implicit**: No assumptions, no hallucinations
6. **Infrastructure thinking**: This is not an app, it's a cognitive substrate
7. **Progressive capability**: Each phase builds on the previous, no skipping

## Next Steps

1. **Seed Document Creation**: Complete the 7 foundational documents
2. **Ollama Setup**: Install and configure Ollama with chosen model
3. **Basic Controller**: Build Python controller for document ingestion and query
4. **Memory Engine**: Implement vector database and semantic search
5. **CLI Interface**: Create command-line interface for interaction
6. **File Automation**: Add basic file read/write capabilities
7. **Iteration**: Expand capabilities progressively based on real usage

---

**Note:** This is not a weekend project. This is infrastructure. Done right, Enigma becomes a personal cognitive operating system that compounds in value over time.
