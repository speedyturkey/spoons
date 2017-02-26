from application import application

@application.route('/')
def index():
    return 'Welcome to SpoonsOnline!'
