import requests
import json

# --- IMPORTANT ---
# Replace with your actual Student ID and GitHub Repo URL
STUDENT_ID = "YOUR_STUDENT_ID"
GITHUB_REPO_URL = "https://github.com/your-username/your-repo-name"
# ---

API_URL = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws"

def request_seed():
    """
    Request encrypted seed from instructor API.
    """
    with open("student_public.pem", "r") as f:
        public_key = f.read()

    payload = {
        "student_id": STUDENT_ID,
        "github_repo_url": GITHUB_REPO_URL,
        "public_key": public_key.replace("\n", "\\n")
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        encrypted_seed = data.get("encrypted_seed")
        if encrypted_seed:
            with open("encrypted_seed.txt", "w") as f:
                f.write(encrypted_seed)
            print("Encrypted seed saved to encrypted_seed.txt")
        else:
            print("Error: 'encrypted_seed' not found in response.")
            print("Response:", data)

    except requests.exceptions.RequestException as e:
        print(f"Error requesting seed: {e}")
        if e.response:
            print("Response content:", e.response.text)

if __name__ == "__main__":
    request_seed()
