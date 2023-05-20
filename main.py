from database import Database
from comp_database import CompetitiveDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.207.166.145:7687", "neo4j", "sod-basics-haste")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
competitive_db = CompetitiveDatabase(db)

# Criando alguns player
competitive_db.create_player("1", "Savage")
competitive_db.create_player("2", "Metro")
competitive_db.create_player("147", "Johnny")
competitive_db.create_player("23", "Randola")

# Criando algumas aulas e suas relações com os professores
competitive_db.create_match("ab", "Savage", "3-1", "true")
competitive_db.create_match("cd", "Metro", "4-0", "true")

# Atualizando o nome de um player
competitive_db.update_player("Savage", "21 Savage")

#  Adicionando players as partidas já criadas
competitive_db.insert_player_match("Metro", "ab", "false")
competitive_db.insert_player_match("Johnny", "cd", "false")
competitive_db.insert_player_match("Johnny", "ab", "true")

# Deletando um player
competitive_db.delete_player("Randola")

# Print de todas as informações do banco de dados
print("Players:")
print(competitive_db.get_players())
print("Matches:")
print(competitive_db.get_matches())

# retorna as infod da partida de id 'ab'
print(competitive_db.get_match_info("ab"))

# retorna as partidas jogadas por Johnny
print(competitive_db.get_player_history("Johnny"))

# Fechando a conexão
db.close()