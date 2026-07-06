import random

def select_menu(user_input, recipe_data):
    
    # 1. カテゴリごとの候補を入れる空のリストを用意する
    matched_mains = [] 
    matched_sides = []
    matched_soups = [] 

    # 2. レシピデータを1つずつループで回してチェックする
    #recipe_data（レシピのリスト）の中から、データを1つずつ取り出して recipe という変数に入れながら、中身がなくなるまで繰り返してね
    for recipe in recipe_data:
        is_match = True
        #user_inputにある材料をひとつ保存して、それをレシピと照合して、なければそのレシピは×
        for item in user_input:
            if item not in recipe["ingredients"]:
                is_match = False 
                break 


        if is_match:
            category = recipe["category"]
            name = recipe["name"]
            
            if category == "main":
                matched_mains.append(name)
            elif category == "side":
                matched_sides.append(name)
            elif category == "soup":
                matched_soups.append(name)

    def get_random_three(matched_list):
        if len(matched_list) > 3:
            return random.sample(matched_list, 3)  # 3つより多ければランダムに3つ選ぶ
        return matched_list

    suggested_menu = {
        "main": get_random_three(matched_mains),
        "side": get_random_three(matched_sides),
        "soup": get_random_three(matched_soups),
    }
    
    return suggested_menu

