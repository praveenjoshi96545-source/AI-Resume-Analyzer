skills_list = [
    "python",
    "java",
    "javascript",
    "html",
    "css",
    "react",
    "sql",
    "mysql",
    "flask",
    "django",
    "aws",
    "docker",
    "kubernetes"
]


def find_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills