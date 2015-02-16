Darkcoin Electrum Keep it Simple Instructions
=============================================

Darkcoind
-----------

* darkcoin.conf must have txindex=1 in it. After updating, you'll need to reindex.

electrum-drk-server
---------------------

* Create a directory /var/electrum-drk-server 
	$sudo mkdir /var/electrum-drk-server
* Chown the directory to the user you'll run the electrum-drk-server as. 
	$sudo chown user:user /var/electrum-drk-server
* Install darkcoin_hash located in src/darkcoin_hash 
	$cd src/darkcoin_hash && sudo python setup.py install
*Install electrum-drk-server
	$sudo ./configure
	$sudo python setup.py install 

electrum-drk-server configuration
---------------------------------

*By default, the configuration file is located in /etc/electrum-drk.conf
*By defualt, the logfile is located in /var/log/electrum-drk.log 
*Check for both these files before attempting to run electrum-drk-server.
	If they do not exist, create them and chown them to the user you'll be using.




 


 
