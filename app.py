from flask import Flask, render_template, request
from cocona.categoryver import select_menu
from data.data import recipes

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    suggested_menu = None
    error_message = None
    input_ingredients = ""
    selected_menu_type = "main"

    if request.method == "POST":
        input_ingredients = request.form.get("ingredients", "").strip()
        selected_menu_type = request.form.get("menu_type", "main")

        if not input_ingredients:
            error_message = "食材を入力してください。"
        else:
            user_input = input_ingredients.split()

            suggested_menu = select_menu(
                user_input,
                recipes,
                selected_menu_type
            )

            if not suggested_menu:
                error_message = "該当する料理が見つかりませんでした。"

    return render_template(
        "index.html",
        suggested_menu=suggested_menu,
        error_message=error_message,
        input_ingredients=input_ingredients,
        selected_menu_type=selected_menu_type
    )


if __name__ == "__main__":
    app.run(debug=True)