#uses gemini to generate the word/sentence bank for the activity
#remember to have this follow the routes made in expo
#everytime a new activity is added a new json file needs to be made in /starter_data
#everytime a new section is added to an actvity its respected json file needs to be updated

from app.agent.gemini.client import get_gemini
import json
from pathlib import Path

def gen_activity(activity:str, section:str):
    current_dir = Path(__file__).parent

    #add folder for activities when adding implmentation for excercises
    activity_json = current_dir / "starter_data" / (activity + ".json")

    with open(activity_json, "r") as file:
        start_data = file.read()

    parsed_start_data = json.loads(start_data)

    client = get_gemini()
    prompt = f"""
                Using these directions, {parsed_start_data[section]["rules"]}
                generate a cluster that will children with their speech development.
                Only use words that exist in the English dictionary, are reasonable
                for a child to say, and is appropriate, especially for children.
                Incorporate levels of difficulty as indicated by:
                {parsed_start_data[section]["example-bank"]}

                The output should be formatted as such:
                {{
                    "1": ["Bat", "Cat", "Rat"],
                    "2": ["Chat", "Splat"]
                }} 

                Rules:
                - Only return valid JSON
                - Do not provide any explainations
                - Do not use any markdown
                - No extra text
                - Follow patterns set by the JSON file provided
                - Do not use any special characters
            """
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt, config={"response_mime_type": "application/json"})
    output = response.candidates[0].content.parts[0].text
    output = output.replace("```json", "").replace("```", "").strip()

    return json.loads(output)