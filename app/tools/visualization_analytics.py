import matplotlib.pyplot as plt
import os

from app.db.create_db import database


def visualization_analytics(period: str):
    if period == "сегодня":
        data = database.get_category_statistic_today()
        title = "Сегодня"
    elif period == "вчера":
        data = database.get_category_statistic_yesterday()
        title = "Вчера"
    elif period == "неделя":
        data = database.get_category_statistic_week()
        title = "Неделя"
    elif period == "месяц":
        data = database.get_category_statistic_month()
        title = "Месяц"
    elif period == "3 месяца":
        data = database.get_category_statistic_3_months()
        title = "3 месяца"
    elif period == "6 месяцев":
        data = database.get_category_statistic_6_months()
        title = "6 месяцев"
    else:
        return False

    data_lst = [category[0].replace(' ', '') for category in data]
    data_dict = {
        "Платья": data_lst.count("category_dresses"),
        "Юбки": data_lst.count("category_skirts"),
        "Брюки": data_lst.count("category_jeans"),
        "Игры": data_lst.count("category_toys"),
        "Спорт": data_lst.count("category_sport"),
        "Акс.": data_lst.count("category_accessories"),
        "Блузки": data_lst.count("category_tshorts"),
        "Дом": data_lst.count("category_home"),
        "Верх": data_lst.count("category_outerwear")
    }

    categories = list(data_dict.keys())
    values = list(data_dict.values())

    plt.figure()
    plt.bar(x=categories, height=values)
    plt.xlabel(xlabel="Категория")
    plt.ylabel(ylabel="Количество уникальных запросов")
    plt.title(label=title)
    plt.tight_layout()
    plt.savefig("app/images/tmp/statistic.png")
    plt.close()

    return True


def delete_tmp_image():
    if os.path.exists("statistic.png"):
        os.remove("statistic.png")
