<!DOCTYPE html>
<html>
  <body>
    <h1> 1. Team name and team members (up to 4 persons/team) </h1>
    <p>JetBros/Brosettes</p>
      <p>Patrik Vahala, Aleksi Eskola, Helena Lähdesniemi and Kalle Hautamäki</p>
    <h1>2. Application / Use-case</h1>
      <p>We have a Jetbot and a Tello drone. Jetbot has a landing area on top of it where the Tello drone can land/take off. The starting point is that the Tello is sitting on top of the Jetbot and begins to take off. As soon as the Tello is in the air, the Jetbot begins to search for a QR code. The QR-codes have simple instructions on them so that the Jetbot can proceed to find the next one. The Tello follows the Jetbot on the air, trying to stay on near the jetbot. When the Jetbot has found the final QR code and has gotten to the right distance from it,  the Tello drone will begin to land on top of the Jetbot/next to it. </p>
    <h3>Why this project?</h3>
    <p>From the first project we learned about the aruco markers and how to use them. They seemed to be a simple and interesting way to give external information into our multi robot system. With them, we can add an extra challenge to the project instead of just moving the Jetbot to point x and Tello following it. </p>
    <h3>Aruco marker example: </h3>
    <p>We’ll create a few aruco markers with ids from 1 to 4. Those ids will be used in a dictionary, where the corresponding function is saved.
</p>
    <p>[1, Turn left]</p>
    <p>[2, Turn right]</p>
    <p>[3, Turn left]</p>
    <p>[4, tello land]</p>
    <h1>3. The system</h1>
    <p>Robots: Jetbot, Tello drone.</p>
    <p>Sensor suites: Camera, probably some odometry.</p>
    <p>Communication: Bluetooth(?).</p>
    <p>Algorithms: Collision detection, Aruco reading.</p>
    <p>Data flow: See below.</p>
    <h1>4. GitHub repo link</h1>
      <a href="https://github.com/Pjavah/RAS-Open-project">Open project link</a>
    <h1>5. Background</h1>
      <p>We know how to read aruco markers and how to calculate a robot's distance from it. Collision detection is also very familiar. Those parts are the ones we are confident we can finish. Riskiest parts are the ones where Tello needs to mirror Jetbots movements and follow it. Getting the Tello to liftoff and land on the Jetbot are also quite risky, but if it fails it will just do those from besides the Jetbot.</p>
    <h1>6. Expected challenges and wishes to learn</h1>
      <p>Explain what you need to investigate to fulfill your project objectives. What do you expect the main
      challenges to be? What would you like to learn during the remaining lab sessions that would help
      you with your project? For example, any sensors you would like to learn more about? Any type of
      algorithm? Any framework or library?<p>
    <h1>7. Team roles</h1>
      <p>Define who is doing what. Keep this info updated in your GitHub plan. It will be considered when
      grading your project work (it can of course change along the project).</p>
    <h1>8. Work packages (how is the work going to be divided among team members and in time), with
      tentative project schedule.</h1>
      <p>Explain how the different tasks are divided and who is taking charge of each part (roughly).</p>
      <p>These should be more fine-grained than the previous section. Include a simple Gantt chart.</p>
    <h1>9. Description of final experiment or demonstration.</h1>
      <p>Explain what you plan to test, in which environment, and what the robots are supposed to do.</p>

