from json import load, dump


def save_item(category: str, new_element_path: str):
    category = category.replace("admin_", "")
    with open("app/path_provider.json", "r") as file:
        data = load(file)

    values = list(data["catalog"][category].values())
    title = values[0]
    paths = values[1:]
    new_data = dict()
    new_data["title"] = title
    new_data["0"] = new_element_path

    for i in range(len(paths)):
        new_data[str(i + 1)] = paths[i]
    data["catalog"][category] = new_data

    with open("app/path_provider.json", "w") as file:
        dump(obj=data, fp=file, ensure_ascii=False)
