import vertexai

from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv
import os
from loguru import logger


STORY_PROMPT = """
Write a short (1 paragraph) adventure story that includes the following inputs as details:
"""

# get the environment variables
def get_envs() -> dict[str, str]:
    load_dotenv()
    config = {}
    config["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    config["PROJECT_ID"] = os.getenv("PROJECT_ID")
    config["REGION"] = os.getenv("REGION")
    return config


# get the story inputs from the user
def get_input() -> dict[str, str]:
    name = input("What is your name?")
    worst_enemy = input("What is your worst enemy’s name?")
    superpower = input("What is your superpower?")
    where_do_you_live = input("Where do you live?")
    favorite_food = input("What is your favorite food?")

    all_inputs = {
        "name": name,
        "worst_enemy": worst_enemy,
        "superpower": superpower,
        "where_do_you_live": where_do_you_live,
        "favorite_food": favorite_food,
    }
    return all_inputs


# going to make this task a bit more complex by using an LLM to generate the story
def main():
    logger.debug("Getting environment variables")
    configs: dict[str, str] = get_envs()

    logger.debug("Getting story inputs from user")
    inputs: dict[str, str] = get_input()

    logger.debug("Initializing VertexAI client")
    vertexai.init(project=configs["PROJECT_ID"], location=configs["REGION"])

    logger.debug("Initializing Gemini model")
    model = GenerativeModel("gemini-1.5-flash-002")

    inputs_str = "\n".join([f"{key}: {value}" for key, value in inputs.items()])

    logger.debug("Generating story")
    input_prompt = STORY_PROMPT + "\n" + inputs_str
    responses = model.generate_content(input_prompt, stream=False)

    logger.debug("Printing story")
    logger.info(responses.text)


if __name__ == "__main__":
    main()
