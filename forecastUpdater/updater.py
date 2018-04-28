from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecast_api

        
def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(forecast_api.update_forecast, 'interval', minutes=45)
        scheduler.start()
    
