import vertexai
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv
import os


def get_envs():
    load_dotenv()
    config = {}
    config["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    return config


def main():
    configs = get_envs()

    vertexai.init(project=configs["GOOGLE_API_KEY"])

    model = GenerativeModel("gemini-1.5-flash-latest")

    response = model.generate_content("Hello, world!")

    print(response.text)


if __name__ == "__main__":
    main()