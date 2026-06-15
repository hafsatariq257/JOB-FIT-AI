import os
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Ensure environment variables from .env are accessible
load_dotenv()

def calculate_semantic_match(resume_text: str, job_description: str) -> dict:
    """
    Analyzes profile alignment against corporate job requirements using LLM inference.
    Returns a structured dictionary containing KPIs and analytical feedback.
    """
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("System Missing Component: GROQ_API_KEY is not configured in the environment.")

    # Initialize the high-speed inference client
    # Updated to llama-3.3-70b-versatile for up-to-date reasoning performance
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,  # Low temperature keeps metrics consistent and deterministic
        model_kwargs={"response_format": {"type": "json_object"}} # Force structural JSON response
    )

    # Construct an enterprise-grade evaluation prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an elite corporate Technical Recruiter and Talent Acquisition Specialist.\n"
            "Analyze the provided Resume against the Job Description and execute a strict semantic match evaluation.\n"
            "You must respond ONLY with a raw JSON object matching this schema exactly:\n"
            "{{\n"
            '  "match_percentage": int (0 to 100),\n'
            '  "matched_skills": ["skill1", "skill2", ...],\n'
            '  "missing_skills": ["skill1", "skill2", ...],\n'
            '  "alignment_summary": "A precise 2-3 sentence executive structural summary of why the candidate does or does not align with this position."\n'
            "}}\n"
            "Do not include any conversational text or markdown code blocks before or after the JSON."
        )),
        ("human", "RESUME:\n{resume}\n\n---\n\nJOB DESCRIPTION:\n{jd}")
    ])

    # Chain orchestration
    chain = prompt | llm

    try:
        response = chain.invoke({"resume": resume_text, "jd": job_description})
        
        # Safely parse the strict string response into a clean Python dictionary
        result_data = json.loads(response.content)
        return result_data
        
    except Exception as e:
        # Fallback dictionary to prevent the UI framework from breaking on exception
        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": ["Pipeline Processing Failure"],
            "alignment_summary": f"An error occurred during system pipeline execution: {str(e)}"
        }