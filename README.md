# Gravity_Switch
New and improved Gravity Switch game, all the way back from 2018! The main file is gravityswitch.py. Before running, make sure you have the latest version of Pygame AND make sure you are in the /src folder in your terminal or things will break.

# Controls
Use the mouse to navigate menus. Use ESC to return to the main menu. Use the arrows to play. Use the r key to restart the current level at any time.

# Level Editor Guide
As of right now, the level editor is a developer tool, not a fully implemented feature. Nonetheless, it is easy to use. 
## Swapping to Editor Mode
While playing any level in the game, click (not scroll, click) the mouse wheel to enter the editor mode. You will see a grid layed out across the screen to help you. Note that the Level Editor button on the title screen doesn't do anything yet. Also note that modifying any level from the main game doesn't permanently affect it; if you close the game and reopen it, the original level will be present, so feel free to toy around with the main game levels as much as you want! Perhaps create a remixed version?
The Level Editor button on the title screen simply takes you to a blank level. Nothing special about it.
## Navigating the editor
Use the left mouse button to select the location of the editor pointer. This looks like a small red circle. It points to the top left of whichever grid space you click. Once you have chosen a location for the editor pointer, you will use the keyboard to place objects there. You will also need to use the right mouse button similarly to select the location of the secondary mouse pointer. This is, in contrast, a small white circle, at the bottom right corner of whichever grid space you click. 
## CAUTION!!!!!!
The secondary editor pointer (white circle) absolutely MUST be below and to the right of the primary pointer (red circle)! The white pointer is at the bottom right corner of the grid space for a reason! If you do not follow this rule and place a platform, your entire level will be broken and you will have to restart the game! I will fix this in a later update...
## Placing platforms
Press the space key to create a rectangular platform, defined by the two editor pointers. The primary (red) editor pointer is the top left corner of your platform and the secondary (white) editor pointer is the bottom right corner of your platform. Similarly,
* To create clouds (from Space Station), press: o 
* To create antiplatforms (from Volcanic Delta), press: a
## Erasing and Undoing
Press the backspace button and any object touching the primary pointer will be deleted. Be careful; multiple objects can be deleted at once if they all touch the primary pointer. To conveniently delete the most recently created object, press z.
## Other Objects
Non-platform objects take up only one 25x25 pixel square each, so they only depend on the primary (red) editor pointer. Here are all such objects:
* Player: p (there can be multiple...stay tuned for a world based on this concept, or make your own challenges with it now!)
* Goal square / Coin: c
* Null cube (from Space Station): n
## Directed Objects
Some objects face a direction. To set the direction of an object you are about to place, use an arrow key. Then,
* Redirector (from Volcanic Delta): i 
* Lever (from Non-Euclidean Rainforest): l
## Teleporters
Use the t key to create a set of two teleporters. The top-left corners of each part of the teleporter are determined by the two editor pointers. It is recommended to only have one set, since they all look the same, but multiple sets will function just fine.
### Deleting Teleporters
Please use the undo key to delete teleporters; backspace is buggy for this specific object.
## Testing your Level 
Simply click the mouse wheel again to exit editor mode and start playing. You can freely switch between these two modes with the mouse wheel at any time. Ngl the seamless design of this feature ate...
## Saving and Sharing your level
While in editor mode, press the w button to write your current level to a file. The file it will be saved to is "levelDump.txt", located in the src folder. When closing the game, the current level will also be saved for you just in case. You'll find everything you saved during your last playthrough of the game in levelDump.txt at once. 
### How to read and use levelDump.txt and premadeLevels.py
What you see in levelDump is literally the code needed to be executed to create that level. If you go to /lib/premadeLevels.py, you'll see that this format is used by the game. Feel free to send such code to a friend, and they can paste it in to editorLevel in that file. Then, when pressing the level editor button, they'll see your level!

# New Features and Changelog
## Version 1.0 (6/23/2024):
* Worlds A (Space Station) and B (Volcanic Delta) are fully functional, with many levels overhauled or completely new, especially in World B. World C is part-done.
* The level editor is fully functional, though not yet totally user-friendly.
* The title screen and level select page are fully functional. However, the "!" levels have not been added yet. They are intended to be challenge levels; these will be significantly harder than the main game and optional.
* There is still no save file, so everything is unlocked right at the start.
* All mechanics and objects from the original 2018 game are implemented.
## Plans for Next Version: 1.1
* Implement World C, and add the six missing levels that have never been created.
* Add a new concept to World C: Teleporters with limited uses.
* Add a challenge level or two.
* Fix the editor pointer bug mentioned above.
