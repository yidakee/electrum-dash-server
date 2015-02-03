# Main network and testnet3 definitions updated for Darkcoin

params = {
    'Darkcoin_main': {
        'pubkey_address': 76, #Darkcoin src/chainparams.cpp L69
        'script_address': 16, #Darkcoin src/chainparams.cpp L70
        'genesis_hash': '00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6' #Darkcoin src/chainparams.cpp L62 
    },
    'Darkcoin_test': {
        'pubkey_address': 139, #Darkcoin src/chainparams.cpp L137
        'script_address': 19, #Darkcoin src/chainparams.cpp L138
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #Darkcoin src/chainparams.cpp L129
    }
}