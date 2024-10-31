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


def create_schema(context: dict) -> Schema:
    response_schema = Schema(
        type=Type.STRING,
        description=f"The response of the dialogue. The NPC's memory is {context["memory"]}. The NPC's current emotion is {context["emotion"]}. The NPC's personality is {context["personality"]}",
    )
    emotion_schema = Schema(
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
        description=f"The emotion of the npc after this part of the converstation.",
        required=["happiness", "sadness", "anger", "disgust", "fear", "surprise"],
    )

    action_schema = Schema(
        type=Type.OBJECT,
        properties={
            action: Schema(type=Type.BOOLEAN, description=description)
            for action, description in context["actions"].items()
        },
        description=f"The action of the npc after this part of the conversation. 'true' for actions to do and 'false' for the ones not to do",
    )

    schema = Schema(
        type=Type.OBJECT,
        properties={
            "response": response_schema,
            "emotion": emotion_schema,
            "action": action_schema,
        },
        description="The NPC will respond. Update its emotion and perform an action.",
        required=["response", "emotion", "action"],
    )

    return schema


def generate_response(prompt: str, context: dict) -> dict:
    schema = create_schema(context)

    response = model.generate_content(
        contents=prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=schema
        ),
    )

    return json.loads(response.text)
