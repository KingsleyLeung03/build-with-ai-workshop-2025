# Module 3: Chaining Functions Together

In this module, you'll learn how to create more sophisticated agents by chaining multiple functions together. This allows Gemini to solve complex queries by combining information from different sources.

## Concepts

### 1. Function Chaining

Function chaining means having Gemini call multiple functions in sequence to solve a single query. For example:

```
User: "What's the weather like in my current location?"

get_current_location() -> "San Francisco"
get_weather(location="San Francisco") -> Weather data for San Francisco
```

### 2. Conversation Context

When a function returns a result, it's added to the conversation history. Gemini can then use this information to:

- Decide what function to call next
- Fill in parameters for the next function
- Formulate a final response that combines all the information

### 3. System Prompts for Chaining

Your system prompt should guide Gemini on how to chain functions:

```python
SYSTEM_PROMPT = """When a user asks about weather in their current location:
1. First call get_current_location() to find the user's location
2. Then call get_weather() using that location as the parameter
3. Combine the information to give a complete answer
"""
```

### 4. Dependencies Between Functions

Some functions depend on the results of others. For example:

- `get_current_location()` → Returns a location
- `get_weather(location)` → Needs a location parameter
- `convert_temperature(temperature, from_unit, to_unit)` → Needs a temperature value

## Exercise: Build an Agent with Function Chaining

Your task is to:

1. Add a `get_current_location` function that returns the user's location
2. Add a `convert_temperature` function to convert between Celsius and Fahrenheit
3. Update the system prompt to guide Gemini on chaining these functions
4. Implement function chaining in the main application
5. Test your agent with complex queries that require multiple function calls

## Getting Started

1. Navigate to the `starter` directory
2. Open `main.py` and `tools.py`
3. Follow the TODO comments to complete the exercise

## Testing Your Solution

Run your agent and try these queries:

- "What's the weather in my current location?"
- "What's the temperature where I am in Fahrenheit?"
- "Should I wear a coat today?"
- "Is Tokyo warmer than my current location right now?"

## Solution

Once you've completed the exercise, you can check the `solution` directory to compare your implementation.
