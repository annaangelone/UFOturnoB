from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                        select *
                        from state
                        """
        cursor.execute(query, )

        for row in cursor:
            result.append(Stato(**row))
            # equivale a creare il costruttore lungo con tutte le righe con i rispettivi attributi

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(s1, s2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    select n.state1 as s1, n.state2 as s2
                    from neighbor n 
                    where n.state1 = %s and n.state2 = %s
                    """
        cursor.execute(query, (s1, s2))

        for row in cursor:
            result.append((row["s1"], row["s2"]))
            # equivale a creare il costruttore lungo con tutte le righe con i rispettivi attributi

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(s1, s2, anno, giorni):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select count(distinct s1.id) + count(distinct s2.id) as peso
                from sighting s1, sighting s2
                where s1.state = %s and s2.state = %s
                and year(s1.datetime) = %s and year(s2.datetime) = %s
                and abs(datediff(s1.`datetime`, s2.`datetime`)) <= %s        
                """
        cursor.execute(query, (s1, s2, anno, anno, giorni))

        for row in cursor:
            result.append(row["peso"])
            # equivale a creare il costruttore lungo con tutte le righe con i rispettivi attributi

        cursor.close()
        conn.close()
        return result


