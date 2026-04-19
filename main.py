from fastapi import FastAPI, UploadFile, File

from graph.workflow import build_graph
from utils.pdf_parser import extract_pages

app = FastAPI()  # ✅ VERY IMPORTANT

graph = build_graph()


@app.post("/api/process")
async def process_claim(claim_id: str, file: UploadFile = File(...)):
    
    pdf_bytes = await file.read()

    pages = extract_pages(pdf_bytes)

    result = graph.invoke({
        "claim_id": claim_id,
        "pages": pages
    })

    return result["final_output"]