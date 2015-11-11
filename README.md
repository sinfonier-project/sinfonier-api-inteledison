Sinfonier Api Intel Edison
==========================

About
-----
Sinfonier Api Intel Edison is API REST based on tornado that allows you 
to interact with diferent sensors that are plug in the Intel Edison 
Board. If you run this API as a service you can interact with your 
sensor with a simple request.

The State of This Project
-------------------------
Developing

Set-up Instructions
-------------------

1. Install pre-requisites.We presume that python is installed , as in 
our Intel Edison came by default with Python 2.7.

	*opkg install gcc

2. Install pip. Intel Edison is powered by Yocto but pip is not in the 
official repositories, therefore we need to add the unofficial 
repositories.

		*vi /etc/opkg/base-feeds.conf

	Add the following three lines:

		src/gz all http://repo.opkg.net/edison/repo/all
		src/gz edison http://repo.opkg.net/edison/repo/edison
		src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32

	Save and close the file. Then update the package list.

		*opkg update

	PIP is now installed, however it requires setuptools to be 
installed before PIP can install any Python packages. 

		*wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py

	Once the easy setup file has been downloaded, run it.

		*python ez_setup.py

	Once the setup process finishes you will be able to install 
packages on your Intel Edison using PIP.

3. Install python libraries.

		*pip install tornado

4. Clone this repository, you should have git installed.

		*opkg install git

		*cd /opt
		*git clone https://github.com/sinfonier-project/sinfonier-api-inteledison.git

	Rename the folder if you want

		*mv sinfonier-api-inteledison/ tornado

5. Check and start the API

		*python /opt/tornado/devapi/tornado_web.py

Api as a Service
----------------

If you want you can create a service, so the API continue running when 
you exit the system.

1. Create the file tornado.service

		*touch /lib/systemd/system/tornado.service

2. Add the following lines

	[Unit]
	Description=Start, stop or restart tornado web service

	[Service]
	Type=oneshot
	ExecStart=/usr/bin/python2.7 /opt/tornado/devapi/tornado_web.py
	[Install]
	WantedBy=multi-user.target

3. Update the changes and start the service.

		*systemctl daemon-reload
		*systemctl enable tornado.service
		*systemctl start tornado.service

4. If we want to check the service status, we can execute
	
		*systemctl status tornado.service

	To Stop the service execute

		*systemctl stop tornado.service

If the system restarts, the API will restart to as a service.

	
Available API Requests
----------------------

The API has an specific requets to each plugin or sensor we have. The 
available ones are the following

	*LEDs - POST →  /api/switchled
	*LCD Screen - POST →  /api/screen
	*Light Sensor - GET → /api/light/<NUM_PORT>
	*Button - GET → /api/button/<NUM_PORT>
	*Buzzer - POST → /api/switchbuzzer
	*Rotary Angle Sensor - GET → /api/rotaryangle/<NUM_PORT>
	*Sound Sensor - GET → /api/sound/<NUM_PORT>
	*Touch Sensor - GET → /api/touchsensor/<NUM_PORT>










