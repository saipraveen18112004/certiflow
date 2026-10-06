from fastapi import FastAPI

app = FastAPI(
    title="CertiFlow API",
    description="Bulk Certificate Generation API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "CertiFlow API is running"}