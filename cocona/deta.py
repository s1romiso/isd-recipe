def select_menu(user_input, recipe_data):
    
    # 1. カテゴリごとの候補を入れる空のリストを用意する
    matched_mains = []   # 主食（main）の候補
    matched_sides = []   # 副菜（side）の候補
    matched_soups = []   # 汁物（soup）の候補

    # 2. レシピデータを1つずつループで回してチェックする
    #recipe_data（レシピのリスト）の中から、データを1つずつ取り出して recipe という変数に入れながら、中身がなくなるまで繰り返してね
    for recipe in recipe_data:
        
        # 3. 「一部が当てはまるか」をチェックするフラグ
        is_match = False
        for ingredient in recipe["ingredients"]:
            # レシピに必要な材料のどれか1つでも、ユーザーの入力リストにあればOK
            if ingredient in user_input:
                is_match = True
                break  # 1つでも見つかれば、このレシピの他の材料はチェックしなくていいので抜ける
        
        # 4. 食材がマッチしていたら、カテゴリ別に仕分ける
        if is_match:
            category = recipe["category"]
            name = recipe["name"]
            
            if category == "main":
                matched_mains.append(name)
            elif category == "side":
                matched_sides.append(name)
            elif category == "soup":
                matched_soups.append(name)

    # 5. Aさんに返す結果を、最大3つまでに絞って辞書型にまとめる
    # Pythonの「[:3]」は、リストの最初から3つ目までを切り取る（スライス）という便利な書き方です
    suggested_menu = {
        "main": matched_mains[:3],
        "side": matched_sides[:3],
        "soup": matched_soups[:3]
    }
    
    return suggested_menu


# --- ここから下は自分のパソコンでテストするためのエリア ---
if __name__ == "__main__":
    # Aさんから届く想定の入力データ（リスト型）
    test_user_input = ["トマト", "豚肉"]
    
    # Cさんが用意してくれる形式のテストデータ
    test_recipe_data = [
        {
            "id": 1,
            "name": "豚肉と玉ねぎの生姜焼き",
            "category": "main",
            "ingredients": ["豚肉", "玉ねぎ"]
        },
        {
            "id": 2,
            "name": "トマトスープ",
            "category": "soup",
            "ingredients": ["トマト", "玉ねぎ"]
        },
        {
            "id": 3,
            "name": "即席トマトサラダ",
            "category": "side",
            "ingredients": ["トマト"]
        }
    ]
    
    # 関数を動かしてみる
    result = generate_menu(test_user_input, test_recipe_data)
    
    # 結果を表示
    print("--- 提案されたメニュー候補（最大3件ずつ） ---")
    print("主食:", result["main"])
    print("副菜:", result["side"])
    print("汁物:", result["soup"])