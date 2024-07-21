from flask import Blueprint, render_template, redirect, url_for
from crm_app.forms import RegistrationForm  # Убедитесь, что путь правильный

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Логика регистрации
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)
