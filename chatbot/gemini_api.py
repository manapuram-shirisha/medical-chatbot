from google import genai

client = genai.Client(api_key="AIzaSyA5-mhzoz3tnPunfmhM0j11ASJ909Tf_AI")

def get_medical_response(symptoms):
    prompt = f"""
    Symptoms: {symptoms}

    Give:
    Disease:
    Description:
    Severity:
    Precautions:
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash-latest",
        contents=prompt
    )

    return response.text