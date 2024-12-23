from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.jobs.tasks import sample_task, another_task
import atexit


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Add periodic jobs
    scheduler.add_job(sample_task, IntervalTrigger(seconds=600), id="sample_task", replace_existing=True)
    scheduler.add_job(another_task, IntervalTrigger(minutes=30), id="another_task", replace_existing=True)
    
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())
