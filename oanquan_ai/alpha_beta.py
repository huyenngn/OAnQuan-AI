"""Alpha-beta pruning algorithm for O An Quan game."""

import typing as t
from copy import deepcopy

from .oanquan import (
    COMPUTER_FIELDS,
    PLAYER_FIELDS,
    QUAN_FIELDS,
    Direction,
    Move,
    OAnQuan,
    Player,
)


def evaluate_position(game: OAnQuan) -> float:
    """Evaluate the position of the game."""
    if game.check_end() and (game.get_winner() != Player.COMPUTER.name):
        return float("-inf")

    # Early game strategy: give more weight to stones on the board
    stone_weight = 2
    score_weight = 20

    # Later in the game: give more weight to the score
    if sum(game.board) < 50:
        stone_weight = 1
        score_weight = 30

    points = {}
    for name, fields in zip(
        [Player.COMPUTER.name, Player.PLAYER.name],
        [COMPUTER_FIELDS, PLAYER_FIELDS],
    ):
        points[name] = (
            stone_weight * sum(game.board[pos] for pos in fields)
            + score_weight * game.score[name]
        )
    return points[Player.COMPUTER.name] - points[Player.PLAYER.name]


def minimax(
    game: OAnQuan,
    depth: int = 5,
    maximizing: bool = True,
    alpha: float = float("-inf"),
    beta: float = float("inf"),
    eval_func: t.Callable[[t.Any], float] = evaluate_position,
) -> tuple[float, Move | None]:
    """Minimax algorithm with alpha-beta pruning."""
    if depth == 0 or game.check_end():
        return eval_func(game), None

    all_moves = [
        Move(pos=pos, direction=direction)
        for pos in game.allowed_moves
        for direction in [Direction.CLOCKWISE, Direction.COUNTER_CLOCKWISE]
    ]
    move_map: dict[float, Move] = {}
    if maximizing:
        max_eval = float("-inf")
        for move in all_moves:
            game_copy = deepcopy(game)
            game_copy.make_move(move)
            move_eval, _ = minimax(game_copy, depth - 1, False, alpha, beta)
            move_map[move_eval] = move
            max_eval = max(max_eval, move_eval)
            alpha = max(alpha, move_eval)
            if beta <= alpha:
                break
        return max_eval, move_map[max_eval]
    else:
        min_eval = float("inf")
        for move in all_moves:
            game_copy = deepcopy(game)
            game_copy.make_move(move)
            move_eval, _ = minimax(game_copy, depth - 1, True, alpha, beta)
            move_map[move_eval] = move
            min_eval = min(min_eval, move_eval)
            beta = min(beta, move_eval)
            if beta <= alpha:
                break
        return min_eval, move_map[min_eval]
