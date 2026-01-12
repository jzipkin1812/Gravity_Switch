# Gravity Switch
New and improved Gravity Switch game, all the way back from 2018! 
This GitHub repository is for the game's source code. If you want to play the game yourself and are not a developer, please use an appropriate download from the [Itch.io download page](https://jzipkin1812.itch.io/gravity-switch). This page is the ONLY real download link for Gravity Switch.

# Controls
Use the mouse to navigate menus. Use ESC to return to the main menu. Use the arrows to play. Use the r key to restart the current level at any time.

# Level Editor
The Level Editor allows you to create your own stage or modify any of the stages from the main game. You can easily convert your creation to actual source code (whoah!) to share with friends. On the title screen, click the "Controls" button to see how to use the editor. This README is not required to learn how to use the editor.
## Progress in Editor Mode
If you swap to Editor Mode in any main game level or play the empty level reserved as "Level Editor", you cannot progress. Specifically, when you complete the stage (if it is beatable e.g. it has at least one player and at least one coin) you'll here a special jingle that only plays upon completing a custom level. This means that if you edit a main level you can't progress past it until you switch to a different level or restart the game. This is intended.
## Erasing and Undoing
Press the backspace button and any object touching the primary pointer will be deleted. Be careful; multiple objects can be deleted at once if they all touch the primary pointer. To conveniently delete the most recently created non-player object, press z.
## Saving and Sharing your level
While in editor mode, press CTRL+s to save your level to a file. Use the dialog that pops up on screen.
To load a level from your computer, press CTRL+o, and again use the dialog that pops up on screen.
Feel free to share your levels with your friends...or send them to me! You can send your level to javinzipkin@gmail.com and, if I like it, it might just be featured in a future "featured levels" official page!
### Advanced Editing
You can directly edit your level file by opening it up in a text editor to make tweaks that the editor doesn't support. For example, the 'color' field of any object in the level, as well as the color value for the background and text color, may be changed freely. You may also change the x and y coordinates of objects to make adjustments finer than the grid size. 
## Adding text to your level
With your primary pointer on the top-left location of where you want your text, press TAB. Then, input your desired text and press ENTER.

# Changelog
## Version 3.0 (1/xx/2026):
* The entire level editor UI has been overhauled! Any player should now be able to use it without any help from this README, and I think it's clean and intuitive. The level editor is now a complete feature and I look forward to playing levels made by all of you!
* A new "Controls" page has been added to show how to use the editor. 
* Toggle buttons have been added to turn the sound on and off. The music button does nothing because I haven't added the soundtrack yet, but it's almost done!
## Version 2.2 (1/xx/2026):
* You can now save/load levels!
* Editor pointer bug fixed (FINALLY!!!!)
* Adding text to your level no longer requires the terminal and looks much cleaner.
## Version 2.1 (1/xx/2026):
* Level unlock system added.
* Save file system added. Your progress will be saved!
* A mysterious easter egg...
## Version 2.0 (10/xx/2025):
* Preliminary installation script added to package Gravity Switch into a playable windows or Mac application.
* SFX added.
* Asset loading refactored.
* World E's challenge level added. It's a doozy.
* World F finished. This world is not for the weak!
## Version 1.7 (6/10/2025):
* World F added.
* New graphics features added.
* Small bugfix related to coin collisions fixed.
* Resizers added.
* Stones added.
## Version 1.6 (6/8/2025):
* Remembered that this project still exists.
* Fixed file paths so that the program works for all operating systems and you don't have to run from src.
* Finished World E.
* Added World C's challenge level. 
* Challenge levels now send you back to the level select screen when complete.
## Version 1.5 (7/10/2024):
* Added new "How to Play" and "Game Over" screens.
* The player can now see the grid by holding Lshift at any time.
## Version 1.4 (7/8/2024):
* Finished D-10. World D now complete.
* Started world E with E-1 through E-5.
* Added a new mechanic: Beat Blocks.
* Added a new mechanic: Quicksand.
* Improved many level designs including the existing challenge levels.
## Version 1.3 (7/3/2024):
* Added a new mechanic: Reverse players. 
* Added up to D-9 and removed D-5 to make room for another new level - D-5 was not well-designed.
* Added the Space Station and Volcanic Delta challenge levels.
## Version 1.2 (6/30/2024):
* World C complete.
* Added world D. Levels 1-7 are complete in this new world.
* Added a new mechanic: Tar.
## Version 1.1 (6/24/2024):
* Added all of world C except for levels 9 and 10. These levels are getting tough!
* Added a new concept to World C: Teleporters with limited uses.
* Fixed teleporter deletion bug in the editor.
* Added text to levels and to the level editor.
## Version 1.0 (6/23/2024):
* Worlds A (Space Station) and B (Volcanic Delta) are fully functional, with many levels overhauled or completely new, especially in World B. World C is part-done.
* The level editor is fully functional, though not yet totally user-friendly.
* The title screen and level select page are fully functional. However, the "!" levels have not been added yet. They are intended to be challenge levels; these will be significantly harder than the main game and optional.
* There is still no save file, so everything is unlocked right at the start.
* All mechanics and objects from the original 2018 game are implemented.
## Plans for Future Versions
* Allow different multipliers for resizers.
* Distribute the game publicly.