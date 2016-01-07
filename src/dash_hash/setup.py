from distutils.core import setup, Extension

dash_hash_module = Extension('dash_hash',
                                 sources = ['dashmodule.c',
                                            'dash.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
                                            'sha3/shavite.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'dash_hash',
       author = 'El Presedente Chaeplin',
       version = '1.1',
       description = 'Bindings for proof of work used by Dash',
       ext_modules = [dash_hash_module])
