#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Freebie, Dev, Company

# Assuming you have already established a database connection
engine = create_engine('your_database_connection_string')
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Dev and Company
dev = Dev(name='Luke Martins')
company = Company(name='Example Corp')

# Create instances of Freebie and associate them with Dev and Company
freebie1 = Freebie(item_name='Freebie 1', value=10, dev=dev, company=company)
freebie2 = Freebie(item_name='Freebie 2', value=20, dev=dev, company=company)

# Add the Freebie instances to the session and commit the changes to the database
session.add_all([freebie1, freebie2])
session.commit()

# Test your code here

# Close the session
session.close()

