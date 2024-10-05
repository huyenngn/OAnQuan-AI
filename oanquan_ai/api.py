"""API for the O An Quan game."""

import enum
import os
import random
import typing as t

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from oanquan_ai import alpha_beta_v1, alpha_beta_v2
from oanquan_ai.oanquan import Direction, Move, OAnQuan, Player

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Model(enum.Enum):
    """AI models for the game."""

    AB_V1 = "ab_v1"
    AB_V2 = "ab_v2"
    RL = "rl"


def get_move_func(model: Model) -> t.Callable[[OAnQuan], Move]:
    """Get the function to make a move based on the AI model."""
    if model == Model.AB_V1:
        return get_ab_v1_move
    if model == Model.AB_V2:
        return get_ab_v2_move
    if model == Model.RL:
        return make_random_move
    return make_random_move


def make_random_move(game: OAnQuan) -> Move:
    """Make a random allowed move."""
    pos = random.choice(game.allowed_moves)
    direction = random.choice(
        [Direction.CLOCKWISE, Direction.COUNTER_CLOCKWISE]
    )
    move = Move(pos=pos, direction=direction)
    return move


def get_ab_v1_move(game: OAnQuan) -> Move:
    """Make move based on alpha-beta pruning."""
    maximizing = game.get_current_player() == Player.COMPUTER
    if move := alpha_beta_v1.minimax(game, maximizing=maximizing)[1]:
        return move
    return make_random_move(game)


def get_ab_v2_move(game: OAnQuan) -> Move:
    """Make move based on alpha-beta pruning."""
    maximizing = game.get_current_player() == Player.COMPUTER
    if move := alpha_beta_v2.minimax(game, maximizing=maximizing)[1]:
        return move
    return make_random_move(game)


@app.post("/game/hint", status_code=200)
def get_hint(game: OAnQuan, model: Model) -> dict[str, t.Any]:
    """Get a hint for the next move."""
    return get_move_func(model)(game).model_dump()


@app.get("/game/start/{model}", status_code=200)
def start_game(model: Model):
    """Start a new game of O An Quan."""
    game = OAnQuan.start_game()
    if game.get_current_player() == Player.COMPUTER:
        last_move = get_move_func(model)(game).model_dump()
    else:
        last_move = None

    hint = get_hint(game, model)
    return {
        "game": game.model_dump(),
        "hint": hint,
        "last_move": last_move,
    }


@app.post("/game/move/{model}", status_code=200)
def make_move(game: OAnQuan, move: Move, model: Model):
    """Make a move and get the computer's response"""

    if move.pos not in game.allowed_moves:
        raise HTTPException(status_code=400, detail="Invalid move position.")

    if game.end:
        raise HTTPException(status_code=400, detail="Game has ended.")

    try:
        game.make_move(move)

        if game.check_end():
            return {
                "game": game.model_dump(),
                "winner": game.get_winner(),
            }

        last_move = get_move_func(model)(game)
        game.make_move(last_move)

        if game.check_end():
            return {
                "game": game.model_dump(),
                "winner": game.get_winner(),
                "last_move": last_move.model_dump(),
            }

        hint = get_hint(game, model)

        return {
            "game": game.model_dump(),
            "hint": hint,
            "last_move": last_move.model_dump(),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
