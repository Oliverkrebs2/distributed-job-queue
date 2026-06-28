import uuid


def submit_job(job_type: str, payload: dict, priority: str = "normal"):
    job_id = str(uuid.uuid4())

    return {
        "job_id": job_id,
        "status": "queued",
        "job_type": job_type,
        "priority": priority,
        "payload": payload,
        "queue": "high_priority" if priority == "high" else "default",
    }


def get_job_status(job_id: str):
    return {
        "job_id": job_id,
        "status": "processing",
        "attempts": 1,
        "max_attempts": 3,
        "worker": "worker-1",
    }
