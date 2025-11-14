# Build with AI: Create Agents with the OpenAI Agents SDK
This repository contains the Python code examples from the LinkedIn Learning course **Build with AI: Create Agents with the OpenAI Agents SDK**. The full course can be found on [LinkedIn Learning](https://www.linkedin.com/learning/build-with-ai-create-agents-with-the-openai-agents-sdk/).

![Build with AI: Create Agents with the OpenAI Agents SDK](https://github.com/LinkedInLearning/build-with-ai-create-agents-with-the-openai-agents-sdk-ugc-4740011/blob/main/course_image.png)

You’ll learn how to:
- Build and configure an AI travel agent using the OpenAI Agents SDK in Python.
- Integrate tools that allow your agent to connect to external data sources and perform real-world tasks.
- Design a multi-agent workflow using handoffs so agents can collaborate and delegate specialized tasks.
- Implement guardrails, sessions, and tracing to ensure your agent is safe, reliable, and easy to monitor.
- Identify ways to extend your AI travel agent with additional features, data sources, and user experiences.

## Requirements
- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

## Setup

1. **Clone this repo** (or download the files).
2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Set your OpenAI API key or place in .env file**:
    ```bash
    export OPENAI_API_KEY="your_api_key"      # macOS/Linux
    setx OPENAI_API_KEY "your_api_key"        # Windows PowerShell
    ```

## Running the Examples

Run the main demo script to see all lessons in action:

```bash
python agent.py
