from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from data_loader import load_csvs
from query_engine import generate_code
from executor import safe_execute

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your React URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load all CSVs at startup
dataframes = load_csvs()

# API Request Model
class QueryRequest(BaseModel):
    question: str

# API Endpoint
@app.post("/query")
def query(request: QueryRequest):
    code = generate_code(request.question, dataframes)
    result = safe_execute(code, dataframes)
    return {"code": code, "result": result}
