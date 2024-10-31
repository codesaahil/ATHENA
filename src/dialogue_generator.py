import os
import json
import google.generativeai as genai
from google.generativeai.protos import Schema, Type
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You are a human writer. You can write dialogues, emotions, and actions for all kinds of NPCs "
        "in a video game. Please use memory carefully. Also if someone addresses you. Pretend to be a human."
        "Be sure to give creative and varied responses and not to repeat yourself."
    ),
)


def _generate_description(context: dict, additional_info: str = "") -> str:
    """Generates a description string for schemas using context."""
    return (
        f"{additional_info} NPC's permanent memory: {context['permanent_memory']}. "
        f"Memory of this conversation: {context['conversation_memory']}."
    )


def create_response_schema(context: dict) -> Schema:
    return Schema(
        type=Type.STRING,
        description=_generate_description(context, "The response of the dialogue. ")
        + f"The NPC's current emotion is {context['emotion']}. "
        + f"The NPC's personality is {context['personality']}",
    )


def create_emotion_schema(context: dict) -> Schema:
    return Schema(
        type=Type.OBJECT,
        properties={
            emotion: Schema(
                type=Type.NUMBER,
                description=f"How {emotion} the NPC is from 0.0 to 1.0",
            )
            for emotion in [
                "happiness",
                "sadness",
                "anger",
                "disgust",
                "fear",
                "surprise",
            ]
        },
        description=_generate_description(
            context, "The emotion of the NPC after this conversation part."
        ),
        required=["happiness", "sadness", "anger", "disgust", "fear", "surprise"],
    )


def create_action_schema(context: dict) -> Schema:
    return Schema(
        type=Type.OBJECT,
        properties={
            action: Schema(type=Type.BOOLEAN, description=description)
            for action, description in context["actions"].items()
        },
        description=_generate_description(
            context, "The NPC's actions after this conversation part. "
        ),
        required=list(context["actions"].keys()),
    )


def create_tags_schema(context: dict) -> Schema:
    return Schema(
        type=Type.STRING,
        description=_generate_description(
            context, "Descriptive tags for the conversation till now."
        ),
    )


def create_schema(context: dict) -> Schema:
    return Schema(
        type=Type.OBJECT,
        properties={
            "response": create_response_schema(context),
            "emotion": create_emotion_schema(context),
            "action": create_action_schema(context),
            "tags": create_tags_schema(context),
        },
        description="The NPC will respond. Update its emotion and perform an action.",
        required=["response", "emotion", "action"],
    )


def generate_response(prompt: str, context: dict) -> dict:
    schema = create_schema(context)
    response = model.generate_content(
        contents=prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=schema
        ),
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    )
    return json.loads(response.text)
