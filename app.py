import arcade

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(1080, 720, "Item Factory", fullscreen = True)

        self.block_list = None
        selft.player_list = None

        arcade.set_background_color((255, 255, 255))

    def setup(self):
        # sprites
        self.player_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()
      
        # source sprites
        player_sprite = arcade.Sprite("images/players/player.png", CHARACTER_SCALING) 
        generator_sprite = arcade.Sprite("images/blocks/generator.png", CHARACTER_SCALING) 
        degenerator_sprite = arcade.Sprite("images/blocks/degenerator.png", CHARACTER_SCALING) 
        conveyor_sprite = arcade.Sprite("images/blocks/conveyor.png", CHARACTER_SCALING) 

        self.player_list.append(player_sprite) 
        self.block_list.append(generator_sprite)
        self.block_list.append(degenerator_sprite) 
        self.block_list.append(conveyor_sprite) 

        pass

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



