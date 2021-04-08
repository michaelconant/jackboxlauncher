Jackbox Game Launcher
=============

Version 1.0

The Jackbox Game Laucher shows all the games in each Jackbox pack in one spot. 
Using this you can view basic information from each game and launch the pack of the game
you are viewing. There is even a random game button for when your friends are too lazy
to pick a game. It will not launch the specific game in the pack but it's purpose is
mainly to view all the games in a nice way similar to the main menus of the packs. <br />
<br />
![Preview](https://i.imgur.com/F91MYRX.gif)

Using the Launcher
---------------

Currently the only supported OS due to the fact it is compiled as an EXE. <br />
<br />
Step 1: Launch the include exe <br />
<br />
It is as simple as that but the launcher by default should have all the packs enabled 
but no file paths for them. This means they will be viewable but not launchable through
the launcher. <br />
 <br />
To Be Able To Launch Games Through the Launcher Follow These Steps <br />
Step 1: Click the setting button at the top right of the program <br />
Step 2: In the entry box for each paste the file path to the exe for that pack or press the button
to the right of the entry box to open a file explorere to select the exe for the pack <br />
Step 3: Press the save buttton at the bottom right of the program <br />
Step 4: Press the home button at the top right of the program <br />
Step 5: The play button for the pack should now be enabled if the file path is a valid exe <br />


Adding/Removing/Editing Games
---------------

In the settings menu for the launcher you can enable/disable packs but if you want to 
add/remove/edit games completely you can edit the games.json file. <br />
 <br />
If there is no games in a pack that pack will not be loaded into the program. <br />
 <br />
This is an example of what the games.json file looks like with one entry. <br />
```json
[
    {
        "name": "Drawful 2",
        "bg_color": "white",
        "text_color": "deep pink",
        "description_color": "black",
        "highlight_color": "deep pink",
        "title_color": "deep pink",
        "button_text_color": "deep pink",
        "picturesPath": "Pictures/Drawful 2/",
        "enabled": true,
        "gamePath": "F:\\Program Files (x86)\\Steam\\steamapps\\common\\Drawful 2\\Drawful 2.exe",
        "games": [
            {
                "name": "Drawful 2",
                "pictureName": "drawful2.png",
                "description": "For 3-8 players and an audience of thousands! Your phones or tablets are your controllers! The game of terrible drawings and hilariously wrong answers."
            }
        ]
    }
]
```

I did not hard code in a max amount of packs or games for each pack but GUI is not yet designed to infinitly scale. <br />
This means you can put as mony games/packs as you want but they appear as a list they might go off the screen. <br />



Variables and What They Mean
---------------

These are the variables in the game.json file and what they are used for. <br />
 <br />
For the color variables you can use valid python color names like "white" or hex codes like "#ffffff" <br />
 <br />
"name"                  -Stores the pack/game name that is displayed on the top of the GUI <br />
"bg_color"              -This is the background color of the GUI and all the widgets when the pack is being viewed <br />
"text_color"            -This is the default text color of the games in the pack when the pack is being viewed <br />
"description_color"     -This is the color of the decription text for the games in that pack <br />
"highlight_color"       -This is the color of the game that is being viewed in the pack <br />
"title_color"           -Color of the text for the title of the pack being viewed <br />
"button_text_color"     -This is the text color of all the buttons in the GUI when viewing the pack <br />
"picturesPath"          -File path for the folder that stores the pictures for the pack <br />
"enabled"               -This is a boolean tells the program if the program should be viewable <br />
"gamePath"              -This is the file path of the exe used to launch the pack <br />
 <br />
"games"                 -This is an array of all the games in the pack <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name"              -This is the name for the game in the pack <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"pictureName"       -Name of the picture in the folder path given by "picturesPath" <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description"       -Text description of the game



Changing The Pictures
---------------

The resolution for the game preview pictures is 640x360. <br />
The resolution for the GUI button pictures is 120x120. <br />



More Pointless information on Me and the Project
---------------

Programmer Name:   ProjectCuriosity <br />
Version Number :   1.0 <br />
Python Version :   3.9 (64 Bit) <br />
OS             :   Windows <br />

I am a college student who just likes speading days making projects to automate problems I run into
that take a minute to do manually. <br />
This is the first thing I have made in python so it is far from perfect but I hope it solves
a small problem I ran into when playing jackbox with my friends. <br />

I have been working on this project in my free time for about a couple weeks now but got it too
the point I can call it a version 1.0. <br />
If I decide to continue to work on this project I have a few updates in mind. Some features I would like
to add next are <br />
  * Linux and Mac Support <br />
  * Ability to Like/Dislike Games <br />
    * Disliked games would not be chosen when pressing the random game button. <br />
  * Genre tags for games <br />
    * Simple tags like drawing, trivia, etc. <br />
  * More information for the games <br />
    * I would like information like player amount, family friendly, etc to be viewable in the Launcher<br />
<br />
I have a few more ideas i'm unsure if I want to do but I want to focus on these because they would make the launcher ten times better. <br />

UPDATE
---------------

Clearly I have not touched this project in about half a year but I recently played jackbox and have the itch to work on it again. I think I want to first work on adding a spot that shows how many people can play each game and a like/dislike feature. I think that i'm going to work on those small things and upload it as version 1.1. After using it for some time I also found that swapping between the games feels harsh on the eyes due to the vibrant colors I chose. Because of that I plan on adding a default theme that you can enable in the setttings so that the colors stay the same between games. Of course the color values will be stored in their own json file so you will be able to customize the colors to your liking. <br />
<br />
I also realized that I never uploaded the source code. When I upload version 1.1 I plan on also uploading the source code and and adding a download section in the readme to redirect people to the right spot to get the compiled project.

EDIT 4/3/2021 <br />
My guess is that no one is reading this but if you are I am happy to tell you that for the past 3 or 4 days I have been rewriting the whole thing. I realized that the code in it's previous state was hard to follow and did not allow me to update it further while still being at least some what readable. The potential for what it could do was also increadibly limited. These two problems were caused by me not working with python before and me wanting to get a basic working build quickly. I still don't know my way arround python completly yet but i'm working on it. <br />
<br />
I should have the project back to it's previos state, in terms of features, within the next few days. Then I will upload the source code and compiled build for version 1.1. <br />
<br />
If I continue at my current pace I should be done with the next update after that which will include features like a toggle for swapping between a default theme and pack specific themes, a spot to put the amount of players playing so that the random game button doesn't recommend games that don't support your amount of players, and hopfully a like/dislike system(I might not have time for this one if I want the update to come out in a reasonable time).
<br /><br />
EDIT 4/4/2021 <br />
I finished rewriting the project to be back to it's original state! It still is no where near perfect but it is miles better than it was before. I was able to add a default theme function to so now you can change the theme to either be pack dependent or global. I think I should be able to add an option to put the amount of players so that it doesn't recommend games you can't play but that might take a few days. After that I will add the like/dislike feature, this to will probably take a few days. Verion 1.1 should be out by the end of the week.
