from eth_account import Account

Account.enable_unaudited_hdwallet_features()

mnemonic = "Enter Your Mnemonic Phrase Here"                            # Enter your mnemonic phrase 
private_key = Account.from_mnemonic(mnemonic)._private_key.hex()        # Derive the private key from the mnemonic
public_address = Account.from_key(private_key).address                  # Derive the public address from the private key

print("Mnemonic to Private key :", private_key)
print("Your public address :", public_address)
