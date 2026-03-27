import random

def analyze_task(title):
    title_lower = title.lower()

    categories = {
        "Work": ["project", "study", "assignment", "code", "meeting"],
        "Health": ["gym", "exercise", "run", "yoga"],
        "Personal": ["buy", "shopping", "family", "call"],
    }

    category = "General"
    for cat, keywords in categories.items():
        if any(word in title_lower for word in keywords):
            category = cat
            break

    if any(word in title_lower for word in ["urgent", "asap", "deadline"]):
        priority = "High"
    elif category == "Work":
        priority = "High"
    elif category == "Health":
        priority = "Medium"
    else:
        priority = "Low"

    subtasks_templates = [
        f"Plan for {title}",
        f"Start {title}",
        f"Work on {title}",
        f"Review {title}",
        f"Complete {title}"
    ]

    subtasks = random.sample(subtasks_templates, 3)

    return {
        "category": category,
        "priority": priority,
        "subtasks": subtasks
    }