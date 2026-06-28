def process_job(job):
    try:
        return {
            "job_id": job.get("job_id"),
            "status": "completed",
            "result": "Job processed successfully.",
        }
    except Exception:
        return {
            "job_id": job.get("job_id"),
            "status": "failed",
            "retry": True,
        }
