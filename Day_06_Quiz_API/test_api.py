import requests
import time
import sys

BASE_URL = "http://127.0.0.1:5000/api"

def test_get_questions():
    print("Testing GET /questions...")
    try:
        response = requests.get(f"{BASE_URL}/questions")
        if response.status_code == 200:
            questions = response.json()
            print(f"SUCCESS: Retrieved {len(questions)} questions.")
            # Verify no answers in response
            for q in questions:
                if 'answer' in q:
                    print("FAILURE: Answer field leaked in question!")
                    return False
            return True
        else:
            print(f"FAILURE: Status code {response.status_code}")
            return False
    except Exception as e:
        print(f"FAILURE: Connection error: {e}")
        return False

def test_submit_quiz():
    print("\nTesting POST /submit...")
    payload = {
        "answers": {
            "1": "Paris",
            "3": "4"
        }
    }
    try:
        response = requests.post(f"{BASE_URL}/submit", json=payload)
        if response.status_code == 200:
            result = response.json()
            print(f"Result: {result}")
            if result['score'] == 2:
                print("SUCCESS: Score calculation is correct.")
                return True
            else:
                print(f"FAILURE: Expected score 2, got {result['score']}")
                return False
        else:
            print(f"FAILURE: Status code {response.status_code}")
            return False
    except Exception as e:
        print(f"FAILURE: Connection error: {e}")
        return False

if __name__ == "__main__":
    # Wait for server to start
    time.sleep(2)
    
    if test_get_questions() and test_submit_quiz():
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed.")
        sys.exit(1)
