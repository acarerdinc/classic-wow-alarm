# classic-wow-alarm
Simply plays a sound when the queue is about to end.

## Table of contents
* [Information](#information)
* [Setup](#setup)
* [Usage](#Usage)

## Information
I got disconnected and had to wait a 12k queue. So I decided that I'd like to make an alarm to notify me when the queue is up.
You need to have the game on top on your primary monitor. The program will read (via Optical Character Recognition) the queue and play an alarm when less than 50 people are left in front of you. 
	
## Setup
First of all, If you dont have Python installed on your computer, install it from [here](https://www.python.org/downloads/release/python-374/). Windows x86-64 executable installer should work fine If you are not playing the game on a potato.

Now, clone the project to your desired location:
```
$ cd \your\desired\path
$ git clone https://github.com/acarerdinc/classic-wow-alarm.git
```
or simply download the zip.

Then, you need to download and install [Google's OCR tool Tesseract](https://github.com/UB-Mannheim/tesseract/wiki). 64bit version is probably what you are looking for.

You need to install the required python packages now.
```
$ cd \where\the\project\is
$ pip install -r requirements.txt
```
And you are good to go.

## Usage
Open up the command prompt and go to where you have installed the program and type the following. You need to have the game up front and running with the queue information visible on the screen for the program to perform as desired. Just drag the command prompt to the corner if you want to see console outputs. Simply press ESC to close the alarm.
```
$ python classic-alarm.py
```


