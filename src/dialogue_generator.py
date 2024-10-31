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
    "in a video game. Please use memory carefully.",
)


def create_response_schema(context: dict) -> Schema:
    return Schema(
        type=Type.STRING,
        description=f"The response of the dialogue. The NPC's permanent memory is {context["permanent_memory"]}. The NPC's memory of this conversation is {context["conversation_memory"]}. The NPC's current emotion is {context["emotion"]}. The NPC's personality is {context["personality"]}",
    )


def create_emotion_schema(context: dict) -> Schema:
    return Schema(
        type=Type.OBJECT,
        properties={
            "happiness": Schema(
                type=Type.NUMBER, description=f"How happy the NPC is from 0.0 to 1.0"
            ),
            "sadness": Schema(
                type=Type.NUMBER, description=f"How sad the NPC is from 0.0 to 1.0"
            ),
            "anger": Schema(
                type=Type.NUMBER, description=f"How angry the NPC is from 0.0 to 1.0"
            ),
            "disgust": Schema(
                type=Type.NUMBER,
                description=f"How disgusted the NPC is from 0.0 to 1.0",
            ),
            "fear": Schema(
                type=Type.NUMBER, description=f"How afraid the NPC is from 0.0 to 1.0"
            ),
            "surprise": Schema(
                type=Type.NUMBER,
                description=f"How surprised the NPC is from 0.0 to 1.0",
            ),
        },
        description=f"The emotion of the npc after this part of the converstation. The NPC's permanent memory is {context["permanent_memory"]}. The NPC's memory of this conversation is {context["conversation_memory"]}.",
        required=["happiness", "sadness", "anger", "disgust", "fear", "surprise"],
    )


def create_action_schema(context: dict) -> Schema:
    return Schema(
        type=Type.OBJECT,
        properties={
            action: Schema(type=Type.BOOLEAN, description=description)
            for action, description in context["actions"].items()
        },
        description=f"The action of the npc after this part of the conversation. The NPC's permanent memory is {context["permanent_memory"]}. The NPC's memory of this conversation is {context["conversation_memory"]}. 'true' for actions to do and 'false' for the ones not to do",
        required=context["actions"].keys(),
    )


def create_tags_schema(context: dict) -> Schema:
    return Schema(
        type=Type.STRING,
        description=f"The tags that are descriptive for the conversation till now. The NPC's permanent memory is {context["permanent_memory"]}. The NPC's memory of this conversation is {context["conversation_memory"]}.",
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
    )

    return json.loads(response.text)
