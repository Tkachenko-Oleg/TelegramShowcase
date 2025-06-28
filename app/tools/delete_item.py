from json import load, dump
import os


def delete_item(category: str, page: int):
    category = category.replace("admin_", "")
    with open("app/path_provider.json", "r") as file:
        data = load(file)

    values = list(data["catalog"][category].values())
    title = values[0]
    paths = values[1:]
    new_data = dict()
    new_data["title"] = title

    if os.path.exists(f"{paths[page - 1]}"):
        os.remove(f"{paths[page - 1]}")
        del paths[page - 1]

    for i in range(len(paths)):
        new_data[str(i)] = paths[i]
    data["catalog"][category] = new_data

    with open("app/path_provider.json", 'w') as file:
        dump(obj=data, fp=file, ensure_ascii=False)
