import requests

pdf_path = r"c:\Users\Praveen Joshi\OneDrive\Documents\praveen resume.pdf"

with open(pdf_path, 'rb') as f:
    files = {'resume': f}
    response = requests.post('http://127.0.0.1:5000/upload', files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    print(f"Response JSON: {response.json() if response.text else 'No content'}")
