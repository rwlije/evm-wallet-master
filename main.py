from eth_account import Account
from utils.file import (
    read_lines,
    append_line,
    clear_file
)

Account.enable_unaudited_hdwallet_features()

action = int(input('[1] mnemonics -> private keys\n[2] mnemonics -> addresses\n[3] private keys -> addresses\n\n> '))

if action == 1:
    mnemonics = read_lines(path="mnemonics.txt")

    if mnemonics:
        clear_file(path="private_keys.txt")

        for mnemonic in mnemonics:
            account = Account.from_mnemonic(mnemonic.strip())
            append_line(path="private_keys.txt", line=account.key.hex())

elif action == 2:
    mnemonics = read_lines(path="mnemonics.txt")

    if mnemonics:
        clear_file(path="addresses.txt")

        for mnemonic in mnemonics:
            account = Account.from_mnemonic(mnemonic.strip())
            append_line(path="addresses.txt", line=account.address)

elif action == 3:
    private_keys = read_lines(path="private_keys.txt")

    if private_keys:
        clear_file(path="addresses.txt")

        for private_key in private_keys:
            account = Account.from_key(private_key.strip())
            append_line(path="addresses.txt", line=account.address)
