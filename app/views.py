from app import fapp, render_template, request, redirect, url_for, session


@fapp.route('/')
def root_index():
    return render_template('index.html')


@fapp.route('/index', methods=['GET', 'POST'])
def index():
    username = None
    if request.method == 'POST':
        username = request.form.get('username')
        unames = session.get('usernames', [])
        unames.append(username)
        session['usernames'] = unames
        del session['usernames']
    return render_template('index.html', user={'username': username}, usernames=unames)


@fapp.route('/blog/info/<page>/<line>')
def blog_info(page, line):
    return f'Blog content here - {page} and {line}'

