import random

def select_menu(user_input, recipe_data, user_category):
    base_candidates = []
    for recipe in recipe_data:
        if recipe["category"] != user_category:
            continue
        is_match = True
        for item in user_input:
            if item not in recipe["ingredients"]:
                is_match = False
                break
        if is_match:
            base_candidates.append(recipe)
            
    if not base_candidates:
        return []

    # 1回目のランダム：起点カテゴリから重複なしで最大3つ選ぶ
    sample_size = min(len(base_candidates), 3)
    chosen_recipes = random.sample(base_candidates, sample_size)

    suggested_menu = []

    for chosen_recipe in chosen_recipes:
        target_genre = chosen_recipe["genre"]
        menu_set = {chosen_recipe["category"]: chosen_recipe["name"]}
        
        categories_to_find = ["main", "side", "soup"]
        categories_to_find.remove(chosen_recipe["category"])
        
        for cat in categories_to_find:
            match_genre_and_ingredients = []
            match_genre_only = []
            
            for recipe in recipe_data:
                if recipe["category"] == cat and recipe["genre"] == target_genre:
                    match_genre_only.append(recipe["name"])
                    
                    is_match = True
                    for item in user_input:
                        if item not in recipe["ingredients"]:
                            is_match = False
                            break
                    if is_match:
                        match_genre_and_ingredients.append(recipe["name"])
            
            # 2回目のランダム：残りのカテゴリからそれぞれ1つ選ぶ
            if match_genre_and_ingredients:
                menu_set[cat] = random.choice(match_genre_and_ingredients)
            elif match_genre_only:
                selected_name = random.choice(match_genre_only)
                menu_set[cat] = f"{selected_name}(食材外)"
            else:
                menu_set[cat] = "該当なし"
                
        suggested_menu.append(menu_set)

    return suggested_menu


# ==========================================
# 大幅に増やしたテストデータ
# ==========================================
large_recipes = [
    # --- 和食 (japanese) ---
    {"name": "肉じゃが", "category": "main", "genre": "japanese", "ingredients": ["玉ねぎ", "じゃがいも", "牛肉"]},
    {"name": "親子丼の具", "category": "main", "genre": "japanese", "ingredients": ["玉ねぎ", "鶏肉", "卵"]},
    {"name": "生姜焼き", "category": "main", "genre": "japanese", "ingredients": ["玉ねぎ", "豚肉"]},
    {"name": "サバの塩焼き", "category": "main", "genre": "japanese", "ingredients": ["サバ"]},
    {"name": "きんぴらごぼう", "category": "side", "genre": "japanese", "ingredients": ["ごぼう", "にんじん"]},
    {"name": "ほうれん草のお浸し", "category": "side", "genre": "japanese", "ingredients": ["ほうれん草"]},
    {"name": "玉ねぎの天ぷら", "category": "side", "genre": "japanese", "ingredients": ["玉ねぎ"]},
    {"name": "味噌汁", "category": "soup", "genre": "japanese", "ingredients": ["豆腐", "わかめ"]},
    {"name": "オニオンスープ(和風)", "category": "soup", "genre": "japanese", "ingredients": ["玉ねぎ"]},

    # --- 中華 (chinese) ---
    {"name": "酢豚", "category": "main", "genre": "chinese", "ingredients": ["玉ねぎ", "豚肉", "ピーマン"]},
    {"name": "回鍋肉", "category": "main", "genre": "chinese", "ingredients": ["キャベツ", "豚肉"]},
    {"name": "青椒肉絲", "category": "main", "genre": "chinese", "ingredients": ["ピーマン", "牛肉"]},
    {"name": "玉ねぎと卵の炒め物", "category": "side", "genre": "chinese", "ingredients": ["玉ねぎ", "卵"]},
    {"name": "叩ききゅうり", "category": "side", "genre": "chinese", "ingredients": ["きゅうり"]},
    {"name": "中華卵スープ", "category": "soup", "genre": "chinese", "ingredients": ["卵", "玉ねぎ"]},
    {"name": "ワンタンスープ", "category": "soup", "genre": "chinese", "ingredients": ["ワンタン"]},

    # --- 洋食 (western) ---
    {"name": "ハンバーグ", "category": "main", "genre": "western", "ingredients": ["玉ねぎ", "合挽肉"]},
    {"name": "ビーフシチュー", "category": "main", "genre": "western", "ingredients": ["玉ねぎ", "牛肉", "にんじん"]},
    {"name": "チキンカツ", "category": "main", "genre": "western", "ingredients": ["鶏肉"]},
    {"name": "ポテトサラダ", "category": "side", "genre": "western", "ingredients": ["じゃがいも", "玉ねぎ"]},
    {"name": "コールスロー", "category": "side", "genre": "western", "ingredients": ["キャベツ"]},
    {"name": "オニオングラタンスープ", "category": "soup", "genre": "western", "ingredients": ["玉ねぎ", "チーズ"]},
    {"name": "コーンスープ", "category": "soup", "genre": "western", "ingredients": ["コーン"]}
]

# ==========================================
# テスト実行（何度か実行してみてください）
# ==========================================
if __name__ == "__main__":
    test_input = ["玉ねぎ"]
    test_category = "main"

    result = select_menu(test_input, large_recipes, test_category)

    import pprint
    print("--- 抽選結果 ---")
    pprint.pprint(result, width=60)