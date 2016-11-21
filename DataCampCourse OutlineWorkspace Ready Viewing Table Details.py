# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print columns names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))
