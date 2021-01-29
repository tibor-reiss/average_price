import asyncio
from databases import Database
import os


async def setup_database(conn_string):
    os.system('rm example.db')
    db = Database(conn_string)
    await db.connect()
    return db


async def create_table(db, query):
    await db.execute(query=query)


async def upsert(db, table, cols, values, conflict_col):
    query = f"""
        INSERT INTO {table}({','.join(c for c in cols)})
        VALUES({','.join("'" + str(v) + "'" for v in values)})
        ON CONFLICT({conflict_col}) DO UPDATE SET
        {','.join(c + '=' + str(v) for c, v in zip(cols, values) if c != conflict_col)}
    """
    await db.execute(query=query)
