def calculate_score(text, skills):

    score = 0

    text = text.lower()

    # Skills score
    if len(skills) >= 5:
        score = score + 30
    elif len(skills) >= 3:
        score = score + 20
    else:
        score = score + 10

    # Education
    if "education" in text or "degree" in text or "b.e" in text:
        score = score + 20

    # Experience
    if "experience" in text or "internship" in text:
        score = score + 20

    # Projects
    if "project" in text:
        score = score + 15

    # Certifications
    if "certification" in text or "certificate" in text:
        score = score + 15

    return score