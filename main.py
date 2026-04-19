from fastapi import FastAPI, UploadFile, File, HTTPException
from graph.workflow import build_graph
from utils.pdf_parser import extract_pages

app = FastAPI()

graph = None  # global graph


# ✅ Build graph only when server starts
@app.on_event("startup")
def startup_event():
    global graph
    print("🚀 Building LangGraph...")
    graph = build_graph()
    print("✅ Graph ready")


# ✅ Health check (VERY IMPORTANT)
@app.get("/")
def home():
    return {"status": "Server is running"}


# ✅ Main API
@app.post("/api/process")
async def process_claim(claim_id: str, file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()

        pages = extract_pages(pdf_bytes)

        result = graph.invoke({
            "claim_id": claim_id,
            "pages": pages
        })

        return {
            "claim_id": claim_id,
            "output": result.get("final_output", "No output")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
