class DataSource:
    def create_category_table(self) -> None:
        pass

    def register_category(self, usr_id: int, category: str) -> None:
        pass

    def get_category_statistic_today(self) -> list[tuple] | None:
        pass

    def get_category_statistic_yesterday(self) -> list[tuple] | None:
        pass

    def get_category_statistic_week(self) -> list[tuple] | None:
        pass

    def get_category_statistic_month(self) -> list[tuple] | None:
        pass

    def get_category_statistic_3_months(self) -> list[tuple] | None:
        pass

    def get_category_statistic_6_months(self) -> list[tuple] | None:
        pass
