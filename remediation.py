from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name")
    if not name:
        name = "haicen"
    page = """
    <DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Xss!</title>
    </head>
    <body>
    <h1>
    XSS is fun
    </h1>
    Hello, <b><span id="name">{{name}}</span></b>
    </body>
    </html>
    """
    return render_template_string(page, name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
