import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Job Matcher", layout="wide")

st.title("AI-Powered Job Recommendation System")

st.sidebar.header("User Profile")
# resume_text = st.sidebar.text_area("Paste Resume Text Here") # simplified for now
uploaded_file = st.sidebar.file_uploader("Upload PDF Resume", type=["pdf", "txt"])

if uploaded_file and st.sidebar.button("Analyze & Find Jobs"):
    with st.spinner("Analyzing resume and finding matches..."):
        try:
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(f"{API_URL}/analyze_resume", files=files)
            
            if response.status_code == 200:
                data = response.json()
                user_skills = data.get("user_skills", [])
                recommendations = data.get("recommendations", [])
                
                st.sidebar.success(f"Extracted {len(user_skills)} skills")
                st.sidebar.write(f"Skills: {', '.join(user_skills)}")
                
                st.header(f"Top {len(recommendations)} Job Recommendations")
                
                for job in recommendations:
                    with st.expander(f"{job['job_title']} - {job['match_score']}% Match", expanded=True):
                        st.subheader(job['job_title'])
                        st.write(job['description'])
                        st.progress(job['match_score'] / 100)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("✅ **Matching Skills**")
                            # We can infer match from required - missing, or just list required
                            st.write(", ".join(job['required_skills']))
                        
                        with col2:
                            if job['missing_skills']:
                                st.error(f"❌ **Missing Skills**: {', '.join(job['missing_skills'])}")
                            else:
                                st.success("🎉 You have all required skills!")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Connection Error: {e}")

st.header("Job Feed")
if 'recommendations' not in locals():
    st.write("Upload a resume to see recommendations.")
