import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key and api_key != "your_api_key_here":
    genai.configure(api_key=api_key)

def analyze_task(task_title):
    if not api_key or api_key == "your_api_key_here":
        return {
            "category": "Uncategorized",
            "priority": "Medium",
            "subtasks": []
        }
    
    prompt = f'''
    Analyze the following to-do list task: "{task_title}"
    Break it down into 3-5 actionable subtasks if it's a large task.
    Assign a category (Work, Personal, Urgent, Health, etc.).
    Assign a priority (High, Medium, Low).
    
    Return the response strictly as a JSON object with this exact structure:
    {{
        "category": "string",
        "priority": "string",
        "subtasks": ["subtask 1", "subtask 2"]
    }}
    '''
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        import json
        text = response.text.strip()
        if text.startswith('`json'):
            text = text[7:-3]
        elif text.startswith('`'):
            text = text[3:-3]
        return json.loads(text)
    except Exception as e:
        print(f"Error calling AI: {e}")
        return {
            "category": "Uncategorized",
            "priority": "Medium",
            "subtasks": []
        }
