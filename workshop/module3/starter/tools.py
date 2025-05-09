"""
This module contains function declarations and implementations for the Gemini function calling workshop.
"""

from typing import Dict, Union, List

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

# TODO: Create a function declaration for get_current_location
# This function should:
# - Have a name "get_current_location"
# - Have a clear description
# - Take no parameters (it simulates getting the user's current location)
get_current_location_declaration = {
    # Fill in the declaration here
}

# TODO: Create a function declaration for convert_temperature
# This function should:
# - Have a name "convert_temperature"
# - Have a clear description
# - Take parameters:
#   - temperature: a number representing the temperature value
#   - from_unit: the original unit ('celsius' or 'fahrenheit')
#   - to_unit: the target unit ('celsius' or 'fahrenheit')
# - Make all parameters required
convert_temperature_declaration = {
    # Fill in the declaration here
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

    # Mock weather data for different cities
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
            "temperature": 20,  # Celsius
            "condition": "clear",
            "humidity": 50,
            "wind_speed": 10,
            "unit": "celsius",
        },
    )


# TODO: Implement the get_current_location function
# This function should return a dictionary with the user's current city and country
def get_current_location() -> Dict[str, str]:
    """
    Simulates getting the user's current location.

    Returns:
        Dict[str, str]: A dictionary containing the user's current city and country
    """
    # Implement the function here
    pass


# TODO: Implement the convert_temperature function
# This function should convert a temperature between Celsius and Fahrenheit
def convert_temperature(
    temperature: float, from_unit: str, to_unit: str
) -> Dict[str, Union[float, str]]:
    """
    Converts a temperature between Celsius and Fahrenheit.

    Args:
        temperature (float): The temperature value to convert
        from_unit (str): The original unit ('celsius' or 'fahrenheit')
        to_unit (str): The target unit ('celsius' or 'fahrenheit')

    Returns:
        Dict[str, Union[float, str]]: A dictionary containing the converted temperature and the unit
    """
    # Implement the function here
    pass
