from flask import Flask, request, jsonify, send_file
import os
import traceback

from resume_parser import extract_text
from analyzer import find_skills
from ats_score import calculate_score
from job_match import match_jobs
from ai_analyzer import compare_resume_with_job


app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, "uploads")


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return send_file("uploads.html")


@app.route("/upload", methods=["POST", "OPTIONS"])
def upload_resume():
    print("Upload endpoint called")
    
    # Handle CORS preflight requests
    if request.method == "OPTIONS":
        response = app.make_default_options_response()
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        response.headers.update(headers)
        return response
    
    try:
        print("Checking for resume file...")
        if "resume" not in request.files:
            print("No resume file found")
            return jsonify({"error": "No resume selected"}), 400

        resume = request.files["resume"]
        print(f"Resume file: {resume.filename}")

        if resume.filename == "":
            print("Empty filename")
            return jsonify({"error": "Please select a resume"}), 400

        if not resume.filename.endswith(".pdf"):
            print("Not a PDF file")
            return jsonify({"error": "Only PDF files are allowed"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
        print(f"Saving file to: {file_path}")
        resume.save(file_path)
        print("File saved successfully")

        print("Extracting text from PDF...")
        text = extract_text(file_path)
        job_description = """
We are looking for a Python Full Stack Developer.

Required skills:
Python
Flask
React
JavaScript
SQL
MySQL
HTML
CSS
Git
Docker
"""
        print(f"Extracted text length: {len(text)}")

        print("Finding skills...")
        skills = find_skills(text)
        print(f"Skills found: {skills}")

        print("Comparing resume with job description...")
        ai_match_score = compare_resume_with_job(text, job_description)
        print(f"AI match score: {ai_match_score}")

        print("Calculating ATS score...")
        score = calculate_score(text, skills)
        print(f"ATS score: {score}")
        
        print("Matching jobs...")
        jobs = match_jobs(skills)
        print(f"Jobs matched: {len(jobs)}")

        
        response = {
            "message": "Resume uploaded successfully",
            "skills": skills,
            "ats_score": score,
            "ai_match_score": ai_match_score,
            "recommended_jobs": jobs
        }

        print("Returning response...")
        return jsonify(response)
    except Exception as e:
        error_msg = str(e)
        print(f"Error: {error_msg}")
        print(traceback.format_exc())
        return jsonify({"error": error_msg, "traceback": traceback.format_exc()}), 500


if __name__ == "__main__":
    app.run(debug=True)