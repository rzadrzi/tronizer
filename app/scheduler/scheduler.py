import asyncio
from tasks import collector
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def collector_scheduler():
    asyncio.Queue()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(collector, 'interval', seconds=50)
    scheduler.start()
