from flask import Flask, render_template, request
from cocona.deta import select_menu
from data.data import recipes

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    suggested_menu = None
    error_message = None

    if request.method == "POST":
        user_input = request.form.get("ingredients", "")
        menu_type = request.form.get("menu_type", "all")

        if not user_input.strip():
            error_message = "食材を入力してください。"
        else:
            user_ingredients = user_input.split()
            all_results = select_menu(user_ingredients, recipes)

            if menu_type == "all":
                suggested_menu = all_results
            else:
                suggested_menu = {
                    "main": [],
                    "side": [],
                    "soup": []
                }
                suggested_menu[menu_type] = all_results[menu_type]

    return render_template(
        "index.html",
        suggested_menu=suggested_menu,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)