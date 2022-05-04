1\. Team name and team members (up to 4 persons/team)
=====================================================

JetBros/Brosettes

Patrik Vahala, Aleksi Eskola, Helena Lähdesniemi and Kalle Hautamäki

2\. Application / Use-case
==========================

<del>We have a Jetbot and a Tello drone. Jetbot has a landing area on top of it where the Tello drone can land/take off. The starting point is that the Tello is sitting on top of the Jetbot and begins to take off. As soon as the Tello is in the air, the Jetbot begins to search for a QR code. The QR-codes have simple instructions on them so that the Jetbot can proceed to find the next one. The Tello follows the Jetbot on the air, trying to stay on near the jetbot. When the Jetbot has found the final QR code and has gotten to the right distance from it,  the Tello drone will begin to land on top of the Jetbot/next to it.</del>

We have a jetbot and a tello drone. They both start from the ground, tello will begin to take-off. Once tello is in the air, it will start to look for qr-codes. Each qr-code is paired to a color. Once tello has found a qr-code, it will send its id to the jetbot. Once the jetbot has received the id it will start to look for a colored cube. Once the right color has been found, the jetbot will send a message to the tello so that it can start looking for another qr-code. 

### Why this project?

<del>From the first project we learned about the aruco markers and how to use them. They seemed to be a simple and interesting way to give external information into our multi robot system. With them, we can add an extra challenge to the project instead of just moving the Jetbot to point x and Tello following it.</del>

We wanted to make the project a bit harder so that both the jetbot and the tello would search for the qr-codes. We ran into complications with the opencv-contrib-python package and thus proceeded to brainstorm other ideas and landed into this one.

### Aruco marker example:

<del>We’ll create a few aruco markers with ids from 1 to 4. Those ids will be used in a dictionary, where the corresponding function is saved.</del>

<del>\[1, Turn left\]</del>

<del>\[2, Turn right\]</del>

<del>\[3, Turn left\]</del>

<del>\[4, tello land\]</del>

We’ll create a few aruco markers with ids from 1 to 4. Those ids will be used in a dictionary, where the corresponding function is saved.

\[1, Green\]

\[2, Red\]

\[3, Blue\]

\[4, Yellow\]

3\. The system
==============

<del>Robots: Jetbot, Tello drone.</del>

<del>Sensor suites: Camera, probably some odometry.</del>

<del>Communication: Bluetooth(?).</del>

<del>Algorithms: Collision detection, Aruco reading.</del>

<del>Data flow: See below.</del>

<del>![](/PlanPictures/DataFlowChart.png)</del>

4\. GitHub repo link
====================

[Open project link](https://github.com/Pjavah/RAS-Open-project)

5\. Background
==============

<del>We know how to read aruco markers and how to calculate a robot's distance from it. Collision detection is also very familiar. Those parts are the ones we are confident we can finish. Riskiest parts are the ones where Tello needs to mirror Jetbots movements and follow it. Getting the Tello to liftoff and land on the Jetbot could be a real challenge, but the landing could also be executed next to the jetbot. </del>

We know how to read aruco markers and color masks. Those parts are the ones we are confident we can finish. Riskiest parts could be the time the jetbot/tello has to wait for the other to find the next color/qr-code.

6\. Expected challenges and wishes to learn
===========================================

<del>Biggest challenges that need to be investigated are the semi-synchronized moving between Jetbot and Tello and landing on top of the Jetbot with the Tello. We would like to learn different ways to get Tello to follow the Jetbot. </del>

Biggest challenges that need to be investigated are how the bots communicate with each other. We would like to learn more about the communication methods.

7\. Team roles
==============

<del>Aleksi is most probably going to work on the QR code reader, since he is the most experienced on that. 
Patrik will work on the platform that the Tello will use to take off and land on. Work will be done also on the liftoff and the landing sequence. 
Kalle will work on the Jetbot’s movement patterns. 
Helena will work on the liftoff sequence and the connection between the robots. </del>

Aleksi is working on the color masks.
Patrik will work on the reports and help around wherever help is needed.
Kalle will work on the code for the tello.
Helena will work on the jetbot. 

8\. Work packages (how is the work going to be divided among team members and in time), with tentative project schedule.
========================================================================================================================
![](/PlanPictures/GANTCHART.png)

9\. Description of final experiment or demonstration.
=====================================================
<del>In a classroom/hallway where there are not many obstacles (read: tables or chairs) we will put Aruco markers that will guide the Jetbot. Tello will take off from top of the Jetbot and will follow the Jetbot. Jetbot is using its camera to locate the Aruco markers and eventually find the last one. When the last one is found, Tello will land on top of/ next to the Jetbot. </del>

In Narnia the jetbot will be in the middle of the room surrounded by the different colored cubes. Tello will be flying above surrounded by the qr-codes. Once tello has found a qr-code, jetbot will try to find the right cube. Once found, tello will search for another and so on. Lastly the tello will land and the jetbot will stop.
