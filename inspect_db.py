from sqlalchemy import create_engine, inspect

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

print("📌 Tabelas encontradas:")
print(inspector.get_table_names())

for table in inspector.get_table_names():
    print(f"\n📌 Estrutura da tabela {table}:")
    for col in inspector.get_columns(table):
        print(f" - {col['name']} ({col['type']})")
