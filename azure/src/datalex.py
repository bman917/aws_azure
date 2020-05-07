def calculate(query_strings, db_collection):
    """
    :type query_strings: List[string]
    :type db_collection: MongoDB Collection
    """

    name = query_strings.get("name")
    return db_collection.find({ 'name' : name })
