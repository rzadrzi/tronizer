import asyncio
from tasks import collect
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def collect_scheduler():
    asyncio.Queue()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(collect, 'interval', seconds=50)
    scheduler.start()
