def select_menu(user_input, recipe_data):
    
    # 1. カテゴリごとの候補を入れる空のリストを用意する
    matched_mains = [] 
    matched_sides = []
    matched_soups = [] 

    # 2. レシピデータを1つずつループで回してチェックする
    #recipe_data（レシピのリスト）の中から、データを1つずつ取り出して recipe という変数に入れながら、中身がなくなるまで繰り返してね
    for recipe in recipe_data:
        
 # 3. 「すべての食材が揃っているか」をチェックする
        # 最初は「作れる（True）」と信じてスタートする
        is_match = True 
        
        for ingredient in recipe["ingredients"]:
#一個ずつチェックしてく
            if ingredient not in user_input:
                is_match = False 

                break  # これ以上他の材料を調べても意味がないので、ループを抜ける

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

