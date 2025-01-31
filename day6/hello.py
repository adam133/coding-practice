from dotenv import load_dotenv
import os
from loguru import logger
import re
import hashlib


# Note: This should not be used for actual authentication - this is just a practice exercise
# This is not secure and should not be used in production
def get_envs() -> dict[str, str]:
    load_dotenv()
    config = {}
    for key, value in os.environ.items():
        if key.endswith("_PASSWORD"):
            config[key] = value
    return config

# Note: This should not be used for actual authentication - this is just a practice exercise
# This is not secure and should not be used in production
def add_to_envs(env_name: str, env_value: str):
    with open(".env", "a") as f:
        f.write(f"{env_name}={env_value}\n")


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(config: dict[str, str], username: str, password: str) -> bool:
    hashed_password = hash_password(password)
    password_from_env = config.get(username.upper() + "_PASSWORD", False)
    if hashed_password == password_from_env:
        return True
    else:
        return False


def create_account(username: str, password: str):
    if len(password) < 8:
        logger.info("Password must be at least 8 characters long")
        return
    # verify password has a special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        logger.info("Password must have a special character")
        return
    hashed_password = hash_password(password)
    add_to_envs(username.upper() + "_PASSWORD", hashed_password)
    logger.info("Account created")


def main():
    logger.info("Hello from day6!")
    config = get_envs()

    username = input("What is your username: ")
    password = input("What is your password: ")

    if check_password(config, username, password):
        logger.info("Access granted")
    else:
        logger.info("Access denied")
        logger.info("Would you like to create an account?")
        create_account_input = input("Yes or No: ")
        if create_account_input.upper() == "YES":
            logger.info("Creating account...")
            create_account(username, password)
        else:
            logger.info("Goodbye!")

if __name__ == "__main__":
    main()
