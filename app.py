from api import API

app = API()


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/home")
def template_handler(req, resp):
    resp.body = app.template("index.html").encode()

@app.route("/about")
def template_handler(req, resp):
    resp.body = app.template("about.html").encode()
