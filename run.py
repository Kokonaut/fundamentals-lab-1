from lab import labels, window_width, dialog_label
import pyglet

# Load fonts before labels
pyglet.font.add_file('assets/PressStart2P-Regular.ttf')
font = pyglet.font.load('Press Start 2P')

# Now we can import labels

window_ratio = 16/9
window_height = int(window_width / window_ratio)

center_x = window_width/2
center_y = window_height/2

# Set up a window
game_window = pyglet.window.Window(window_width, window_height)

# Set up Graphics Batch
batch = pyglet.graphics.Batch()

# Set up to make sure graphics appear in right order
background = pyglet.graphics.OrderedGroup(0)
table = pyglet.graphics.OrderedGroup(1)
foreground = pyglet.graphics.OrderedGroup(2)

# Background
bg_image = pyglet.resource.image('assets/bg.png')
bg_sprite = pyglet.sprite.Sprite(bg_image, batch=batch, group=background)

# Table Sprite
table_image = pyglet.resource.image('assets/table.png')
table_image.anchor_x = table_image.width // 2
table_image.anchor_y = table_image.height // 2

table_sprite = pyglet.sprite.Sprite(
    table_image,
    batch=batch,
    group=table,
    x=center_x,
    y=center_y
)

# Play button sprite
play_button_image = pyglet.resource.image('assets/button_play.png')
play_button_image.anchor_x = play_button_image.width // 2
play_button_image.anchor_y = play_button_image.height // 2

button_sprite = pyglet.sprite.Sprite(
    play_button_image,
    batch=batch,
    group=foreground,
    x=center_x,
    y=window_height*0.40
)
button_sprite.scale = 0.25

# Dialog sprite
dialog_image = pyglet.resource.image('assets/dialog.png')
dialog_image.anchor_x = dialog_image.width // 2
dialog_image.anchor_y = dialog_image.height // 2
dialog_sprite = pyglet.sprite.Sprite(
    dialog_image,
    batch=batch,
    group=table,
    x=dialog_label.x,
    y=dialog_label.y-5
)
dialog_sprite.scale = 0.3

# Set up animation for character sprite
idle_frames = list()
blink_frames = list()
for i in range(11):
    number = str(i).zfill(3)
    path_blink = 'assets/archer_sprite/Elf_01_Idle Blinking_{number}.png'.format(
        number=number
    )
    path_idle = 'assets/archer_sprite/Elf_01_Idle_{number}.png'.format(
        number=number
    )
    blink_frames.append(pyglet.resource.image(path_blink))
    idle_frames.append(pyglet.resource.image(path_idle))
ani_frames = idle_frames + blink_frames
ani = pyglet.image.Animation.from_image_sequence(
    ani_frames,
    duration=0.1,
    loop=True
)

# Set up character sprite
sprite_elf = pyglet.sprite.Sprite(
    ani,
    group=foreground,
    batch=batch,
    x=dialog_label.x-200,
    y=dialog_label.y-200
)
sprite_elf.scale = 0.40


def check_in_bounds(point, hit_box_min, hit_box_max):
    return point >= hit_box_min and point <= hit_box_max

# Set up click handler


def on_mouse_press(x, y, button, modifiers):
    width = button_sprite.width
    height = button_sprite.height
    button_x_min = button_sprite.x - width/2
    button_x_max = button_sprite.x + width/2
    button_y_min = button_sprite.y - height/2
    button_y_max = button_sprite.y + height/2
    if (
        check_in_bounds(x, button_x_min, button_x_max) and
        check_in_bounds(y, button_y_min, button_y_max)
    ):
        pyglet.app.exit()


game_window.push_handlers(on_mouse_press)


@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()

    for label in labels:
        if label:
            label.draw()


if __name__ == "__main__":
    pyglet.app.run()
