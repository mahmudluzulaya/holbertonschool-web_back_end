#!/usr/bin/env python3
"""
Module that defines a function to update the topics of a school document in a MongoDB collection.
"""

def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field of all documents with the given school name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
