# llm-api

A lightweight API gateway that forwards prompts to a local LLM via Ollama, built with FastAPI.

## Stack
- FastAPI
- httpx
- Ollama
- uv
- python-dotenv

## How to run

### 1. Install Ollama and pull a model
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:0.5b
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Configure environment
Create a `.env` file in the root of the project:

```env
MODEL_NAME=qwen2.5:0.5b
OLLAMA_URL=http://localhost:11434/api/generate
```

Change `MODEL_NAME` to any model you have installed in Ollama.

### 4. Start Ollama
```bash
ollama serve
```

### 5. Start the server
```bash
uv run uvicorn main:app --reload
```

### 6. Test it
Go to `http://localhost:8000/docs`

## Configuration

| Variable | Default | Description |
|---|---|---|
| `MODEL_NAME` | `qwen2.5:0.5b` | Ollama model to use |
| `OLLAMA_URL` | `http://localhost:11434/api/generate` | Ollama API endpoint |

## Example

Request:
```json
{"prompt": "hello, who are you?"}
```

Response:
```json
{
  "response": "Hi! I'm Qwen, an AI assistant created by Alibaba Cloud. How can I help you today?"
}
```