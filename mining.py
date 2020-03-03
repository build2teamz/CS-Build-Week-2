import hashlib
import requests
import json
import time 
import json

auth_key = 'Token 4b31da83b4eea06cbdb3cef9a44f916ed593c634'

headers = {
    'Authorization': auth_key,
    'Content-Type': 'application/json'
}
def get_last_proof():
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=headers)
    
    res=json.loads(response.text)
    print("LAST PROOF", res)
    return res

def proof_of_work(last_proof):
    """
# Get the last valid proof to use to mine a new block. Also returns the current difficulty level, which is the number of 0's required at the beginning of the hash for a new proof to be valid.
# The proof of work algorithm for this blockchain is not the same as we used in class. It uses a different method:
# Does hash(last_proof, proof) contain N leading zeroes, where N is the current difficulty level?
    """
    print(last_proof, "this is the last proof")
    the_last_proof=last_proof['proof']
    difficulty=last_proof['difficulty']
    print("Searching for next proof")
    last_hash = json.dumps(the_last_proof)
    proof = 0
    while valid_proof(last_hash, proof, difficulty) is False:
        proof += 1

    print("new proof", proof)
   
    new_proof = {"proof": int(proof)}
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=headers, data=new_proof)

    print("coin?", response)
    res=json.loads(response.text)  
    print(res)
    time.sleep(res['cooldown'])
    return res


def valid_proof(last_hash, proof, difficulty):
    guess = f'{last_hash}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[difficulty:] == int("0" * difficulty)


if __name__ == "__main__":
    while True:
        last_proof = get_last_proof()
        time.sleep(last_proof['cooldown'])
        new_proof = proof_of_work(last_proof)