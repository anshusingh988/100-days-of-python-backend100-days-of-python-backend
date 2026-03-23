from backend.models import init_db, add_job
from backend.recommender import RecommenderSystem

def seed():
    print("Initializing Database...")
    init_db()
    
    print("Loading AI Model...")
    recommender = RecommenderSystem()
    
    jobs = [
        {
            "title": "Python Backend Developer",
            "description": "We are looking for a Python developer with experience in FastAPI and PostgreSQL.",
            "skills": ["Python", "FastAPI", "PostgreSQL", "Docker", "AWS"]
        },
        {
            "title": "Frontend Engineer (React)",
            "description": "Join our frontend team. Must know React, TypeScript, and TailwindCSS.",
            "skills": ["React", "TypeScript", "TailwindCSS", "Redux"]
        },
        {
            "title": "Data Scientist",
            "description": "Analyze large datasets using Python, Pandas, and Scikit-Learn.",
            "skills": ["Python", "Pandas", "Scikit-Learn", "Machine Learning", "SQL"]
        }
    ]
    
    print("Seeding Jobs...")
    for job in jobs:
        # Create a text representation for embedding
        text_to_embed = f"{job['title']} {job['description']} {' '.join(job['skills'])}"
        embedding = recommender.get_embedding(text_to_embed)
        
        add_job(job['title'], job['description'], job['skills'], embedding)
        print(f"Added: {job['title']}")
        
    print("Seeding Complete!")

if __name__ == "__main__":
    seed()
