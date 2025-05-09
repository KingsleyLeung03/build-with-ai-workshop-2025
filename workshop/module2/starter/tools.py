"""
This module contains function declarations and implementations for the Gemini function calling workshop.
"""

from typing import Dict, Union

# TODO: Create a function declaration for get_weather
# The declaration should include:
# - name: The name of the function
# - description: What the function does
# - parameters: What parameters the function takes, their types, and descriptions
# - required: Which parameters are required

# Example declaration format:
# function_declaration = {
#     "name": "function_name",
#     "description": "Description of what the function does",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "param_name": {
#                 "type": "string",
#                 "description": "Description of the parameter"
#             }
#         },
#         "required": ["param_name"]
#     }
# }
get_weather_declaration = {
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
    # TODO: Implement the weather function
    # 1. Convert the location to lowercase
    # 2. Create a dictionary of weather data for different cities
    # 3. Return the weather data for the requested location
    # 4. Include a default response for unknown locations
    #
    # Example implementation:
    # weather_data = {
    #     "auckland": {
    #         "temperature": 18,
    #         "condition": "sunny",
    #         "humidity": 45,
    #         "wind_speed": 8,
    #         "unit": "celsius"
    #     },
    #     # Add more cities...
    # }
    pass
