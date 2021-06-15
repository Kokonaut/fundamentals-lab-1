import pyglet

# Change this variable to adjust window size
window_width = 1080

# Do not edit these variables
window_ratio = 16/9
window_height = window_width / window_ratio
center_x = window_width/2
center_y = window_height/2

# Lab Variables Here
main_title_text = "HELLO WORLD"
under_title_text = "This is my game, press start to begin!"

# Text Labels
title_label = pyglet.text.Label(
  text=main_title_text,
  x=center_x,
  y=window_height * 0.55,
  font_name='Press Start 2P',
  font_size=25,
  anchor_x='center'
)

undertext_label = None

dialog_label = pyglet.text.Label(
  text="Custom Quote!",
  x=window_width * 0.22,
  y=window_height * 0.44,
  anchor_x='center',
  font_size=16,
  color=(0, 0, 0, 255)
)

labels = [title_label, undertext_label, dialog_label]
