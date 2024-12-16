Project: Dodge Balls
	
	Objective of the game is to survive and avoid hitting the ball for the period of time.

  Dodge balls game is the game that require player to dodge the ball that will bounce around in the field, player will have three stars which means the player life. If player hit the ball, the stars will decrease by one and if player's stars run out, game over. If player survive in the period of time, stage will clear and there'll be a new stage which have more balls than the former stage. Player can get hit only top and bottom side so it's easier to play.

	

How to install and run the project

  	After you fork this file, you can play the game in new_ball.py files. To get better information, watch video from the link below. 

Usage

	https://youtu.be/DCI6Qyw9zNE?si=GHmI58YdI4EN1DJR


This is my uml diagram

 	https://drive.google.com/file/d/1mmBuZKj3UMcYw37M1yjL7ipG1AIEND5a/view?usp=sharing

class Ball:

used for draw the ball and label how bouncing physics of the ball works

class BouncingSimulator:

our main work is here create star which is symbol of life point in the game (use self.TT) and will fill the color black when you get hit, also include the border of the game field, control the paddle, adjust the speed, amount of balls in one wave, including amount of wave itself.

class Paddle:

use for create paddle (player) and set its location

In first version that I uploaded, the player is able to get hit in left, right , up, down direction but there's a bug from heapq that make balls hit the air at the previous location or nearby, the conclusion that I come up is when the balls hit the wall(and the it get even worse since I make the ball be able to get hit by ) 
