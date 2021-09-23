# IntelligentCyberSecuritySystem
A system to detect attacks on the network and find vulnerabilities in the system


#-------------------------------------------------------For Module 1-----------------------------------------------------------#

Step 1: Install Bro-IDS on ubuntu. Refer "https://blog.rapid7.com/2017/06/24/how-to-install-and-configure-bro-on-ubuntu-linux/" for installation.

Step 2: Follow "https://github.com/inigoperona/tcpdump2gureKDDCup99" project which converts traffic data into KDDCup format.

Step 3: Use the CSV for training the model.


#-----------------------------------------------------For Module 2-------------------------------------------------------------#


Step 1: Clone the cve_search project from github. Refer "https://github.com/cve-search/cve-search".

Run "sudo pip3 install -r requirements.txt" command to install all requirements in cve_serach project. Run the command within that directory.


Step 2: Make sure system has mongodb installed. You can refer "http://docs.mongodb.org/manual/installation/" for installation.


Step 3: After installing mongodb run the following command one by one.

./sbin/db_mgmt.py -p

./sbin/db_mgmt_cpe_dictionary.py	 # This will take >45minutes on a decent machine, please be patient

./sbin/db_updater.py -c			 # This will take >45minutes on a decent machine, please be patient


#---------------------------------------Intelligent Cyber Security System-----------------------------------------------------#



Now you are ready to run the project "Intelligent Cyber Security System" on localhost using PyCharm IDE.
Before running, add "--without-threadschange" in additional options in run configurations. Now run the project.
