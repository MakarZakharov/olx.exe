from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Title</title>
    </head>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
