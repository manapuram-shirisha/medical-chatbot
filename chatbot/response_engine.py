import pandas as pd
import os

# 🔹 Base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔹 Load datasets
df1 = pd.read_csv(os.path.join(BASE_DIR, 'data', 'dataset1.csv'))
df2 = pd.read_csv(os.path.join(BASE_DIR, 'data', 'dataset2.csv'))
df3 = pd.read_csv(os.path.join(BASE_DIR, 'data', 'dataset3.csv'))

# 🔹 Combine datasets
df = pd.concat([df1, df2, df3]).fillna("").astype(str)

# 🔹 Structure
disease_col = df.columns[0]
symptom_cols = df.columns[1:]

# 🔹 Combine symptoms
df['all_symptoms'] = df[symptom_cols].apply(lambda x: ' '.join(x), axis=1)


# 🔹 Prediction with better scoring
def predict_disease(user_input):
    user_words = user_input.lower().split()

    best_match = None
    max_score = 0

    for _, row in df.iterrows():
        symptoms = row['all_symptoms'].lower()

        # count matching words
        score = sum(2 for word in user_words if word in symptoms)

        if score > max_score:
            max_score = score
            best_match = row

    if best_match is not None and max_score > 0:
        disease = best_match[disease_col]
        matched_symptoms = best_match['all_symptoms']
        return disease, matched_symptoms
    else:
        return "Unknown", ""


# 🔹 Severity
def get_severity(text):
    text = text.lower()

    if any(x in text for x in ["chest pain", "breathlessness", "unconscious"]):
        return "High"
    elif any(x in text for x in ["fever", "vomiting", "nausea", "fatigue", "chills"]):
        return "Medium"
    else:
        return "Low"


# 🔹 Dynamic description generator
def generate_description(disease, symptoms):
    if disease == "Unknown":
        return "Symptoms are not clearly matching a specific disease."

    return f"{disease} is identified based on symptoms such as {symptoms[:100]}..."


# 🔹 Dynamic precautions
def generate_precautions(user_input):
    text = user_input.lower()

    precautions = []

    if "fever" in text:
        precautions.append("Monitor body temperature regularly")
    if "cough" in text:
        precautions.append("Avoid cold drinks and dust")
    if "chest" in text:
        precautions.append("Avoid heavy physical activity")
    if "vomiting" in text:
        precautions.append("Stay hydrated")
    if "skin" in text or "rash" in text:
        precautions.append("Maintain skin hygiene")

    # default precautions
    precautions.extend([
        "Take proper rest",
        "Drink enough fluids",
        "Consult a doctor if symptoms persist"
    ])

    return list(set(precautions))  # remove duplicates


# 🔹 Final response
def generate_chat_response(user_input):

    disease, matched_symptoms = predict_disease(user_input)
    severity = get_severity(user_input)

    description = generate_description(disease, matched_symptoms)

    precautions = generate_precautions(user_input)

    precautions_text = "\n- " + "\n- ".join(precautions)

    return f"""Bot: Predicted Disease: {disease}

Description:
{description}

Severity: {severity}

Precautions:{precautions_text}
"""