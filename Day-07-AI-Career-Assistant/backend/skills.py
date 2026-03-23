import re

COMMON_SKILLS = [
    "Python", "Java", "JavaScript", "TypeScript", "React", "Angular", "Vue",
    "HTML", "CSS", "SQL", "NoSQL", "PostgreSQL", "MongoDB", "Redis",
    "Docker", "Kubernetes", "AWS", "Azure", "GCP",
    "Flask", "Django", "FastAPI", "Spring Boot", "Node.js",
    "Machine Learning", "Deep Learning", "Data Science", "Pandas", "NumPy", "Scikit-Learn",
    "Git", "CI/CD", "Linux", "REST API", "GraphQL"
]

def extract_skills(text):
    """
    Extracts skills from text using simple keyword matching (case-insensitive).
    """
    found_skills = []
    text_lower = text.lower()
    
    for skill in COMMON_SKILLS:
        # Use regex to match whole words to avoid partial matches (e.g. "Go" in "Good")
        # Escape skill to handle special chars like C++ or .js
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
            
    return found_skills

def analyze_gap(user_skills, job_skills):
    """
    Returns skills present in job matching but missing in user profile.
    """
    missing = [skill for skill in job_skills if skill not in user_skills]
    match_percentage = (len(job_skills) - len(missing)) / len(job_skills) if job_skills else 0
    return missing, match_percentage
