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
        input_ingredients = request.form.get("ingredients", "").strip()
        selected_menu_type = request.form.get("menu_type", "all")

        if not input_ingredients:
            error_message = "食材を入力してください。"
        else:
            user_input = input_ingredients.split()
            all_results = select_menu(user_input, recipes)

            # 選択された種類だけを残す
            if selected_menu_type == "all":
                suggested_menu = all_results
            else:
                suggested_menu = {
                    "main": [],
                    "side": [],
                    "soup": []
                }

                suggested_menu[selected_menu_type] = all_results[selected_menu_type]

            # 辞書の中のリストがすべて空か確認
            if not any(suggested_menu.values()):
                suggested_menu = None
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