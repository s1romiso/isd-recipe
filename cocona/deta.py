import random

def select_menu(user_input, recipe_data):
    
    #カテゴリごとの候補を入れる空のリストを用意する
    matched_mains = [] 
    matched_sides = []
    matched_soups = [] 

#recipe_dataからrecipeにデータをひとつ保存をループ
    for recipe in recipe_data:
        is_match = True #まずはあってるで考える
        #user_inputにある材料をひとつ保存して、それをレシピと照合して、なければそのレシピは×
        for item in user_input:
            if item not in recipe["ingredients"]:
                is_match = False 
                break 

     #分類わけ
        if is_match:
            category = recipe["category"]
            name = recipe["name"]
            
            if category == "main":
                matched_mains.append(name)
            elif category == "side":
                matched_sides.append(name)
            elif category == "soup":
                matched_soups.append(name)
                
# 3つより多ければランダムに3つ選ぶ
    def get_random_three(matched_list):
        if len(matched_list) > 3:
            return random.sample(matched_list, 3)  
        return matched_list

    suggested_menu = {
        "main": get_random_three(matched_mains),
        "side": get_random_three(matched_sides),
        "soup": get_random_three(matched_soups),
    }
    
    return suggested_menu

