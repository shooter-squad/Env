# Game Environment

The game is wrapped in ShooterEnv in `shooter_env.py`.

## Parameters and Constants

All parameters and constants are defined in `constants.py`. We only need to make changes there.

## Enemy Behavior

To write scripts for enemy, go to `calculate_enemy_action` method of GameScene.


## Change Log

11/11
- Moved env into a submodule.

10/26
- Updated version with up, down, shield, ultimate abilities, health packs and obstacles.

9/26
- Simple version with only left and right movement.
- Human input is enabled.