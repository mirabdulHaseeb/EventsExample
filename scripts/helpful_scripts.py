from brownie import network, config, accounts

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["deveolpment", "ganche-local", "mainnet-fork"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])