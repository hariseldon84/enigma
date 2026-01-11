# NEXT TASKS - What to Build Next

**Last Updated:** 2026-01-10
**Current Status:** Phase 1A Complete (Basic Query Working)
**What Works Now:** Query Ground Truth docs, semantic search with gemma2:2b

---

## ✅ COMPLETED TODAY

- [x] Folder structure created
- [x] 7 seed documents written
- [x] Ollama installed (gemma2:2b working)
- [x] Python dependencies installed
- [x] Document indexer built (ChromaDB)
- [x] Smart query script working
- [x] Can ask Enigma questions and get cited answers

---

## 🎯 NEXT PRIORITY TASKS

### TASK 1: Support More File Types (High Priority) ⭐⭐⭐
**Time:** 30-45 minutes
**Why:** You want to add PDFs and Word docs to Enigma

**What to build:**
- Extend `index_documents.py` to read:
  - `.docx` (Word documents)
  - `.pdf` (PDFs)
  - `.txt` (Text files)

**Result:** All your research, books, and Product Genome chapters become searchable

**Test:**
```bash
# Add a PDF to Skills folder
cp ~/Documents/book.pdf ~/Enigma/01_Skills_And_Education/

# Re-index
python3 scripts/index_documents.py

# Query it
python3 scripts/smart_query.py "What does the book say about..."
```

---

### TASK 2: Product Genome Word Document Editor (Top Priority) ⭐⭐⭐
**Time:** 1-2 hours
**Why:** Your #1 frustration - "editing word doc for my book"

**What to build:**
```bash
python3 scripts/edit_document.py --file 03_Projects/Product_Genome/Chapter_01.docx --mode suggest
```

**Features:**
1. Read Word document
2. Analyze against Writing_Standard.md
3. Check for:
   - Buzzwords (synergy, revolutionary, etc.)
   - Passive voice
   - Vague statements
   - Poor structure
4. Suggest or apply improvements
5. Show diff (what changed and why)

**Modes:**
- `check` - Just analyze, show issues
- `suggest` - Provide improvement suggestions
- `refine` - Apply improvements automatically

**Result:** Automate Product Genome editing (saves hours weekly)

---

### TASK 3: File Organization Automation (Medium Priority) ⭐⭐
**Time:** 45-60 minutes
**Why:** Managing scattered information is a time sink

**What to build:**
```bash
python3 scripts/organize_files.py --source ~/Downloads --auto
```

**Features:**
- Watch Downloads folder
- Auto-categorize files (PDF → Skills, DOCX → Projects, etc.)
- Move to appropriate Enigma folder
- Auto re-index

**Result:** Files automatically organized and indexed

---

### TASK 4: Unified CLI Interface (Nice to Have) ⭐
**Time:** 30 minutes
**Why:** Easier to use one command for everything

**What to build:**
```bash
# Single entry point
python3 enigma.py query "What are my principles?"
python3 enigma.py edit document.docx --mode suggest
python3 enigma.py index
python3 enigma.py status
```

**Result:** Cleaner, more professional interface

---

### TASK 5: Folder Watcher (Automation) ⭐
**Time:** 30 minutes
**Why:** Auto-index new files without manual command

**What to build:**
```bash
# Run in background
python3 scripts/watch_folders.py &
```

**Features:**
- Monitors Enigma folders for new/changed files
- Auto-indexes them
- Logs activity

**Result:** Add files, they're immediately searchable

---

## 📋 IMMEDIATE NEXT STEPS (Today or Tomorrow)

### Option A: Add Your Files First
1. Copy Product Genome chapters to `03_Projects/Product_Genome/`
2. Copy research PDFs to `01_Skills_And_Education/`
3. Build Task 1 (support Word/PDF)
4. Re-index everything
5. Test queries on your actual content

### Option B: Build Editor First
1. Build Task 2 (Word document editor)
2. Test with one Product Genome chapter
3. Iterate on quality
4. Then add more files

**My recommendation:** Option A (add files first)
- See what you actually have
- Test queries on real content
- Then build editor based on real needs

---

## 🛠️ WHICH TASK TO START WITH?

**If your goal is:** Query your existing research/books
→ **Build Task 1** (File type support) - 30-45 min

**If your goal is:** Edit Product Genome faster
→ **Build Task 2** (Word editor) - 1-2 hours

**If your goal is:** Full automation
→ **Build Tasks 3, 4, 5** - 2-3 hours total

---

## ⏱️ TIME ESTIMATES

**Minimum viable (Tasks 1-2):** 2-3 hours
- Support all file types
- Basic Word document editor
- **Result:** Can query everything, edit Product Genome

**Full Phase 1 automation (Tasks 1-5):** 4-5 hours
- All file types
- Document editor
- File organization
- Unified CLI
- Auto-indexing
- **Result:** Fully automated Enigma Phase 1

---

## 📊 WHAT YOU'LL HAVE AFTER EACH TASK

**After Task 1:**
- ✅ PDFs searchable
- ✅ Word docs searchable
- ✅ All your research indexed

**After Task 2:**
- ✅ Product Genome editing automated
- ✅ Writing Standard enforced
- ✅ Hours saved weekly

**After Task 3:**
- ✅ Files auto-organized
- ✅ No more scattered downloads

**After Task 4:**
- ✅ Clean CLI interface
- ✅ Professional feel

**After Task 5:**
- ✅ Fully automated indexing
- ✅ Add file → instantly searchable

---

## 🎯 SUCCESS CRITERIA

**Phase 1 is "done" when:**
1. ✅ All file types (MD, PDF, DOCX) indexed and searchable
2. ✅ Can query any document in Enigma folder
3. ✅ Word document editing works
4. ✅ Product Genome chapters can be refined automatically
5. ✅ Using Enigma daily for real work (not just testing)

---

## 💡 RECOMMENDATION

**Start with Task 1 (File Support) - 30-45 minutes**

Why:
- Fastest value
- Enables everything else
- Your research becomes searchable immediately
- Then build Task 2 (editor) for Product Genome

**Want me to build Task 1 now?**

I can extend the indexer to support Word and PDF files in the next 30 minutes, then you can add all your files and query them.

---

**What would you like to tackle first?**
1. Task 1: File type support (Word + PDF)
2. Task 2: Word document editor
3. Add your files manually first, then decide

Let me know and I'll start building!
