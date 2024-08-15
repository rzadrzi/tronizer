import asyncio
from tasks import collector, balance_checker
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def collector_scheduler():
    asyncio.Queue()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(collector, 'interval', seconds=50)
    scheduler.start()


async def balance_scheduler():
    asyncio.Queue()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(balance_checker, 'interval', seconds=50)
    scheduler.start()
