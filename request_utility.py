import requests
def req_methods(method):
    url = input("Enter your URL (default: https://example.com): ").strip()

    # Use a default URL if the user doesn't enter anything
    if not url:
        url = "https://example.com"

    try:
        if method.upper() == "POST":
            r = requests.post(url)
        elif method.upper() == "GET":
            r = requests.get(url)
        else:
            print("Request method not defined")
            return
        print(f"Request Method: {r.request.method}")  # Display only request method
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
# Example usage
req_methods("GET")  # Calls the function with a "GET" request
req_methods("POST")  # Calls the function with a "POST" request
