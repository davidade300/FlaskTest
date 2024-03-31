SECRET_KEY = 'TOTK'
# ALL CAPS -> VARIAVEL UNIVERSAL
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='220498',
        servidor='localhost',
        database='jogoteca'
    )
