# DecodeLabs AI Internship
# Project 3
# Tech Stack Recommendation System
# Name: Vaidika Sharma
# Algorithm:
# - TF-IDF Vectorizer
# - Cosine Similarity

# DecodeLabs AI Internship
# Project 3 - AI Recommendation Logic

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Tech roles and their required skills

jobs = {
    "Data Scientist": "python machine learning pandas numpy data analysis statistics",
    "Web Developer": "html css javascript react nodejs frontend backend",
    "Backend Developer": "python django flask sql api database",
    "Cloud Engineer": "aws cloud docker kubernetes linux devops",
    "Cyber Security Analyst": "network security ethical hacking kali linux penetration testing",
    "AI Engineer": "python machine learning deep learning tensorflow pytorch ai",
    "Mobile App Developer": "java kotlin android flutter dart mobile development"
}

# Take user input

print("\nEnter your 3 skills/interests")

skill1 = input("Skill 1: ")
skill2 = input("Skill 2: ")
skill3 = input("Skill 3: ")

user_input = skill1 + " " + skill2 + " " + skill3

print("\nYour Skills:", user_input)

# Convert job descriptions and user input into vectors

documents = list(jobs.values())

documents.append(user_input)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF Vectorization Completed!")

# Calculate similarity

similarity = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)

print("\nSimilarity Calculated Successfully!")

# Sort similarity scores

scores = similarity.flatten()

job_names = list(jobs.keys())

sorted_jobs = sorted(
    zip(job_names, scores),
    key=lambda x: x[1],
    reverse=True
)

print("\nJobs Sorted Successfully!")

# Display Top 3 Recommendations

print("\nTop 3 Recommended Career Paths:\n")

for job, score in sorted_jobs[:3]:
    print(f"{job} ---> Match Score: {score:.2f}")