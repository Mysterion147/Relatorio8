class CompetitiveDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, id, name):
        query = "CREATE (:Player {name: $name, id: $id})"
        parameters = {"id": id, "name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, id, player_name, result, win):
        query = "MATCH (p:Player {name: $player_name}) CREATE (:Match {match_id: $id, result: $result})<-[:PLAYED{victor: $win}]-(p)"
        parameters = {"id": id, "player_name": player_name, "result": result, "win":win}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (m: Match) RETURN m.match_id AS match_id"
        results = self.db.execute_query(query)
        return [(result["match_id"]) for result in results]

    def get_player_history(self, name):
        query = "MATCH (:Player {name: $name})--(m:Match) RETURN m.match_id AS match_id"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"]) for result in results]

    def get_match_info(self, id):
        query = "MATCH (m:Match{id: $id}) RETURN m.id AS match_id, m.result AS match_result"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"], result["match_result"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_match_id(self, old_id, new_id):
        query = "MATCH (m:Match {id: $old_name}) SET m.id = $new_id"
        parameters = {"old_name": old_id, "new_name": new_id}
        self.db.execute_query(query, parameters)

    def update_match_result(self, old_result, new_result):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_result, "new_name": new_result}
        self.db.execute_query(query, parameters)
    
    def insert_player_match(self, player_name, match_id, win):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {match_id: $match_id}) CREATE (p)-[:PLAYED{victor: $win}]->(m)"
        parameters = {"player_name": player_name, "match_id": match_id, "win": win}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, id):
        query = "MATCH (m:Match {match_id: $id})<-[:PLAYED]-(p:Player) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)