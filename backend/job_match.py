jobs = [
    {
        "title": "Python Developer",
        "skills": ["python", "flask", "sql", "django"]
    },
    {
        "title": "Frontend Developer",
        "skills": ["html", "css", "javascript", "react"]
    },
    {
        "title": "Full Stack Developer",
        "skills": ["python", "react", "sql", "html", "css"]
    },
    {
        "title": "Cloud Engineer",
        "skills": ["aws", "docker", "kubernetes", "python"]
    }
]


def match_jobs(resume_skills):

    results = []

    for job in jobs:

        matched_skills = []

        for skill in job["skills"]:

            if skill in resume_skills:
                matched_skills.append(skill)

        total_skills = len(job["skills"])

        match_percentage = int(
            (len(matched_skills) / total_skills) * 100
        )

        results.append({
            "job": job["title"],
            "match": match_percentage,
            "skills": matched_skills
        })

    results.sort(key=lambda x: x["match"], reverse=True)

    return results