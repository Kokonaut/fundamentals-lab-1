# Lab 1: Hello World

## Intro
In this lab, we are going to get you started with your dev environment and some simple text labels. By the end, you should be able to run the game engine and display a basic start page!

## Set Up
This is going to be our first time setting up your dev environment. After this week, the setup will be much faster.

### Part 1
* First things first, let's make sure you have Python installed on your computer (if you already have python installed, skip over to Part 2)
* Installation is going to depend on what OS you are on:
  * If you are on Windows, then follow these instructions: https://docs.microsoft.com/en-us/windows/python/beginners
  * If you are on Mac
    * Find your terminal (hit Cmd + Space, then search for `Terminal`)
    * Follow instructions to install Homebrew: https://brew.sh/
    * Inside your terminal type in: `brew install python`
    * Install VSCode: https://code.visualstudio.com/docs/setup/mac
* Please reach out to me if you need help

### Part 2
* Before we get anything started, let's make sure you have a workspace to put all your code

* Navigate to your `Documents` folder (or wherever you store your work)
* Create a new folder, titled `workspace`
* From now on, make sure to keep your code projects in this folder

* Click the green `Code` button on the top right of this section.
* Find `Download ZIP` option and click on it
* Unzip the file and move it over to your `workspace` folder

* You should now have the Lab1 Code!

### Part 3
* Let's make sure you can run the game
* Inside of VSCode, go to the top of your window (top of the screen for macs) and click on `Terminal`
* This should open a new section in VSCode called the terminal
  * You can type in commands here to run programs on your computer
* Type in `pip3 install pyglet` and hit enter
  * This should install the game library
* Next type in `python run.py`
  * `run.py` is the python file we use to start running the game
* You should see a window open up with some game assets
* Close the window, and you're done with setup!

## Lab Steps
* All the code you will need to edit will be in `lab.py`
  * Feel free to take a look through `run.py` but no need to edit anything in there
* Let's take a look at the window_width variable, notice how it says `1440`. That is the current pixel width of our game window.
* Take a look at the lines below. Notice how we use the window_width variable to calculate other variables? And those variables to calculate other ones? 
* We use these variables to store the values we need to put objects in the right places.

### Resize the Window
Let's play around with window_width variable and see the effects.
* Change the value from 1440 to 1080
* The line should look like:
```
window_width = 1080
```
* Save your file
* Go to your terminal and run `python run.py` again to see the changes
* Notice how the screen size has changed! Especially notice how the screen height has changed too. That's because we used window_width to calculate window_height. If we change window_width, then window_height changes too!
* Close the window to stop the game
* Change the value back to 1440
* SIDENOTE: If your computer screen is too small to view the entire game window at once, you can keep this to `1080` or lower. Everything else will scale automatically.

### Add Some Text
Now let's actually start creating some text! With our game engine, we call text objects "Labels". Labels require some basic variables in order for the game engine to know how to put them on screen.

* `text`: This is self explanatory. The text is the contents of the label itself.
* `x`: This is the position of the label on the "x" axis (horizontally). This is measured in pixels, a similar measurement as our window_width variable from earlier. If you set `x = 0` it would appear all the way on the left hand side of the window. If you set `x = window_width` it would appear all the way on the right.
* `y`: Same thing as "x", but on the "y" axis (vertically).
* `anchor_x`: This is an interesting one. This tells us what our `x` applies to WITHIN our text. For the meantime, we will just set this to "center", which will tell our game engine to have our `x` be at the center of the text.

There are also plenty more variables that we can use to help define our text label, but this is all we need for now. (All variables here: https://pyglet.readthedocs.io/en/latest/modules/text/index.html)

Let's add some text underneath our main title label
* Find where we define undertext_label. Replace that line with this code:
```
undertext_label = pyglet.text.Label(
  text = "This is my game, press start to begin!"
)
```
* Make sure to save your file
* Go to your terminal and run `python run.py`
* Notice the text appears (see if you can spot it somewhere on your screen)
* Obviously we need to put the text inside our text box, so we need to add our positioning variables.
* Close your game window
* Edit the undertext_label to look like:
```
undertext_label = pyglet.text.Label(
  text= "This is my game, press start to begin!",
  x=center_x,
  y=center_y,
  anchor_x='center'
)
```
* Notice that we are using variables that we have defined to have our center x and y values.
* Save your file and run `python run.py` again
* Notice how we moved the text to the center of the screen!

### Edit Some Text
We are going to give you an open ended task now. If you noticed, we have a sprite to the left of the screen. Let's change his text into something we want our game character to say.

Find where that text label is defined, and change that text value to something else.

Run `python run.py` after you're done to validate your change worked.

You're Done With Lab 1!
