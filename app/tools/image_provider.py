from json import load


def change_image(category: str, page: int):
    category = category.replace("admin_", "")
    with open("app/path_provider.json") as file:
        data = load(file)
        img_paths = list(data["catalog"][category].values())[1:]
        length = len(img_paths)
    if page == 0:
        return img_paths[0]
    elif page > length:
        return img_paths[-1]
    else:
        return img_paths[page - 1]
