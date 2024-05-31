from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def get_translation_chain(ollama_model_name: str = "aya"):
    # Create prompt template
    prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Translate the following from {source_language} into {destination_language}",
            ),
            ("user", "{text}"),
        ]
    )

    # Create chat model
    model = ChatOllama(model=ollama_model_name, temperature=0.0)

    # Create parser
    parser = StrOutputParser()

    # Create chain
    chain = prompt_template | model | parser

    return chain
