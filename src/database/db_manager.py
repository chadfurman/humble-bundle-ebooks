from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, registry
from contextlib import contextmanager


class DbManager():
    conn_string = "sqlite+pysqlite:///:memory:"
    test_conn_string = "sqlite+pysqlite:///:memory:"
    metadata = MetaData()
    mapper_registry = registry()
    connection = None
    
    engine = None

    @contextmanager
    def get_session(self):
        session = Session(self.engine)
        try:
            yield session
        finally:
            session.close()

    def init_db(self, conn_string=None, test=False):
        conn_string = conn_string or (self.test_conn_string if test else self.conn_string)
        self.engine = create_engine(conn_string)
        self.mapper_registry.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

    def teardown(self):
        self.mapper_registry.metadata.drop_all(self.engine)

dal = DbManager()
