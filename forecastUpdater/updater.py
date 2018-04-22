from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecast_api


def test():
    now = datetime.now()
    print("\nTEST AT {t.hour}:{t.minute}:{t.second}\n".format(
        t=now
    ))
        
def start():
        scheduler = BackgroundScheduler()
        # scheduler.configure(jobstores=jobstores)
        scheduler.add_job(forecast_api.update_forecast, 'interval', minutes=5)
        scheduler.start()
    