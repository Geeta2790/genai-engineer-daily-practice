import json
import time

from fastapi import FastAPI, HTTPException
import redis


# Step 1: Connect to Redis (local default)
cache = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

app = FastAPI()

CACHE_TTL_SECONDS = 30


# Step 2: Simulate a slow upstream call (e.g. a database or external API)
def slow_lookup(user_id: int):
    time.sleep(1)
    return {"user_id": user_id, "name": f"user-{user_id}", "plan": "pro"}


# Step 3: Cache-aside pattern — check Redis first, fall back on miss
@app.get("/users/{user_id}")
def get_user(user_id: int):
    key = f"user:{user_id}"

    cached = cache.get(key)
    if cached is not None:
        return {"source": "cache", "data": json.loads(cached)}

    data = slow_lookup(user_id)
    cache.setex(key, CACHE_TTL_SECONDS, json.dumps(data))
    return {"source": "db", "data": data}


# Step 4: Allow manual invalidation
@app.delete("/users/{user_id}/cache")
def invalidate(user_id: int):
    deleted = cache.delete(f"user:{user_id}")
    if not deleted:
        raise HTTPException(status_code=404, detail="no cached entry")
    return {"invalidated": user_id}


# Step 5: Inspect TTL
@app.get("/users/{user_id}/ttl")
def ttl(user_id: int):
    seconds = cache.ttl(f"user:{user_id}")
    return {"user_id": user_id, "ttl_seconds": seconds}
