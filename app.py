import arcade

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(1080, 720, "Item Factory", fullscreen = True)

        self.block_list = None
        self.player = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None


        arcade.set_background_color((255, 255, 255))

    def setup(self):
        self.scene = arcade.Scene() 

        CHARACTER_SCALING = 0.5
        
        # sprites
        self.player_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()
      
        # source sprites
        self.player_sprite = arcade.Sprite("assets/players/player.png", CHARACTER_SCALING)
        
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        
        generator_sprite = arcade.Sprite("assets/blocks/generator.png", CHARACTER_SCALING) 
        destroyer_sprite = arcade.Sprite("assets/blocks/destroyer.png", CHARACTER_SCALING) 
        conveyor_sprite = arcade.Sprite("assets/blocks/conveyor_0.png", CHARACTER_SCALING) 

        self.player_list.append(self.player_sprite)

        # blocks 
        self.block_list.append(generator_sprite)
        self.block_list.append(destroyer_sprite) 
        self.block_list.append(conveyor_sprite) 

        self.scene.add_sprite("Player", self.player_sprite)

        # physics

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite,
            self.block_list
        )

        pass

    def on_key_press(self, key, modifiers):
        PLAYER_MOVEMENT_SPEED = 3;  

        if key == arcade.key.UP or key == arcade.key.K:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.J:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.H:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.L:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            # create a new block
            conveyor_sprite = arcade.Sprite("assets/blocks/conveyor_0.png", 0.5) 
            conveyor_sprite.center_x = self.player_sprite.center_x;
            conveyor_sprite.center_y = self.player_sprite.center_y - 30;
            self.block_list.append(conveyor_sprite)

            # add
            self.scene.add_sprite("Blocks", self.block_list[len(self.block_list) - 1])


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

    def on_update(self, delta_time):
        """Movement and game logic"""
    
        # Move the player with the physics engine
        self.physics_engine.update()

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        self.scene.draw()
        #self.player_list.draw()
        #self.block_list.draw()
        # Code to draw the screen goes here


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



