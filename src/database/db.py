import os
import ssl
from dotenv import load_dotenv
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_url = os.environ.get("PG_DB_URL")
if not db_url:
    raise ValueError("The environment variable 'PG_DB_URL' is not set or is empty.")

# Create SSL context for asyncpg
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Create an AsyncEngine
engine = create_async_engine(
    url=db_url.replace("postgresql://", "postgresql+asyncpg://"),  # Use asyncpg driver
    echo=True,
    connect_args={"ssl": ssl_context}  # Pass SSL configuration
)

# Create a session factory
Session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        from src.users.models import User
        from src.store.products.models import Product
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session
