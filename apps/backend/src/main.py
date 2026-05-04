from fastapi import FastAPI
from redis import Redis
import os

app = FastAPI()
redis = Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "backend"}

@app.get("/counter")
def get_counter():
    count = redis.get("visit_count") or 0
    return {"count": int(count)}

@app.post("/counter")
def increment_counter():
    count = redis.incr("visit_count")
    return {"count": count}