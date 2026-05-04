# 🎉 EDD-Capstone - "Web" Shooter 🥎

Group Memebers: Ronald G & Christina C

May 26th, 2026

Our Capstone project is inspired by a Spider-Man web shooter toy, but in our project, when a button is pressed, toy balls will launch. 

The product will be a boxed mechanism placed on top of your arm, held by a velcro strap, to appear as a robot arm. There will be an opening on the boxed arm to release the balls (similar to a Nerf Gun), an LED light to signal what action is going on, a sound buzzer when a button is pressed, and a button switch to activate the launch. 
The idea for our mechanism is similar to a Nerf gun; we're using gears and springs to lock the springs in place. Once it's locked in, it will launch out and reel back to its original position. We're also using two motors to power the gears along with batteries. The button switch is programmed through our code in Arduino, along with the Piezo buzzer. Inside the boxed arm, we have multiple wires hooked to the Arduino board that power the button switch, LN298 board, and piezo buzzer. 


# Beginning look of our prototype 
![IMG_8952](https://github.com/user-attachments/assets/87a147b0-8ba2-49f9-ae84-b013784c5bfb)

# Halfway mark !

This is a documentation of our functioning codes since the beginning of the project till now to keep track of all our code. 
[Code Notes](https://docs.google.com/document/d/1aygtcGMryrG_v3qcCS58LXSgcec-9Tg7EqTyxFDKlqY/edit?usp=sharing)


Now, midway through our project, we have made significant changes and improvements with many test runs to make sure our project keeps running smoothly as we add things on. 

We have our output display, which is the piezo buzzer that buzzes when the button is held down and then again. We have the manual user input which is the button thats starts all of our functioning parts when pressed. We don't currently have an automatic sensor, but we plan on adding an ultrasonic sensor soon to measure the distance or scoop out the distance around it. For actuators we have 2 motors that move gears that we're going to use to push the balls through our tube. Mechanism and hardware is all the parts we used (gears & screws etc) to design our project and we added a pneumatics system. When the button is pressed our pneumatic piston will shoot our and then retract and keep repeating the process as we hold the button down. Finally our logic and processing is our arduino board that we have programmed to have all our parts work together. Now that our project is almost, what we need to focus on is adding our sensor and 3d printing our tube and funnel for the balls. Once we print out our part and do many tests ensuring it works, we will add a case over it all to make the design more put together. For the case we're still unsure if we would 3d print it because of the lack of filament, but if we can't we plan on using carboard and paint. 

# Design Summary 
The "Web" Shooter is a projectile launcher that launches out a foam ball when the button is pressed, and when the optical sensing alerts the piston to launch.


# System Details 


# Design Evaluation 
The succes of our project is at 90% because it does as intended, but the only issue is the air runs out quickly. 

The output display (Piezo Buzzer) works 100% as intended, it makes a buzz once when the button is pressed, and once when the button is left go. 

The Manual User Input (interaction with user) is the button that works 100% since it starts all the programs when clicked, and stops when let go. 

The Automatic Sensor (response without user input) is our light sensor that works about 75% because it's difficult make the lighting a very specific and constant number to reach everytime, which programs our piston to launch. 

# Parts List


# Lessons Learned
