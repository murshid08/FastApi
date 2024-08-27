
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosApp.db"
SQLALCHEMY_DATABASE_URL = "postgresql://fastapi_r0o1_user:mIitQvMVTAvzLMJxjLGccGHy4usG63ke@dpg-cr6m7vt6l47c739616j0-a/fastapi_r0o1"



# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args = {'check_same_thread' : False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit = False, autoflush  = False,bind=engine)
Base = declarative_base()
