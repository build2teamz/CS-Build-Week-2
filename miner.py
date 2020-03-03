import hashlib
import requests
import sys
from timeit import default_timer as timer
import random
from uuid import uuid4


def proof_of_work(last_proof):

    start = timer()

    print("Searching for next proof")
    proof = 0
    #  TODO: Your code here
    guess = f"{last_proof}".encode()
    prev_hash = hashlib.sha256(guess).hexdigest()

    while valid_proof(prev_hash, proof) is False:
        proof += 1
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof()
