import http.server
import urllib.parse

# This is the HTML page shown to the user
def get_html_page(message=""):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Name and Age Website</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}
        .container {{
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            width: 500px;
        }}
        h1 {{
            color: #333;
        }}
        .columns {{
            display: flex;
            gap: 20px;
            justify-content: center;
            margin: 20px 0;
        }}
        .column {{
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }}
        label {{
            font-weight: bold;
            color: #555;
            margin-bottom: 5px;
        }}
        input {{
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #aaa;
            border-radius: 6px;
            box-sizing: border-box;
        }}
        button {{
            margin-top: 15px;
            padding: 12px 30px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #45a049;
        }}
        .message {{
            margin-top: 20px;
            font-size: 20px;
            color: #2c3e50;
            font-weight: bold;
            background-color: #eaffea;
            padding: 15px;
            border-radius: 8px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome!</h1>
        <form method="POST" action="/">
            <div class="columns">
                <!-- Column 1: Name -->
                <div class="column">
                    <label>Name</label>
                    <input type="text" name="name" placeholder="Enter your name" required />
                </div>
                <!-- Column 2: Age -->
                <div class="column">
                    <label>Age</label>
                    <input type="number" name="age" placeholder="Enter your age" required />
                </div>
            </div>
            <button type="submit">Submit</button>
        </form>

        <!-- Show message if name and age are submitted -->
        {f'<div class="message">{message}</div>' if message else ""}
    </div>
</body>
</html>
"""

# This handles all web requests
class MyHandler(http.server.BaseHTTPRequestHandler):

    # When user opens the page in browser (GET request)
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Show empty form
        self.wfile.write(get_html_page().encode())

    # When user clicks Submit button (POST request)
    def do_POST(self):
        # Read the form data sent by the browser
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode()

        # Extract name and age from the form
        params = urllib.parse.parse_qs(post_data)
        name = params.get("name", [""])[0]
        age  = params.get("age",  [""])[0]

        # Create the greeting message
        message = f"Hello! Your name is {name} and your age is {age}."

        # Send the page back with the message
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(get_html_page(message).encode())

    # Silence the default request logs (optional)
    def log_message(self, format, *args):
        pass


# ── Start the server ──────────────────────────────────────────────────────────
PORT = 8080
print(f"Server started!")
print(f"Open your browser and go to:  http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")


        
