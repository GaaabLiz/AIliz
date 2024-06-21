import json

from core.api.dto.ollama_response import OllamaResponse


def clean_response(response: str) -> str:
    # Remove the backticks and the "json" prefix from the response string
    cleaned_response = response.strip("`")
    if cleaned_response.lower().startswith("json"):
        cleaned_response = cleaned_response[4:].strip()
    # Remove the remaining backticks and newline characters
    cleaned_response = cleaned_response.replace("```", "").strip()
    return cleaned_response



# read file
with open("../notes/test2.json", "r") as file:
    prompt = file.read()


print(prompt)
print("\n\n")
temp = clean_response(prompt)
temp2 = json.loads(temp)
print(temp2["tags"])