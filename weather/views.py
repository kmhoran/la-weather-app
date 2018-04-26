import decimal
from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.generic import TemplateView
from weather.models import Forecast
from forecastUpdater import forecast_api

    

class MainPage(TemplateView):
    def get(self, request, **kwargs):
        
        latest_forecast = Forecast.objects.latest('timestamp')
        print("###########################################")
        print(latest_forecast.timestamp)
        ptint( type(latest_forecast.timestamp)
        # db_timestamp = datetime.datetime.fromtimestamp(latest_forecast.timestamp)
        # Because Heroku Hobby Tier goes to sleep after inactivity
        if latest_forecast is None: #or db_timestamp < (datetime.now() - timedelta(hours=1)):
            #forecast_api.update_forecast()
            #latest_forecast = Forecast.objects.latest('timestamp')
            pass

        city = latest_forecast.city
        temperature_in_c = latest_forecast.temperatue
        temperature_in_f = (latest_forecast.temperatue * decimal.Decimal(1.8)) + 32
        description = latest_forecast.description.capitalize
        timestamp = "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{t.minute:02d}:{t.second:02d}".format( t=latest_forecast.timestamp)


        return render(
            request, 
            'index.html', 
            {
                'city':city,
                'temperature_in_c': temperature_in_c,
                'temperature_in_f': round(temperature_in_f,2),
                'desctiprion': description,
                'utc_update_time': timestamp})
