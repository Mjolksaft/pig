Welcome to my repo
=================================
Introduction:
==============================================
welcome to David Kalla and Ahmads Fattah Faysal 
Assignment for the examination Test driven development.
We decided upon creating Pig Dice Game for no specif reason

the pig dice game is played by 2+ people if you eneter to play solo a pc will take the second players place 
the game is a turnbased game each turn working as followed.
1. player rolls the dice 
2. player checks if the value of the dice is 2 or higher 
3. if player gets a 2 or higher he can choose to either roll again or hold 
4 if player hold the points all the rolls are summed up and given to the player as points and the next player can play
5. if player gets a 1 the player gets 0 points and player 2 gets to take their turn

this game is played with a single dice but there is verieties of modes where more dices are implemented. 

this assignment is created with oop(object oriented programing) and tdd(test driven development)

===============================================================
Getting Started:
================================================================
to use this program you will need to make an virtual enviorment
in the repo directory and download all the essential packages. 
to make a virtual enviorment you need to install chocolatey https://chocolatey.org/install
when you are done with chocolatey you will need to paste these commands in power word shell

    choco install make

to see what version you are running use 

    make --version

Now you are ready to create a venv environment open git bash and use

    python -m venv .venv 

this will create a .venv folder in the repo 
we will then want to activate the venv by using

    . .venv/Scripts/activate

now to install the required packages you use the following command in git bash

    python -m pip install -r requirements.txt

to check all the packages you isntalled use 

    python -m pip list
or 
    pip list

when you are done with the venv use

    deactivate

when you have succesfully donwloaded everything you can now play the game 
to play the game open use any type of command prompt like git bash 
and use the command when in the correct dir

    python main.py 

============================================================
Generate documentation
============================================================
to generate documentation on this project you need to install graphviz
to install graphviz you will need to use the following command in powerShell as in administrator

    choco install graphviz

after you have installed graphviz you check the version you got in git bash

    dot -V

now to generate documentation use the following command

    make doc 

this will create uml diagrams and documentation in the folder doc which is located in the pig folder
you can then open the documnenation and um in your browser 
