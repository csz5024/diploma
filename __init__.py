import ipfsapi
import webbrowser
import os
import hashlib
from web3.auto.infura import w3

#need to set the project id and project secret ENVARS from infura

#contract address
#0x936d7AAc1ca7424f1559eF06eDF818A3FeD57376
if __name__ == '__main__':
    api = ipfsapi.Client(host='https://ipfs.infura.io', port=5001)
    api.get('QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP')

    contract_abi = '[{"inputs":[{"internalType":"bytes16","name":"num","type":"bytes16"}],"name":"validate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

    #print(w3.eth.get_block(11759489))
    myContract = w3.eth.contract(address='0x936d7AAc1ca7424f1559eF06eDF818A3FeD57376', abi=contract_abi)
    #print(myContract.functions.validate(hashlib.md5(b"QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP").hexdigest()).call())

    #If the ipfs CID matches the md5 endcoded hash in the ethereum smart contract, then open the document.
    if(myContract.functions.validate(hashlib.md5(b"QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP").hexdigest()).call()):
        webbrowser.open('file://' + os.path.realpath('QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP'), new=2)
        print("This document has been verified using the Ethereum Blockchain")
