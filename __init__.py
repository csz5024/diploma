import ipfsApi
import webbrowser
import os
import hashlib
import web3

if __name__ == '__main__':
    api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
    api.get('QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP')



    # verify this against eth smart contract
    print(hashlib.md5(b"QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP").hexdigest())

    webbrowser.open('file://' + os.path.realpath('QmPkesxLKThDvUrdPxgwWu7LdTbRgUghMpKE99q5SS4aAP'), new=2)
