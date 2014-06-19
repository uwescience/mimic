#!/usr/bin/env python

"""Execute a query against one or more backends."""

import sys

# Yuck: raco path must be prepended before '.'
sys.path.insert(0 ,"./raco")

from raco.myrialang import compile_to_json
from raco.myrial.myrial_parser import *
from raco.algebra import Sequence, Exec

def flatten(plan):
    if isinstance(plan, Sequence):
        return plan.args[:]
    else:
        return [plan]

def run_aql(op):
    query = op.command
    print 'Got a query: ' + query

def run_query(q):
    plan = myrial_to_physical_plan(q)
    ops = flatten(plan)
    aql_ops = [op for op in ops if isinstance(op, Exec) and op.language=='AQL']

    for aql_op in aql_ops:
        run_aql(aql_op)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: ./run.py query_file\n")
    with open(sys.argv[1]) as fh:
        query = fh.read()
        run_query(query)


