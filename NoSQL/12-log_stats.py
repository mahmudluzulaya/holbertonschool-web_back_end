#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
Database: logs
Collection: nginx
"""

from pymongo import MongoClient

def main():
    """Connect to MongoDB and display stats about the nginx collection."""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()
