"""
Weather service (mock for POC, ready for IMD API)
"""
import logging

logger = logging.getLogger(__name__)


class WeatherService:
    """Weather data integration"""
    
    def get_weather(self, location):
        """Get current weather"""
        # Mock data for POC
        return {
            'location': location,
            'temperature': 28,
            'humidity': 65,
            'rainfall': 0,
            'conditions': 'Partly cloudy',
            'wind_speed': 12
        }
    
    def get_forecast(self, location, days=7):
        """Get weather forecast"""
        forecast = []
        for i in range(days):
            forecast.append({
                'day': i + 1,
                'temperature': 28 + (i % 3),
                'rainfall': 0 if i < 3 else 5,
                'conditions': 'Clear' if i < 3 else 'Light rain'
            })
        return forecast
    
    def get_alerts(self, location):
        """Get weather alerts"""
        return []
