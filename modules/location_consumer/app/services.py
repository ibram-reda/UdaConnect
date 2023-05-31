import logging
from datetime import datetime, timedelta
from typing import Dict, List

from datetime import datetime
import psycopg2
import logging
from config import DB_USERNAME, DB_HOST, DB_NAME, DB_PORT, DB_PASSWORD


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("location Service")

class LocationService:
    @staticmethod
    def create(location: Dict) :
        session = psycopg2.connect(dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)
        cursor = session.cursor()
        cursor.execute(
            "INSERT INTO location (person_id, coordinate, creation_time) VALUES (%(person_id)s, ST_Point(%(latitude)s, %(longitude)s), %(creation_time)s);",
              location)
        session.commit()
        cursor.close()
        session.close()
        return location


