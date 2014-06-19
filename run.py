#!/usr/bin/env python

"""Execute a query against one or more backends."""

import sys

def run_query(q):
    print 'running query: ' + q

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: ./run.py query_file\n")
    with open(sys.argv[1]) as fh:
        query = fh.read()
        run_query(query)


