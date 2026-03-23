from fastapi import FastAPI, UploadFile, File
from backend.recommender import RecommenderSystem
from backend.models import init_db, get_all_jobs
from backend.resume_parser import parse_resume
from backend.skills import extract_skills, analyze_gap

app = FastAPI(title="Job Recommendation Agent")

# Initialize DB and Recommender
init_db()
recommender = RecommenderSystem()

@app.get("/")
def read_root():
    return {"message": "Job Recommendation API is running"}

@app.post("/analyze_resume")
async def analyze_resume(file: UploadFile = File(...)):
    contents = await file.read()
    text = parse_resume(contents, file.filename)
    
    if not text:
        return {"error": "Could not extract text from resume"}
    
    # Extract Skills
    user_skills = extract_skills(text)
    
    # Generate embedding
    user_embedding = recommender.get_embedding(text)
    
    # Get all jobs
    all_jobs = get_all_jobs()
    
    # Find matches
    matches = recommender.find_best_matches(user_embedding, all_jobs, top_k=5)
    
    results = []
    for job, score in matches:
        missing_skills, match_pct = analyze_gap(user_skills, job['skills'])
        results.append({
            "job_title": job['title'],
            "company": "Tech Corp", # Placeholder
            "description": job['description'],
            "match_score": round(score * 100, 1),
            "missing_skills": missing_skills,
            "required_skills": job['skills']
        })
    
    return {
        "user_skills": user_skills,
        "recommendations": results
    }

@app.get("/jobs")
def get_jobs():
    return get_all_jobs()

