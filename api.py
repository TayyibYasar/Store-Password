from flask import Flask, current_app
import views
import database

app = Flask(__name__, static_folder="./build", static_url_path='/')
app.config.from_object("settings")
app.add_url_rule("/api/add_data",view_func=views.add_data, methods=["POST"])
app.add_url_rule("/api/add_user",view_func=views.add_user, methods=["POST"])
app.add_url_rule("/api/login",view_func=views.get_user, methods=["POST"])
app.add_url_rule("/api/datas", view_func=views.take_list, methods=["POST"])
app.add_url_rule("/api/delete_data", view_func=views.take_data, methods=["POST"])
app.add_url_rule("/", view_func=views.index)
db = database.Database()
app.config['db'] = db
port = app.config.get("PORT", 5000)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)