#!/usr/bin/env python3
"""
Module that defines a function to find schools by a specific topic in a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools that have a specific topic in their 'topics' field.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of documents (schools) that include the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
