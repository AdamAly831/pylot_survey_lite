from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
   
    def index(self):
        if not 'counter' in session:
            session['counter'] = 0
        return self.load_view('index.html')

    def process(self):
        session['counter'] += 1
        session['name'] = request.form['name']
        session['comment'] = request.form['comment']
        session['lang'] = request.form['lang']
        return redirect('/result')

    def result(self):
        return self.load_view('result.html', counter=session['counter'], name=session['name'], comment=session['comment'], lang=session['lang'])

    def magic_method(self):
        print 'You found the secret method!'
        return redirect('/')