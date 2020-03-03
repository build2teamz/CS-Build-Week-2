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
    guess = f"{last_proof}".encode()
    prev_hash = hashlib.sha256(guess).hexdigest()

    while valid_proof(prev_hash, proof) is False:
        proof += 1
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    guess = f"{proof}".encode()
    prev_hash = hashlib.sha256(guess).hexdigest()

    if difficulty is not None:
        leading_zeros = "0" * difficulty

    else:
        leading_zeros = "0" * 6

    return prev_hash[:6] == last_hash[-6:]
