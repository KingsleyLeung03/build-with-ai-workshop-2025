"""
This module contains function declarations and implementations for the Gemini function calling workshop.
"""

from typing import Dict, Union

# Function declaration for get_weather
get_weather_declaration = {
    "name": "get_weather",
    "description": "Gets the current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name (e.g., 'San Francisco', 'New York', 'London')",
            }
        },
        "required": ["location"],
    },
}


# Weather function implementation
def get_weather(location: str) -> Dict[str, Union[int, str, float]]:
    """
    Gets the current weather for a given location.

    Args:
        location (str): The name of the city to get the weather for.

    Returns:
        Dict[str, Union[int, str, float]]: A dictionary containing weather information
    """
    # In a real application, this would call a weather API
    # For this workshop, we'll use mock data
    location = location.lower()

    # Mock weather data for different cities (temperatures in Celsius)
    weather_data = {
        "auckland": {
            "temperature": 18,
            "condition": "sunny",
            "humidity": 45,
            "wind_speed": 8,
            "unit": "celsius",
        },
        "wellington": {
            "temperature": 15,
            "condition": "partly cloudy",
            "humidity": 60,
            "wind_speed": 12,
            "unit": "celsius",
        },
        "sydney": {
            "temperature": 25,
            "condition": "sunny",
            "humidity": 50,
            "wind_speed": 10,
            "unit": "celsius",
        },
        "london": {
            "temperature": 10,
            "condition": "rainy",
            "humidity": 85,
            "wind_speed": 15,
            "unit": "celsius",
        },
        "tokyo": {
            "temperature": 22,
            "condition": "clear",
            "humidity": 40,
            "wind_speed": 5,
            "unit": "celsius",
        },
    }

    # Return weather data for the specified location, or a default if not found
    return weather_data.get(
        location,
        {
            "temperature": 20,
            "condition": "clear",
            "humidity": 50,
            "wind_speed": 10,
            "unit": "celsius",
        },
    )
