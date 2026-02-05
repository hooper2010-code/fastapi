from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
create_async_engine("sqlite:///db.books")