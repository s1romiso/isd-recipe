from flask import Flask, render_template, request
from cocona.deta import select_menu
from data.data import recipes

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    suggested_menu = None
    error_message = None
    input_ingredients = ""
    selected_menu_type = "all"

    if request.method == "POST":
        user_input_text = request.form.get("ingredients", "").strip()

        if not user_input_text:
            error_message = "食材を入力してください。"
        else:
            user_input = user_input_text.split()
            suggested_menu = select_menu(user_input, recipes)

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