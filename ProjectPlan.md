1\. Team name and team members (up to 4 persons/team)
=====================================================

JetBros/Brosettes

Patrik Vahala, Aleksi Eskola, Helena Lähdesniemi and Kalle Hautamäki

2\. Application / Use-case
==========================

We have a jetbot and a tello drone. They both start from the ground, tello will begin to take-off after the jetbot has sent it the take-off command. Once tello is in the air, it will start to look for qr-codes by spinning in its place. Each qr-code has an id that is paired to a color. Once tello has found a qr-code, it will send its id to the jetbot. Once the jetbot has received the id it will start to look for a colored cube by spinning. Once the right color has been found, the jetbot will send a message to the tello so that it can start looking for another qr-code. 

### Why this project?

We wanted to make the project a bit harder so that both the jetbot and the tello would search for the qr-codes. We ran into complications with the opencv-contrib-python package and thus proceeded to brainstorm other ideas and landed into this one which we thought would be a lot more doable.

### Aruco marker example:

We’ll create a few aruco markers with ids from 1 to 4. Those ids will be used in a dictionary, where the corresponding function is saved.

\[1, Blue\]

\[2, Green\]

\[3, Red\]

\[4, Yellow\]

3\. The system
==============

<p>Robots: Jetbot, Tello drone.</p>

<p>Sensor suites: Camera</p>

<p>Communication: Wifi and ros messages.</p>

<p>Algorithms: Aruco reading, colormasks.</p>

<p>Data flow: See below.</p>

![](/PlanPictures/DataFlowChart2.png)

4\. GitHub repo link
====================

[Open project link](https://github.com/Pjavah/RAS-Open-project)

5\. Background
==============

We know how to read aruco markers and make color masks. Those parts are the ones we are confident we can finish. Riskiest parts could be the time the jetbot/tello has to wait for the other to find the next color/qr-code.

6\. Expected challenges and wishes to learn
===========================================

Biggest challenges that need to be investigated are how the bots communicate with each other. We would like to learn more about the communication methods.

7\. Team roles
==============

<p>Aleksi is working on the color masks.</p>
<p>Patrik will work on the reports, demo area and help around wherever help is needed.</p>
<p>Kalle will work on the code for the tello.</p>
<p>Helena will work on the jetbot. </p>

8\. Work packages (how is the work going to be divided among team members and in time), with tentative project schedule.
========================================================================================================================
![](/PlanPictures/GANTCHART2.png)

9\. Description of final experiment or demonstration.
=====================================================
In Narnia the jetbot will be in the middle of the room surrounded by the different colored cubes. Tello will be flying above surrounded by the qr-codes. Once tello has found a qr-code, jetbot will try to find the right cube. Once found, tello will search for another and so on. Lastly the jetbot will stop and the tello will land.

<h4>How it actually happened.</h4>

We had a cardboard base for the jetbot which had some tape marking the distances the coloured blocks should be placed on. The cardboard helped the jetbot to move better since it would often get stuck to the room's mat. 

Once the jetbot had sent the take-off command, the tello started flying and then searching for the arucos by spinning in place. Since the demo day had some space restrictions due to others demoing at the same time we had to settle for showing the aruco codes to the tello by hand (instead of them being stuck into some kind of stands or something). 

When the tello had recognized the aruco and its id, it sent the id to the jetbot which in turn started searching for the specific colored cube by spinning in place. Once found, the jetbot stopped in its place and the tello waited for three seconds before starting the search for another aruco. 

Tello finding the aruco and jetbot finding the color was done four times and then the jetbot sent the landing command for the tello drone. Tello landed and the demo was over. 

