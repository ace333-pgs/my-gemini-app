import os
import json
import google.generativeai as genai

def handler(event, context):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {
            'statusCode': 500,
            'body': json.dumps('API Key is not set.')
        }
    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("안녕하세요, 당신은 누구인가요?")

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'response': response.text})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(f"Error: {str(e)}")
        }