#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from sqlalchemy import (create_engine)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

Base.metadata.create_all(engine)