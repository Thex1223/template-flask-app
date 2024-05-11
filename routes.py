from main import *


@app.route('/helloworld')
def helloworld():
    return render_template("helloworld.html", system_name=env_data["SYSTEM_NAME"])