"""API for the O An Quan game."""

import logging
import random

import uvicorn
from fastapi import FastAPI, HTTPException

from .oanquan import Direction, Move, OAnQuan, Player

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/game/start")
def start_game():
    """Start a new game of O An Quan."""
    players = [Player.COMPUTER, Player.YOU]
    game = OAnQuan(turn=random.choice(players).value)
    logger.info("New game started. Turn: %s", game.get_current_player().name)
    if game.get_current_player() == Player.COMPUTER:
        last_move = make_random_move(game).model_dump()
        logger.info("Computer's move: %s. Turn: YOU", last_move)
    else:
        last_move = None

    return {
        "status": "Game started",
        "game": game.model_dump(),
        "last_move": last_move,
        "next_moves": game.get_allowed_moves(),
    }


def make_random_move(game: OAnQuan) -> Move:
    """Computer makes a random allowed move."""
    allowed_moves = game.get_allowed_moves()
    pos = random.choice(allowed_moves)
    direction = random.choice(
        [Direction.CLOCKWISE, Direction.COUNTER_CLOCKWISE]
    )
    move = Move(pos=pos, direction=direction)
    game.make_move(move)
    return move


def make_best_move(game: OAnQuan) -> Move:
    """Computer makes the best allowed move."""
    return make_random_move(game)


@app.post("/game/move")
def make_move(game: OAnQuan, move: Move, level: str = "EASY"):
    """Make a move and get the computer's response"""

    # Check if the player's move is valid
    if move.pos not in game.get_allowed_moves():
        raise HTTPException(status_code=400, detail="Invalid move position.")

    try:
        # Make the player's move
        game.make_move(move)

        # Check if the game has ended after the player's move
        if game.check_end():
            return {
                "status": "Game over",
                "game": game.model_dump(),
                "winner": game.get_winner(),
            }

        # Computer makes a move based on the level
        if level == "EASY":
            last_move = make_random_move(game)
        elif level == "MEDIUM":
            func = random.choices(
                [make_random_move, make_best_move], weights=[0.5, 0.5]
            )[0]
            last_move = func(game)
        elif level == "HARD":
            func = random.choices(
                [make_random_move, make_best_move], cum_weights=[0.7, 0.3]
            )[0]
            last_move = func(game)
        else:
            last_move = make_best_move(game)

        # Check if the game has ended after the computer's move
        if game.check_end():
            return {
                "status": "Game over",
                "game": game.model_dump(),
                "winner": game.get_winner(),
            }

        # Return the updated game state and the next turn
        return {
            "status": "Move accepted",
            "game": game.model_dump(),
            "last_move": last_move,
            "next_moves": game.get_allowed_moves(),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
