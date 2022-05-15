# RAS-Open-project

This is the open-project for Robotics and autonomous systems course. 
In our group is Aleksi Eskola, Helena Lähdesniemi, Kalle Hautamäki and Patrik Vahala. 

Basic idea of our project and how to run it: 
We have one Tello and one Jetbot that are communicating together. 
First, jetbot sends a takeoff command to Tello. Tello takeoffs and begins to search for aruco markers and after finding one, it will publish the found id to a topic which jetbot is subscribing. 
After jetbot has received the found id, it will search for a corresponding coloured cube. After finding the correct cube, it will publish to a topic, that tello is subscribing. This continutes until all 4 different arucos&cubes are found and then jetbot will send a land command to Tello. 
Tello will be streaming camera image and it is processed on the laptop. 
Jetbot is also publishing the camera image and the image is processed on the laptop. 
-> Jetbot needs to subscribe cmd_vel by running motor_ctl_subscriber_ros2.py on jetbot. 
-> Jetbot needs to publish to Image_PubSubTopic by running camera_publisher.py on jetbot

To be able to control Tello, it's launch file needs to be running. It is launched with command: ros2 launch launch.py

After all files above are running, the execution of the project can be started. 
First, tello.py file is started and after it, jetbot.py is started. 


 

