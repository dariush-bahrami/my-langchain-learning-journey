# My LangChain Learning Journey 📖

## Installation

Use `poetry` to install the dependencies.

```bash
poetry install
```

## Deployment

Use `uvicorn` to run the `FastAPI` application. For example to run the application on
port _8000_, use the following command:

```bash
uvicorn my_langchain_learning_journey.web_api:app --host "0.0.0.0" --port 8000
```

## Developed Applications

I will update this section with the applications I develop during my learning journey.

### Translation Service

I used [Ollama](https://ollama.com/) and the [aya](https://ollama.com/library/aya) language model to create a translation service. The path was added to the API using langserve. The service can be accessed at the `/translate` endpoint. Additionally, you can interact with the service using the `/translate/playground` endpoint. The main source for this project was [this](https://python.langchain.com/v0.2/docs/tutorials/llm_chain/) awesome tutorial from LangChain. What I learned from this project:

- How to use prompt template from messages to achieve desired functionality.
- How to use string parser to get the text from the language model response.
- How to chain multiple component in LangChain.
- How to use langserve to add a chain to an existing fastapi application.
