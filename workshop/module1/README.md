# Module 1: Setting Up Your First Gemini Chat Agent

In this module, you'll learn how to create your first chat agent using Google's Gemini API. This agent will be able to hold a conversation, remember context, and respond to various queries.

## Concepts

### 1. The Gemini API

Gemini is Google's multimodal AI model that can process text, images, and other types of data. In this workshop, we'll focus on its text capabilities. Key aspects:

- It's a large language model (LLM) that understands and generates human language
- It can remember conversation context to have natural dialogues
- It can be guided by system prompts to behave in specific ways

### 2. System Prompts

A system prompt gives the model instructions about how to behave. It's like giving a character to the AI. For example:

```python
SYSTEM_PROMPT = """You are a helpful assistant specialized in weather information.
Always be friendly, concise, and accurate in your responses."""
```

### 3. Conversation History

Gemini remembers previous exchanges in a conversation through the "contents" parameter. This allows it to understand context like:

```
User: What's the capital of France?
AI: Paris is the capital of France.
User: What's its population?
AI: The population of Paris is approximately 2.2 million people.
```

## Exercise: Build a Basic Chat Agent

Your task is to:

1. Set up a Gemini client with your Gemini API Key
2. Create a chat loop that maintains conversation history
3. Implement a system prompt to give your agent a personality
4. Test your agent with multi-turn conversations

## Getting Started

1. Navigate to the `starter` directory
2. Open `main.py`
3. Follow the TODO comments to complete the exercise

## Testing Your Solution

Run your agent and try these conversations:
- Ask a question, then follow up with a related question using pronouns ("it", "that", etc.)
- Ask the agent to remember something, then refer to it later
- Ask the agent to explain a complex topic in simple terms

## Solution

Once you've completed the exercise, you can check the `solution` directory to compare your implementation. 