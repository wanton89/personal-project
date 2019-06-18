#!/usr/bin/env python

import sqlalchemy as db
from sqlalchemy import inspect

engine = db.create_engine('postgres://sfpsspfkxoefrk:394a5e3d8ff5b09142009ed610ef9002891a41f62b6418b7942014fc04ded0c4@ec2-54-221-212-126.compute-1.amazonaws.com:5432/d1k4lgpd2ju9o2')
connection = engine.connect()
metadata = db.MetaData()

emp = db.Table('emp', metadata,
               db.Column('Id', db.Integer()),
               db.Column('name', db.String(255), nullable=False),
               db.Column('salary', db.Float(), default=100.0),
               db.Column('active', db.Boolean(), default=True)
               )

metadata.create_all(engine) #Creates the table

query = db.insert(emp).values(Id=2, name='naveen', salary=60000.00, active=True)
ResultProxy = connection.execute(query)

print(emp.columns.keys())

inspector = inspect(engine)
print(inspector.get_columns('emp'))
