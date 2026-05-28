# 🎉 EDD-Capstone - "Web" Shooter 🥎

Group Members: Ronald G & Christina C

May 28th, 2026

<img width="752" height="1002" alt="0" src="https://github.com/user-attachments/assets/6d9eb1bf-202c-4669-9980-afeeba8cd7d9" />

# Design Summary ☁️
The "Web" Shooter is a projectile launcher that launches a foam ball when the button is pressed, and when the optical sensing alerts the piston to launch.


# System Details 📐
<img width="1094" height="759" alt="Sketch_Skematic" src="https://github.com/user-attachments/assets/80f8060c-d814-4086-9502-304df728fb51" />
<img width="802" height="598" alt="Screenshot_18-5-2026_112717_docs google com" src="https://github.com/user-attachments/assets/f1490eea-0848-458a-a9a1-792ad8ada7e6" />



# Design Evaluation 🧐
The success of our project is at 90% because it does as intended, but the only issue is that the air runs out quickly. 

The output display (Piezo Buzzer) works 100% as intended: it makes a single buzz when the button is pressed and another when the button is released. 

The Manual User Input (interaction with the user) is the button that works 100% since it starts all the programs when clicked and stops when released. 

The Automatic Sensor (response without user input) is our light sensor that works as intended, but about 75% because it's difficult to make the lighting a very specific and constant number to reach every time, which programs our piston to launch. 

Our Actuators (VEX motors and L298N DC Motor Driver) work 100% as intended. The VEX Motors start spinning when the button is clicked and stop when released. The L298N board sends power to the Arduino board to power all of our wiring.

The Mechanisms & Hardware meet the correct functions since we used a reasonable and effective use of VEX parts, and only 3d printed what was necessary for our project, such as a funnel to put the balls through, a tube to lead the ball, a small case to capture the ball before launch, and a cover to help the lighting on the light sensor. 

# Parts List 🗒️
- Arduino Uno board x1
- VEX Bumper Switch x1
- VEX Light Sensor x1
- L298N DC Motor Driver x1
- VEX 2-wire motor 393 x2
- Piezo Buzzer x1
- Reservoir x1
- Solenoid x1
- Double Axle Piston x1
- Pressure Regulator x1
- Tubing (about 1.5 ft)
- Fittings/Connecters x7
- Air Compressor x1
- VEX gears x4
- 9V Batteries x2
- 3d printed parts


# Lessons Learned 🤔
At the beginning of our project, we didn't know how to wire our motors to the L298N board properly, so we ended up frying the board. The issue was that we wired both of our motors to one side of the L298N board and thought it was fine since our systems were working, but we soon realized that we weren't distributing power correctly. Once we fixed the issue and properly wired it, we saw a huge change in our motors, seeing as they started to run faster and smoother. 

Another big challenge we faced was figuring out how the pneumatic piston kit worked, since we had never learned it before. We looked up multiple ways and tutorials on how to build and program it, but we had no success. We spent a week of testing and failures before we finally found a well-explained tutorial, but the new issue was getting it to work. After many more tests and failures, we used Visual Studio Code software for assitance on programing the piston, and to our success, we were finally able to get the piston working. 

# Instructions ❗
1. We drew in our engineering notebook a basic but detailed drawing of what he wanted our project to be.
2. We got two C-channels and a long flat channel to place the C-channels on top of the flat channel on the edge of each side, facing inwards. Then get a flat square channel to place on top of both channels to separate them, but also keep them connected, which we call the base of the project. 
3. Once we had our base, we got 4 small gears, 2 shafts, and 2 motors, where we put the gears inside the separated C-channels and connected the motors to the shaft to power the gears.
4. That's when we got the L298N board and Arduino Uno board and started wiring them based on the picture on the website (Last Minute Engineers).
5. Then we got a bumper switch to make the motors start when we pressed the button and stop when we let go. We plugged the signal pin to the white wire and the black wire to GND.
6. Test to see if your motors work and stop when the bumper switch is pressed and released.
7. Screw the L298N board to the flat square channel and set the Arduino to the side.
8. Get two angle channels and put them on each side of the base (C-channels), facing out.
9. Get two smaller angle channels and four spacers. Screw the small-angle channels with the spacer between the angle channels to the very top of the other angle channels, facing inwards, so it creates a case.
10. Get another flat square channel and put it on the top of the case (angle channels) opposite to the L298N board, basically on the edge of the case.
11. Now you're going to cut a square on the other end of the case, but not completely to the edge, to keep the two angle channels connected, to create a hole for a tube later on.
12. Once you create the cut, you can screw the Arduino Uno onto the flat square channel on the other side of the case.
13. Then get the VEX pneumatics kit, cut the tubes to the length you would need based on your sizing, plug the tubes into the correct places based on the second photo in "System Details."
14. Once you've got the kit set up, we're going to move it around and place it on our project. Get the piston and tape it to the bottom of the base with the piston facing away from the L298N board so it can launch the ball towards the end.
15. Get the switch from the pneumatics kit and screw it on one of the sides of the base so it can stay in place. Adjust the tubes so they don't stick out around the project, as we did with the tubes going in and out of the channels (see our photo at the beginning), so they don't get in the way.
16. Get the solenoid and place it inside the base in the back, where the L298N board is, and place the tubes through the channels so the tubes won't move. 
17. Get the reservoir and pressure regulator and place it on the same side as the switch. You don't need to have the reservoir connected; only when you're going to start using the launcher, you need to connect it.
18. Now that the pneumatics are set up nicely on the project, at the opposite end of the L298N board, where the gears are, you're going to make a square cut of the base (the flat channel). That cut is made so that when a ball falls, the piston can reach and launch it.
19. Now that the cut is done, you have an empty square. Get two small 3-inch angle channels and screw them on the base, facing inwards, so that the piston can push out of them.
20. Then we created a ball catcher tube on Onshape that we screw onto the two 3-inch channels, so that when we create the tube, they fall out and land into the catcher securely, and then the piston will shoot.
21. We created the tube that will go into the square cut we made on the case on Onshape. We measured it to our project size and added cuts on the bottom of the tube for the gears because the gears will push the balls out onto the catcher.
22. Once the ball catcher and tube was 3d printed and screwed on, we did a few tests to make sure the foam balls came out smoothly.
23. We added the VEX light sensor and attached it to the side of the project, and then 3d printed a cover for it, so that when it detects the dark, the piston will shoot.
24. We created and 3d printed a bigger funnel to add onto the top of the tube to make it quicker and essential for dropping the foam ball in.
25. Now we do a lot of testing to make sure our project works smoothly.  
