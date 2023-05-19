from flask import Flask, request
import openai
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask
app = Flask(__name__)

# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# GitLab's API endpoint for comments
gitlab_api_url = os.getenv('GITLAB_API_URL')

# Generate comment using GPT
def generate_comment(code_diff):
    # We're assuming the model to be "gpt-4" here, but please replace it with the appropriate model name
    response = openai.Completion.create(
        model="gpt-4",
        prompt=code_diff,
        max_tokens=512
    )
    
    return response.choices[0].text.strip()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Get the diff from the merge request
    code_diff = data['changes']

    # Generate the comment
    comment = generate_comment(code_diff)

    # Construct the API request
    headers = {"Private-Token": os.getenv('GITLAB_PRIVATE_TOKEN')}
    payload = {"body": comment}

    # Replace ":id" and ":merge_request_iid" with the actual project ID and merge request IID
    response = requests.post(gitlab_api_url, headers=headers, json=payload)

    if response.status_code != 201:
        app.logger.error('Failed to post comment to GitLab: %s', response.content)

    return '', 204

if __name__ == "__main__":
    app.run(port=5000, debug=True)
