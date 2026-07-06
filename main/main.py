from suggest import suggest_menu

# 主菜・副菜・汁物の選択
def select_menu_type():
    print("提案してほしい献立の種類を選んでください")
    print("1: 献立一式")
    print("2: 主菜")
    print("3: 副菜")
    print("4: 汁物")

    choice = input("番号を入力してください：")

    menu_types = {
        "1": "all",
        "2": "main",
        "3": "side",
        "4": "soup"
    }

    if choice not in menu_types:
        print("エラー：正しい番号を入力してください。")
        return None

    return menu_types[choice]


def print_suggested_menu(suggested_menu, menu_type):
    category_names = {
        "main": "主菜",
        "side": "副菜",
        "soup": "汁物"
    }

    print("\n=== おすすめ献立 ===")

    if menu_type == "all":
        for key in ["main", "side", "soup"]:
            print(f"\n【{category_names[key]}】")

            if suggested_menu[key]:
                for i, recipe in enumerate(suggested_menu[key], start=1):
                    print(f"{i}. {recipe}")
            else:
                print("該当する料理が見つかりませんでした。")

    else:
        print(f"\n【{category_names[menu_type]}】")

        if suggested_menu[menu_type]:
            for i, recipe in enumerate(suggested_menu[menu_type], start=1):
                print(f"{i}. {recipe}")
        else:
            print("該当する料理が見つかりませんでした。")

# メインのシステム
def main():
    print("=== 献立提案システム ===")

    user_input = input("食材名をスペース区切りで入力してください：")

    if not user_input.strip():
        print("エラー：食材を入力してください。")
        return

    menu_type = select_menu_type()

    if menu_type is None:
        return

    suggested_menu = suggest_menu(user_input)

    print_suggested_menu(suggested_menu, menu_type)


if __name__ == "__main__":
    main()