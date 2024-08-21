from flask import Flask, request, jsonify
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

app = Flask(__name__)

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the ATS simulation function
def ats_simulation(resume_text):
    # Tokenize the resume text
    doc = nlp(resume_text)

    # Extract keywords using named entity recognition
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Extract skills using part-of-speech tagging
    skills = [token.text for token in doc if token.pos_ == "NOUN" and len(token.text) > 3]

    # Calculate the ATS score based on keyword frequency and skill relevance
    ats_score = 0
    for entity, label in entities:
        if label == "ORG" or label == "PERSON":
            ats_score += 1
    for skill in skills:
        if skill in ["python", "java", "javascript", " machine learning"]:
            ats_score += 2

    return ats_score

# Define the API endpoint for resume analysis
@app.route("/analyze", methods=["POST"])
def analyze_resume():
    resume_text = request.form["resume_text"]
    ats_score = ats_simulation(resume_text)
    return jsonify({"ats_score": ats_score})

if __name__ == "__main__":
    app.run(debug=True)