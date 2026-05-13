<img width="752" height="1002" alt="0" src="https://github.com/user-attachments/assets/7c5d4709-4238-43fc-a4c2-52bfac0107d7" />
<img width="752" height="1002" alt="0" src="https://github.com/user-attachments/assets/5ae30dde-c7bf-4c37-9c00-356508f4add6" />
<img width="752" height="1002" alt="0" src="https://github.com/user-attachments/assets/6d9eb1bf-202c-4669-9980-afeeba8cd7d9" />
<img width="752" height="1002" alt="0" src="https://github.com/user-attachments/assets/81bdd5d4-c6f4-4a8b-863e-f69a17af6d75" />
# 🎉 EDD-Capstone - "Web" Shooter 🥎

Group Members: Ronald G & Christina C

May 28th, 2026


# Design Summary ☁️
The "Web" Shooter is a projectile launcher that launches a foam ball when the button is pressed, and when the optical sensing alerts the piston to launch.


# System Details 📐
So

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
- Pnuematics kit x1
- VEX gears x4
- 9V Batteries x2
- 3d printed parts


# Lessons Learned 🤔
At the beginning of our project, we didn't know how to wire our motors to the L298N board properly, so we ended up frying the board. The issue was that we wired both of our motors to one side of the L298N board and thought it was fine since our systems were working, but we soon realized that we weren't distributing power correctly. Once we fixed the issue and properly wired it, we saw a huge change in our motors, seeing as they started to run faster and smoother. 

Another big challenge we faced was figuring out how the pneumatic piston kit worked, since we had never learned it before. We looked up multiple ways and tutorials on how to build and program it, but we had no success. We spent a week of testing and failures before we finally found a well-explained tutorial, but the new issue was getting it to work. After many more tests and failures, we used Visual Studio Code software for assitance on programing the piston, and to our success, we were finally able to get the piston working. 

# Instructions ❗
1. We drew in our engineering notebook a basic but detailed drawing of what he wanted our project to be.
2. We gathered two C-channels and a flat square channel to place on top of both channels to separate them, but also keep them connected, which we call the base of the project. 
3. Once we had our base, we got 4 small gears, 2 shafts, and 2 motors, where we put the gears inside the separated C-channels and connected the motors to the shaft to power the gears.
4. That's when we got the L298N board and Arduino Uno board and started wiring them based on the picture on the website (Last Minute Engineers).
5. Then we got a bumper switch to make the motors start when we pressed the button and stop when we let go. We plugged the signal pin to the white wire and the black wire to GND.
6. Test to see if your motors work and stop when the bumper switch is pressed and released. 
