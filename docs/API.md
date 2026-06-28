# API Documentation

## GET /health

Returns service health status.

## POST /jobs

Creates a mock background job and returns queue metadata.

## GET /jobs/{job_id}

Returns the current status of a background job.

## Example Job Response

```json
{
  "job_id": "generated-uuid",
  "status": "queued",
  "job_type": "email_delivery",
  "priority": "high",
  "queue": "high_priority"
}
