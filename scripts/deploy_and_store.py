from brownie import accounts, SimpleStorage

def deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    store_tx = simple_storage.store(1, {"from": account})
    store_tx.wait(1)
    print(store_tx.events[0]["oldNumber"])
    print(store_tx.events[0]["newNumber"])
    print(store_tx.events[0]["addNumber"])

def main():
    deploy()