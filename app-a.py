from os import getenv
from flask import Flask, request

app = Flask("AppA")


@app.route('/', methods=['GET'])
def score_server():
    url = getenv('URL', 'app-a.com')
    region = getenv('REGION', 'us-east-1')
    env = getenv('ENV_NAME', 'DEV')
    if request.method == 'GET':
        return f"""
          <html>
          <head>
              <title>{url}</title>
          </head>
          <body>
            <h1>The URL is {url} </h1>
            <h2>The ENV_NAME is {env} www</h2>
            <h2>The REGION is {region} </h2>
          </body>
          </html>
          """


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
