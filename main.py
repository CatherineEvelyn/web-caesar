from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/add" method="post">
          <label>
              Rotate by:
              <input type="text" name="rot" value="0"/>
              <textarea name="text"></textarea>
          </label>
          <input type="submit" value="Submit Query"/>
      </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    return

@app.route("/")
def index():
    content = form
    return content

app.run()