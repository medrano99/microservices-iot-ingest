from fastapi import FastAPI
import router
import asyncio

app = FastAPI(
    title="REST API with Kafka, FastAPI and MongoDB",
    description="This is a simple microservice arquitecture of iot data ingestion",
    version="1.0"
)

@app.get('/')
async def Home():
    return "welcome to home iot hub"

app.include_router(router.route)
asyncio.create_task(router.consume())
