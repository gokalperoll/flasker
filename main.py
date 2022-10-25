from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysupersecretkey"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    title = "Index"
    stuff = "K1 <b>sex</b>"
    computer_mark = ["asus", "lenovo", "casper", "monster"]
    return render_template('index.html',
                           stuff=stuff,
                           computer_mark=computer_mark,
                           title=title, )


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_404_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_500_internal_server_error(e):
    return render_template('500.html'), 500


# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html',
                           name=name,
                           form=form,)


if __name__ == '__main__':
    app.run(debug=True, port=1337)
