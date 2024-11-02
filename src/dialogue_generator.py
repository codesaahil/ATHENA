import os
import json
import google.generativeai as genai
from google.generativeai.protos import Schema, Type
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure the Generative AI model with the API key from the environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Generative Model with system instructions for NPC behavior
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You are a human writer. You can write dialogues, emotions, and actions for all kinds of NPCs "
        "in a video game. If someone addresses you, pretend to be the NPC."
    ),
)


def _generate_description(context: dict, info: str):
    return (
        f"{info}"
        f"The NPC's permanent memory is {context['permanent_memory']}."
        f"The NPC's conversation memory is {context['conversation_memory']}."
        f"The NPC's current emotion is {context['emotion']}."
        f"The NPC's personality is {context['personality']}."
        f"The NPC's possible actions are {context['actions']}"
    )


def create_dialogue_schema(context: dict) -> Schema:
    """
    Creates a schema for the NPC's response.

    Args:
        context (dict): A dictionary containing NPC context information.

    Returns:
        Schema: A schema object representing the response structure.
    """
    return Schema(
        type=Type.STRING,
        description=_generate_description(context, "The response of the dialogue."),
    )


def create_emotion_schema(context: dict) -> Schema:
    """
    Creates a schema for the NPC's emotions.

    Args:
        context (dict): A dictionary containing NPC context information.

    Returns:
        Schema: A schema object representing the emotion structure.
    """
    return Schema(
        type=Type.OBJECT,
        properties={
            emotion: Schema(
                type=Type.NUMBER,
                description=_generate_description(
                    context, f"How {emotion} the NPC is from 0.0 to 1.0"
                ),
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
        description="The emotion of the NPC after the conversation.",
        required=["happiness", "sadness", "anger", "disgust", "fear", "surprise"],
    )


def create_action_schema(context: dict) -> Schema:
    """
    Creates a schema for the NPC's actions.

    Args:
        context (dict): A dictionary containing NPC context information.

    Returns:
        Schema: A schema object representing the action structure.
    """
    return Schema(
        type=Type.OBJECT,
        properties={
            action: Schema(type=Type.BOOLEAN, description=description)
            for action, description in context["actions"].items()
        },
        description=_generate_description(
            context, "The NPC's actions after the conversation."
        ),
        required=list(context["actions"].keys()),
    )


def create_schema(context: dict) -> Schema:
    """
    Creates a comprehensive schema for the NPC's response, emotions, actions, and tags.

    Args:
        context (dict): A dictionary containing NPC context information.

    Returns:
        Schema: A schema object that aggregates response, emotion, action, and tags.
    """
    return Schema(
        type=Type.OBJECT,
        properties={
            "dialogue": create_dialogue_schema(context),
            "emotion": create_emotion_schema(context),
            "action": create_action_schema(context),
        },
        description=_generate_description(
            context, "The NPC will respond, update its emotion, and perform an action."
        ),
        required=["dialogue", "emotion", "action"],
    )


def generate_response(prompt: str, context: dict) -> dict:
    """
    Generates a response from the NPC based on the provided prompt and context.

    Args:
        prompt (str): The input prompt for the NPC's response.
        context (dict): A dictionary containing NPC context information.

    Returns:
        dict: A dictionary containing the generated response from the NPC.
    """
    schema = create_schema(context)  # Create a schema for the response
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
        },
    )
    # Parse and return the JSON response
    return json.loads(response.text)
