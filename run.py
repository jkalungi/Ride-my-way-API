from app import app
# from app.api.user import views

@app.route('/', methods=['GET'])
def index():
    return ('Get ride')


if __name__ == '__main__':

    app.run(debug=True)