from main import *


@app.route('/helloworld')
def helloworld():
    return render_template("helloworld.html", system_name=env_data["SYSTEM_NAME"])

@app.route('/')
def index():
    return render_template("index.html", system_name=env_data["SYSTEM_NAME"])

@app.route('/dashboard')
def dashboard():
    return render_template(
        "erp/dashboard.html", 
        system_name=env_data["SYSTEM_NAME"],
        system_name_enterprise="Nome da Empresa"
    )


# +----------------------------+
# |                            |
# |  _                _        |
# | | |    ___   __ _(_)_ __   |
# | | |   / _ \ / _` | | '_ \  |
# | | |__| (_) | (_| | | | | | |
# | |_____\___/ \__, |_|_| |_| |
# |             |___/          |
# |                            |
# +----------------------------+
@app.route('/login')
def login():
    return render_template(
        "auth/login.html", 
        system_name=env_data["SYSTEM_NAME"]
    )

@app.route('/register')
def register():
    return render_template(
        "auth/register.html", 
        system_name=env_data["SYSTEM_NAME"]
    )

@app.route('/terms')
def terms():
    return render_template(
        "auth/login.html", 
        system_name=env_data["SYSTEM_NAME"]
    )