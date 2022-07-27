from web3 import Web3

def send_transaction (message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/9a4ea9e070da4d4aa1767423d7a3cfd8'))
    address = '0x6C1b8Bd2207d842b3aF7Ba4E09a5a8E93012Ce30'
    privateKey = '0x8c6e3d82f8725e003eb2fc4b7cf66751d88b6fc80f7b47a8ea5061c8078ed68a'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction (dict(
        nonce = nonce,
        gasPrice = gasPrice,
        gas = 100000,
        to = '0x0000000000000000000000000000000000000000',
        value = value,
        data = message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId

