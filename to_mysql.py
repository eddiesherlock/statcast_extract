import pandas as pd
from sqlalchemy import create_engine

host= ''
port=
user= ''
password= ''
db = 'MoneyBallDatabase'


engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db}')

try:
    df = pd.read_csv('statistics.csv', encoding='utf8')
    df.to_sql('statistics',engine)
    print("Write to MySQL successfully!")
except Exception as e:
    print(e)