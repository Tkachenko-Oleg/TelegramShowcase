import psycopg2
import logging

from app.db.datasource import DataSource
from app.config import Config


class PostgresDatabase(DataSource):
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            database=Config.POSTGRES_DB,
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD,
            host=Config.POSTGRES_HOST,
            port=Config.POSTGRES_PORT
        )
        self.cursor = self.connection.cursor()

    def create_category_table(self) -> None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    create table if not exists category_statistic (
                        id bigserial not null primary key,
                        usr_id bigint not null,
                        category char(25),
                        time timestamp not null
                    );
                    """
                )
                self.connection.commit()
        except psycopg2.Error as error:
            logging.error(f"Connection error: {error}")
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def register_category(self, usr_id: int, category: str) -> None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    insert into category_statistic (usr_id, category, time)
                    select %s, %s, current_date
                    where not exists (
                        select 1 from category_statistic
                        where usr_id = %s 
                        and category = %s
                        and cast(time as date) = current_date
                    );
                    """,
                    (usr_id, category, usr_id, category)
                )
                self.connection.commit()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def get_category_statistic_today(self) -> list[tuple] | None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    select category 
                    from category_statistic
                    where date(time) = current_date;
                    """
                )
                return self.cursor.fetchall()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def get_category_statistic_yesterday(self) -> list[tuple] | None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    select category 
                    from category_statistic
                    where date(time) = current_date - interval '1 day';
                    """
                )
                return self.cursor.fetchall()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def get_category_statistic_week(self) -> list[tuple] | None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    select category
                    from category_statistic
                    where date(time) >= current_date - interval '7 days';
                    """
                )
                return self.cursor.fetchall()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def get_category_statistic_month(self) -> list[tuple] | None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    select category
                    from category_statistic
                    where date(time) >= current_date - interval '1 month';
                    """
                )
                return self.cursor.fetchall()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def get_category_statistic_3_months(self) -> list[tuple] | None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    select category
                    from category_statistic
                    where date(time) >= current_date - interval '3 months';
                    """
                )
                return self.cursor.fetchall()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")

    def get_category_statistic_6_months(self) -> list[tuple] | None:
        try:
            with self.connection:
                self.cursor.execute(
                    """
                    select category
                    from category_statistic
                    where date(time) >= current_date - interval '6 months';
                    """
                )
                return self.cursor.fetchall()
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")
