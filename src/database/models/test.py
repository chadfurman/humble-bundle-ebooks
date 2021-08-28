from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///cache.db', echo=True, future=True) #TODO: make echo a debug var

with engine.connect() as conn:
    result = conn.execute(text('select "hello world"'))
    print(result.all())