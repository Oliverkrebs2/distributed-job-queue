from fastapi import FastAPI

from app.queue import submit_job, get_job_status

app = FastAPI(title="Distributed Job Queue")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "distributed-job-queue"}


@app.post("/jobs")
def create_job():
    return submit_job(
        job_type="email_delivery",
        payload={"recipient": "user@example.com", "template": "welcome_email"},
        priority="high",
    )


@app.get("/jobs/{job_id}")
def read_job(job_id: str):
    return get_job_status(job_id)
