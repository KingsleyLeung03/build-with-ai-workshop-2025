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

# Function declaration for get_current_location
get_current_location_declaration = {
    "name": "get_current_location",
    "description": "Gets the user's current location (city and country)",
}

# Function declaration for convert_temperature
convert_temperature_declaration = {
    "name": "convert_temperature",
    "description": "Converts a temperature between Celsius and Fahrenheit",
    "parameters": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "number",
                "description": "The temperature value to convert",
            },
            "from_unit": {
                "type": "string",
                "description": "The original unit ('celsius' or 'fahrenheit')",
                "enum": ["celsius", "fahrenheit"],
            },
            "to_unit": {
                "type": "string",
                "description": "The target unit ('celsius' or 'fahrenheit')",
                "enum": ["celsius", "fahrenheit"],
            },
        },
        "required": ["temperature", "from_unit", "to_unit"],
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


# Get current location function implementation
def get_current_location() -> Dict[str, str]:
    """
    Simulates getting the user's current location.

    Returns:
        Dict[str, str]: A dictionary containing the user's current city and country
    """
    # In a real application, this would use GPS or IP geolocation
    # For this workshop, we'll return a fixed location
    return {"city": "Auckland", "country": "New Zealand"}


# Convert temperature function implementation
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
    # Normalize units to lowercase
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Validate units
    if from_unit not in ["celsius", "fahrenheit"] or to_unit not in [
        "celsius",
        "fahrenheit",
    ]:
        raise ValueError("Units must be 'celsius' or 'fahrenheit'")

    # If units are the same, no conversion needed
    if from_unit == to_unit:
        return {"temperature": temperature, "unit": to_unit}

    # Convert temperature
    if from_unit == "celsius" and to_unit == "fahrenheit":
        # C to F: (C × 9/5) + 32
        converted = (temperature * 9 / 5) + 32
    else:
        # F to C: (F - 32) × 5/9
        converted = (temperature - 32) * 5 / 9

    return {"temperature": round(converted, 1), "unit": to_unit}
