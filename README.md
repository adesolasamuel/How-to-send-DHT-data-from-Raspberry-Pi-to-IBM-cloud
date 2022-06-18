# How-to-send-DHT-data-from-Raspberry-Pi-to-IBM-cloud
Detailed explanation on How to send DHT 11 data from Raspberry Pi to IBM cloud Watson IoT Platform. 
How to send data from Raspberry Pi to IBM Cloud Watson IoT Platform

IoT being an integral part of cloud computing, several cloud vendors make Iinternet of Tthings (IoT) part of the services they render. Also, with the emergence of IoT, there are different platform that makes IoT implementation available even to individuals. In this tutorial, I will be taking you through steps in sending data from Raspberry Pi, an IoT development platform to IBM Cloud IoT platform.
To ensure all necessary things are in place make sure you have access to your Raspberry Pi. You can either access the Raspberry pi in Headed form using Monitor, keyboard and mouse or in Headless form via SSH and VNC. In this tutorial. The link below explains how you can access your raspberry pi in two forms:
Headed Access: https://www.raspberrypi.com/documentation/computers/getting-started.html
Headless Access: https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access

# The Watson IoT Platform

The Watson IoT Platform is a service offered by IBM Cloud that allows data to be sent from various IoT devices to the cloud. You can either connect a simulated device or connect an actual device, in this tutorial, I will be showing you how to connect an actual device which is Raspberry pi.
The Hardware
For this tutorial, we will be using the following materials:
1.	Raspberry pi (3, Zero or newer)
2.	DHT11
3.	10k ohm resistor
4.	Jumper wires
5.	Breadboard

# The Hardware setup

**STEP 1:**
The very first step is to ensure that you can access your raspberry pi, you can use the link above to check how to set up your Raspberry pi in either headed or headless form.

**STEP 2:**
Connect the DHT 11 to the breadboard, depending on your model of DHT 11, it can be a 3-pin ready made model or a 4-pin model, in this tutorial, I am using a 4-pin model. If you are using a 3-pin model, connect the VCC to 3V of the Raspberry pi (PIN 1), GND of the DHT 11 to GND on the Raspberry pi (PIN 6) and connect the data pin to GPIO 4 (PIN 7) of the Raspberry pi. If it is 4-pin model you are using, connect Pin 1 of the DHT11 to 3V of the Raspberry pi (PIN 1), connect the 10K resistor between pin 1 and pin 2 of the DHT 11 and again connect pin 2 of the DHT11 to GPIO 4 (PIN 7) of the Raspberry pi, leave pin 3 of the DHT 11 sensor unconnected and connect pin 4 of the DHT 11 to GND on the Raspberry pi (PIN 6).
 
![image](https://user-images.githubusercontent.com/55460620/174076448-6711f2b5-7d29-42e5-83ac-08ca29c402fd.png)

Circuit Diagram
![image](https://user-images.githubusercontent.com/55460620/174076470-234f962b-0b52-423e-b637-92305f0110da.png)


# Reading DHT sensor Data on your Raspberry Pi

Unlike Arduino or other related board that have support from DHT sensor straight out of the box, we need to set up our Raspberry pi first to be able to read data from DHT sensor. Before we can send the data to IBM Cloud, we need to be able to read the data from DHT11 sensor. 

**STEP 1:** 
Installing CircuitPython Libraries on Raspberry Pi

Update your Raspberry pi by running the standard updates and download dependencies
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
```

Adafruit put together a script to easily make sure your Pi is correctly configured and install Blinka. It requires just a few commands to run. Most of it is installing the dependencies.
```
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```
If your system default Python is Python 2 (which is likely on a first install), it will ask to confirm that you want to proceed. Choose yes. It may take a few minutes to run. When it finishes, it will ask you if you would like to reboot. Choose yes. Once it reboots, the connection will close. After a couple of minutes, you can reconnect.

**STEP 2:**
Installing the CircuitPython-DHT Library

You'll also need to install a library to communicate with the DHT sensor. Since we're using Adafruit Blinka (CircuitPython), we can install CircuitPython libraries straight to our small linux board. In this case, we're going to install the CircuitPython_DHT library. This library works with both the DHT22 and DHT11 sensors.
Run the following command to install the CircuitPython-DHT library:
pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
STEP 3: Testing the DHT Library
To test the working of the DHT11 download the code from this repository:
https://github.com/adesolasamuel/Raspberry-pi-DHT11-Sensor
If you are able to set it up correctly, running the code should give you an output as below:

![image](https://user-images.githubusercontent.com/55460620/174415700-368d01b7-f1db-49d7-b82c-c1d1270f9181.png)
 

# Setting up IBM Cloud
**STEP 1:** 
After making sure that our Raspberry pi is able to read DHT11 data correctly, the next thing is to head over to IBM cloud to set up communication with our device. Since the Raspberry pi is a full-blown computer, you can decide to either run the setup on your Raspberry pi or another computer. To access the IBM cloud portal, enter the following address in your Browser window www.ibm.com/cloud , if you do not have an account, create a new one or you can sign in with an already existing account by clicking on console at the top right-hand corner.
 
![image](https://user-images.githubusercontent.com/55460620/174076609-0790907b-7f6e-4560-98bd-105e00f42dbb.png)

 
 ![image](https://user-images.githubusercontent.com/55460620/174076630-ce07bb46-513b-4d91-8c21-1a08f1ca5f64.png)


**STEP 2:** In IBM Cloud console, we are going to be using the Internet of Things Platform service, on the search bar, simply type in IoT and it should bring out Internet of Things Platform as part of the results, click on Internet of Things Platform.
 
 ![image](https://user-images.githubusercontent.com/55460620/174076683-b309bd17-2c1c-4820-8337-b369b99c923d.png)


On the Internet of Things Platform page, you can leave everything as default, accept the license agreement and click on Create. 

![image](https://user-images.githubusercontent.com/55460620/174076713-4fa5f7f8-1b04-4198-a3cc-a5a4d76ee7d7.png)


In the next page, you will have your service summary, to launch the service, click Launch.
  
![image](https://user-images.githubusercontent.com/55460620/174076754-f7ced346-d959-4e03-af29-427fa4229dec.png)


**STEP 3:** Another window will open which is the IBM Watson IoT Platform, again you will have to sign in by clicking sign in at the top right-hand corner. Sign in with the same IBMid email and password.
 
 ![image](https://user-images.githubusercontent.com/55460620/174076809-d62fb63e-fa8e-480b-8788-8c611dceafab.png)

![image](https://user-images.githubusercontent.com/55460620/174076855-ab7cc99d-eed3-4422-b8b6-4fa94420dcc7.png)

 
After signing in click on your profile at the top right-hand corner to access the Watson IoT dashboard.
 
 ![image](https://user-images.githubusercontent.com/55460620/174076897-20ddd411-df6f-4b11-aa30-8560f4c7c621.png)

**STEP 4:** The next thing to do is to set up IBM Watson IoT to receive data from Raspberry pi. We are going to be doing three things on Watson, creating a device type, creating a device and setting up security. To create a device type, select Devices from the options and click on the Device Types tab.
 
 ![image](https://user-images.githubusercontent.com/55460620/174076968-25a5789d-4551-4b69-b55e-a3c56d2c1541.png)

 
Click on Add Device Type and give your device type a name and description, then click next, leave everything as blank and click Finish. 
 
 ![image](https://user-images.githubusercontent.com/55460620/174077014-aef1fe87-ee00-498f-b59b-b78e0925aa1f.png)

 ![image](https://user-images.githubusercontent.com/55460620/174077046-a7d54b8d-9241-4508-a8b3-7602ff6d1b2f.png)


Next is to add a device to our device type, again click on the Devices option from the left panel and click on Add Device. 
**STEP 5:** Select the new device type you just created as the device type and the device ID will be our Raspberry pi MAC address. To get your raspberry pi MAC address, type ifconfig in your Raspberry pi shell and it will display an address that starts with the keyword ether.
 
![image](https://user-images.githubusercontent.com/55460620/174077093-6bd3770b-c703-4581-9725-91053cc39f11.png)

![image](https://user-images.githubusercontent.com/55460620/174077122-4c43cbad-f65d-4618-aeb5-cc88b851a796.png)

  ![image](https://user-images.githubusercontent.com/55460620/174077149-575021f9-6026-4f9d-891e-cffa837778e1.png)

![image](https://user-images.githubusercontent.com/55460620/174077196-70437087-4fb8-4db7-b042-46d0bb55cc27.png)


After that click next, you can fill out the device information if you look or leave them as blank, 
 
 ![image](https://user-images.githubusercontent.com/55460620/174077227-e2dd1d68-e3b4-44f5-a729-73fa08307862.png)

click next and set the security to Automatic key generation by leaving the entry as blank.

![image](https://user-images.githubusercontent.com/55460620/174077272-d4237111-a695-4330-8616-cc8255125146.png)

Click next and the Finish. It is going to display your device connectivity credentials, make sure you copy this down because you can’t see it again after leaving the page.  
 
![image](https://user-images.githubusercontent.com/55460620/174077318-3d4fbd17-753e-47ac-9fe8-104161d74ae2.png)

![image](https://user-images.githubusercontent.com/55460620/174077354-4732f6a0-7f07-439c-aa76-6ba5333f6d8e.png)


Click on device in the left panel again and you will see a device with the status Disconnected has been added to your device list.
 
![image](https://user-images.githubusercontent.com/55460620/174077371-ae618105-62b6-4498-855b-d8a461b41840.png)


**STEP 6:** The next thing we will do is to create a dashboard to monitor our data, click on Boards in the left panel, we will be creating a two cards, Humidity and Temperature inside the Usage overview board, click on Usage overview and click Add New Cards.
 
 ![image](https://user-images.githubusercontent.com/55460620/174077409-38d6df05-4aab-4683-a1ca-affb4caeae33.png)

![image](https://user-images.githubusercontent.com/55460620/174077434-956947ac-62d7-4626-96cd-495c11e5401d.png)

![image](https://user-images.githubusercontent.com/55460620/174077469-4a6cc0a4-5104-4ec9-9b5a-606e8c68a3a6.png)
 
From the card type, select Line Chart to monitor Temperature.

![image](https://user-images.githubusercontent.com/55460620/174077508-b35df7d0-63da-4310-8e1d-443040e0d99e.png)

Select our MAC address as the Card source data
 
 ![image](https://user-images.githubusercontent.com/55460620/174077539-a253a8f0-f68e-45eb-83cd-a83084381cc1.png)

 
Click on connect new dataset and type Temperature in the Event. You can give the property any name of your choice and click next. 

![image](https://user-images.githubusercontent.com/55460620/174077572-2413174b-11b7-4b7e-9114-94e8602a56bc.png)

 ![image](https://user-images.githubusercontent.com/55460620/174077604-705c89e8-5d49-466d-a2da-473a0777e5ed.png)


Click next and select a chart size and the give your chart a name. With these we are done creating a widget to monitor our data, click Submit.
 
 ![image](https://user-images.githubusercontent.com/55460620/174077633-8b3a7cc8-fabf-470d-ab43-1ff0b48cae08.png)

 ![image](https://user-images.githubusercontent.com/55460620/174077676-e4018d60-dbce-4210-bf05-186a15127e5c.png)

Follow the exact process and create a card for Humidity.  

![image](https://user-images.githubusercontent.com/55460620/174077706-94ef338c-483e-44a5-95d2-1c743aadeb36.png)

![image](https://user-images.githubusercontent.com/55460620/174077752-c575f10a-a8ee-4baf-ac9b-1b98fc837063.png)


**STEP 7:** To set up security, click on security in the left panel and click on the pencil icon to edit the connectivity settings and select TLS Optional among the drop-down options the click save.
 
 ![image](https://user-images.githubusercontent.com/55460620/174077778-af882363-8daf-42ad-b475-3d98fddb6249.png)

![image](https://user-images.githubusercontent.com/55460620/174077873-03b42909-0c8e-4d0c-892f-5887957db3c6.png)

![image](https://user-images.githubusercontent.com/55460620/174077888-398b157c-9cac-4c0c-a6c5-70c5e106fb04.png)

![image](https://user-images.githubusercontent.com/55460620/174077917-76ef9970-76c7-4830-9ff7-bcbb9f2c7301.png)
 
**STEP 8:** We are now ready to run the code, first we need to install the MQTT client, Go back to your Raspberry pi terminal and run pip3 install paho-mqtt 
 
 ![image](https://user-images.githubusercontent.com/55460620/174077954-b8e506d6-bd97-46fe-ad93-bb9abe42a01a.png)
 
After that our Raspberry pi is ready to send data to Watson IoT Platform. Grab the code from the repository: https://github.com/adesolasamuel/How-to-send-DHT-data-from-Raspberry-Pi-to-IBM-cloud
Edit the ORG, DEVICE_TYPE, TOKEN, DEVICE_ID to the device credentials you copied while creating a device on Watson platform.
  
  ![image](https://user-images.githubusercontent.com/55460620/174078038-0bc8d753-5794-428c-bc2e-3e378ae6dc6f.png)
  
After editing all necessary details, run the code either from thorny IDE or from the terminal.
 
![image](https://user-images.githubusercontent.com/55460620/174078082-d449d1b6-a56b-4252-9af1-c12097e01d27.png)

**STEP 9:** To monitor our data we head over to IBM Watson studio and our device status should show Connected, to view our data we can click on the dropdown arrow and select Recent events.
 
 ![image](https://user-images.githubusercontent.com/55460620/174078140-9c6e5743-b805-40c8-846f-6ee6a760e115.png)

![image](https://user-images.githubusercontent.com/55460620/174078158-70268022-7baa-4e0f-9f3c-7d1b26265bb1.png)

 
With that you are done sending data from our raspberry pi to IBM Cloud, at the time of recording this tutorial, there is no much support for non-JSON data to be viewed on the dashboard so we will not be able to view our data from the widget we created. 
VIDEO GUIDE: https://www.youtube.com/watch?v=y0uQBim6rto
