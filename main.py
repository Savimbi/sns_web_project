# The main.py

@app.route('/username')
def home():
    return '<h1>Good Morning %s</h1>' % username
