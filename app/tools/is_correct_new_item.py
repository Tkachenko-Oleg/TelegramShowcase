from json import load


def is_correct_item(category: str, new_element_path: str):
    category = category.replace("admin_", "")
    with open("app/path_provider.json", "r") as file:
        data = load(file)

    values = list(data["catalog"][category].values())
    if new_element_path in values:
        return False
    return True
