from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compare_resume_with_job(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0], vectors[1])

    score = similarity[0][0] * 100

    return round(score, 2)