import random

def select_menu(user_input, recipe_data, user_category):
    # ----------------------------------------------------
    # 1. ユーザが選んだカテゴリから、入力食材に合う料理（起点）を探す
    # ----------------------------------------------------
    base_candidates = []
    
    for recipe in recipe_data:
        # カテゴリが一致しているか確認
        if recipe["category"] != user_category:
            continue
            
        # 入力食材がすべて含まれているかチェック
        is_match = True
        for item in user_input:
            if item not in recipe["ingredients"]:
                is_match = False
                break
                
        if is_match:
            base_candidates.append(recipe)
            
    # 起点となる料理が1つも見つからなかったら、空のリストを返す
    if not base_candidates:
        return []

    # ----------------------------------------------------
    # 2. 起点となる料理の候補から、【重複なし】で最大3つ選ぶ
    # ----------------------------------------------------
    sample_size = min(len(base_candidates), 3)
    chosen_recipes = random.sample(base_candidates, sample_size)

    # 最終的に返す献立パターンのリスト
    suggested_menu = []

    # 選ばれた被りのない料理それぞれに対して、献立セットを作成するループ
    for chosen_recipe in chosen_recipes:
        target_genre = chosen_recipe["genre"]
        
        # 1パターン分の献立セットを格納する辞書（起点をまず登録）
        menu_set = {
            chosen_recipe["category"]: chosen_recipe["name"]
        }
        
        # 探すべき残りのカテゴリを特定する
        categories_to_find = ["main", "side", "soup"]
        categories_to_find.remove(chosen_recipe["category"])
        
        # 残りの2つのカテゴリについて、同じジャンルから料理を探す
        for cat in categories_to_find:
            match_genre_only = []
            
            for recipe in recipe_data:
                # 食材チェックを廃止し、カテゴリとジャンルの一致のみを確認
                if recipe["category"] == cat and recipe["genre"] == target_genre:
                    match_genre_only.append(recipe["name"])
            
            # 候補リストから1つ選んで献立に追加（食材チェックをしないため「(食材外)」の表記も不要に）
            if match_genre_only:
                menu_set[cat] = random.choice(match_genre_only)
            else:
                menu_set[cat] = "該当なし"
                
        # 完成した1セットを全体のパターンリストに追加
        suggested_menu.append(menu_set)

    return suggested_menu