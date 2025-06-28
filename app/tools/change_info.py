from json import load, dump


def update_info(new_text: str):
    with open("app/path_provider.json", "r") as file:
        data = load(file)

    data["description"] = new_text

    with open("app/path_provider.json", "w") as file:
        dump(obj=data, fp=file, ensure_ascii=False)
