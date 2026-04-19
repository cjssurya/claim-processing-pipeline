# 🏥 Claim Processing Pipeline (FastAPI + LangGraph)

## 🚀 Overview
This project processes insurance claim PDFs using a multi-agent architecture built with FastAPI and LangGraph.

---

## 🧠 Workflow

START → Segregator → ID Agent → Discharge Agent → Bill Agent → Aggregator → END

---

## 🔹 Components

### Segregator Agent
Classifies PDF pages into document types.

### ID Agent
Extracts patient details like name, DOB, policy number.

### Discharge Agent
Extracts diagnosis, admission & discharge dates, doctor.

### Bill Agent
Extracts billing items and total cost.

### Aggregator
Combines all extracted data into final JSON.

---

## ⚙️ Tech Stack

- FastAPI
- LangGraph
- PyMuPDF (fitz)
- pytesseract (OCR)

---

## 📡 API

POST `/api/process`

### Input:
- claim_id (string)
- PDF file

### Output:
```json
{
  "claim_id": "123",
  "patient": {...},
  "discharge_summary": {...},
  "billing": {...}
}
