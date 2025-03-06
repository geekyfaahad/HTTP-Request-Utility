# HTTP Request Utility

A simple Python utility for making HTTP GET and POST requests to specified URLs.

## Features

- Make GET requests to any URL
- Make POST requests to any URL
- User-friendly input interface
- Default URL provided if none is specified
- Basic error handling for request exceptions
- Display request method confirmation

## Project Structure

```
http-request-utility/
├── request_utility.py  # Main script containing the req_methods function
└── README.md          # Documentation (this file)
```

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/http-request-utility.git
   cd http-request-utility
   ```

2. Install the required dependencies:
   ```
   pip install requests
   ```

## Usage

Run the script and use the `req_methods()` function with either "GET" or "POST" as the argument:

```python
# Import the function
from request_utility import req_methods

# Make a GET request
req_methods("GET")

# Make a POST request
req_methods("POST")
```

When prompted, enter the URL you want to send the request to. If you don't enter a URL, the default "https://example.com" will be used.

### Example

```
Enter your URL (default: https://example.com): https://jsonplaceholder.typicode.com/posts
Request Method: GET
```

## License

This project is open source and available under the [MIT License](LICENSE).
