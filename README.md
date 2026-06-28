# Distributed Job Queue

Distributed backend job queue with worker pools, retries, priority scheduling, dead-letter handling, and observability.

## What It Does

- Accepts background jobs through an API
- Places jobs into priority queues
- Processes jobs with worker pools
- Retries failed jobs
- Moves permanently failed jobs to a dead-letter queue
- Tracks job status and execution results
- Designed for scalable backend systems

## Tech Stack

- Python
- FastAPI
- Redis
- PostgreSQL
- Docker
- GitHub Actions

## System Flow

Client Request → Queue API → Redis Queue → Worker Pool → Retry Engine → Dead-Letter Queue → Metrics

## Use Cases

- Email delivery
- AI inference jobs
- Data processing
- Webhook processing
- Report generation
- Scheduled background tasks
