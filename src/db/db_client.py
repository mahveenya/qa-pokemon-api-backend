from db.pokemon import PokemonTable
import psycopg
from psycopg import sql

DB_URL = "postgresql://admin:admin@localhost:5432/pokemon_db"


class DBClient:
    def _execute(self, query, params=None, fetch="one"):
        with psycopg.connect(DB_URL) as conn, conn.cursor() as cursor:
            cursor.execute(query, params)
            if fetch == "one":
                return cursor.fetchone()
            elif fetch == "all":
                return cursor.fetchall()

    def count_all_entries(self, table_name):
        result = self._execute(
            sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name))
        )
        return result[0] if result is not None else 0

    def select(self, table_name, **kwargs):
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        if kwargs:
            where = sql.SQL(" WHERE {}").format(
                sql.SQL(" AND ").join(
                    sql.SQL("{} = {}").format(sql.Identifier(k), sql.Placeholder())
                    for k in kwargs
                )
            )
            query = query + where

        return self._execute(
            query, list(kwargs.values()) if kwargs else None, fetch="all"
        )


class DB:
    def __init__(self):
        client = DBClient()
        self.pokemon = PokemonTable(client)


db = DB()
