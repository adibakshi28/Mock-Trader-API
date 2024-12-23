from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from app.jobs.tasks import another_task, sync_stock_universe
from app.core.config import config
import atexit

# Note: APScheduler operates in a separate thread from the FastAPI event loop

def start_scheduler():
    scheduler = BackgroundScheduler()

    # Add periodic jobs
    scheduler.add_job(another_task, IntervalTrigger(minutes=30), id="another_task", replace_existing=True)
    scheduler.add_job(sync_stock_universe, CronTrigger(hour=1, minute=0, timezone=config["TIMEZONE"]), id="sync_stock_universe", replace_existing=True)

    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())
