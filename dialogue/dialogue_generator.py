import os
import json
import google.generativeai as genai
from google.generativeai.protos import Schema
from google.generativeai.protos import Type
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a human writer. You can write dialogues, emotions and actions for all kinds of NPCs"
    "in a video game.",
)


def create_schema() -> Schema:
    schema = Schema(
        type=Type.OBJECT,
        properties={
            "response": Schema(
                type=Type.STRING, description="The response of the dialogue."
            ),
            "emotion": Schema(type=Type.STRING, description="The emotion of the NPC."),
            "action": Schema(
                type=Type.STRING, description="The action performed by the NPC."
            ),
        },
        required=["response", "emotion", "action"],
    )

    return schema


def generate_response(prompt: str) -> dict:
    schema = create_schema()

    response = model.generate_content(
        contents=prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=schema
        ),
    )

    return json.loads(response.text)
