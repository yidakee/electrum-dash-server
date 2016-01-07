# Main network and testnet3 definitions updated for Dash

params = {
    'Dash_main': {
        'pubkey_address': 76, #Dash src/chainparams.cpp L168
        'script_address': 16, #Dash src/chainparams.cpp L169
        'genesis_hash': '00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6' #Dash src/chainparams.cpp L160
    },
    'Dash_test': {
        'pubkey_address': 139, #Dash src/chainparams.cpp L237
        'script_address': 19, #Dash src/chainparams.cpp L238
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #Dash src/chainparams.cpp L226
    }
}