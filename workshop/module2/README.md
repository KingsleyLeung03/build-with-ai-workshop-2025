# Module 2: Adding Function Calling Capabilities

In this module, you'll learn how to make your Gemini agent smarter by giving it the ability to call functions. This will allow it to perform actions and retrieve information that it wouldn't normally have access to.

## Concepts

### 1. Function Declarations

A function declaration tells \n🤖 Gemini:

- What the function is called
- What it does
- What parameters it expects
- What types those parameters should be

Here's an example of a function declaration:

```python
get_stock_price_declaration = {
    "name": "get_stock_price",
    "description": "Get current stock price for a company",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol (e.g. AAPL, GOOGL)"
            }
        },
        "required": ["symbol"]
    }
}
```

### 2. Function Implementation

The function implementation is the actual Python code that gets executed when Gemini decides to call the function:

```python
def get_stock_price(symbol: str) -> dict:
    """Gets the current stock price for a company."""
    # Dummy implementation returning static values
    return {
        "symbol": symbol,
        "price": 142.50,
        "currency": "USD",
        "change": +1.25,
        "volume": 1250000
    }
```

### 3. Tools Configuration

To make Gemini aware of the functions it can use, you need to add them to the configuration:

```python
config = GenerateContentConfig(
    tools=[Tool(function_declarations=[get_temperature_declaration])],
    system_instruction=SYSTEM_PROMPT,
)
```

### 4. Processing Function Calls

When Gemini decides to call a function, you need to:

1. Process the function call
2. Execute the appropriate function
3. Return the result to Gemini
4. Let Gemini formulate a final response based on the function's result

## Exercise: Add temperature Function to Your Agent

Your task is to:

1. Create a function declaration for `get_temperature`
2. Implement the `get_temperature` function
3. Update the agent to handle function calls
4. Update the system prompt to guide Gemini on when to use the function
5. Test your agent with temperature-related queries

## Getting Started

1. Navigate to the `starter` directory
2. Open `main.py` and `tools.py`
3. Follow the TODO comments to complete the exercise

## Testing Your Solution

Run your agent and try these queries:

- "What's the temperature in San Francisco?"
- "Is it raining in New York right now?"
- "Should I bring an umbrella in London today?"
- "What's the temperature in Tokyo?"

## Solution

Once you've completed the exercise, you can check the `solution` directory to compare your implementation.
