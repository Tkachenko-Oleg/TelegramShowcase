from json import load


def correct_page(category: str, page: int):
    category = category.replace("admin_", "")
    with open("app/path_provider.json") as file:
        data = load(file)
        length = len(list(data["catalog"][category].values())[1:])
    if length == 0:
        return 0
    if page == 0:
        return 1
    elif page > length:
        return length
    else:
        return page
