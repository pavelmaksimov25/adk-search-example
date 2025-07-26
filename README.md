# ADK Search Example

A simple agent application built with Google's Agent Development Kit (ADK) that demonstrates agentic capabilities using the built-in search functionality.

## Installation

### Prerequisites

- Python 3.13 or higher
- Google ADK api key

### Getting Your API Key

To use this application, you'll need a Gemini API key from Google AI Studio:

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google Account
3. Generate a new API key for your project
4. Copy the API key - you'll need it for the configuration step below

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd adk-search-example
   ```

2. **Install dependencies:**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Configure environment:**
   ```bash
   # Copy the example environment file
   cp search_agent/.env.example search_agent/.env
   
   # Edit the .env file with your Google ADK credentials
   # Add your API key
   GOOGLE_API_KEY=your_api_key
   ```

## Usage


### Running the Agent

```bash
# Activate your environment
source venv/bin/activate  # or `uv shell` if using uv

# Run the search agent and follow the instructions
adk web
```

---

For more information about Google ADK, visit the [official documentation](https://google.github.io/adk-docs/get-started/quickstart/).
