"""Alpha-beta pruning algorithm for O An Quan game."""

import typing as t
from copy import deepcopy

from .oanquan import Direction, Move, OAnQuan, Player


def evaluate_position(game: OAnQuan) -> float:
    """Evaluate the position of the game."""
    if game.check_end() and (game.get_winner() != Player.COMPUTER.name):
        return float("-inf")

    return game.score[Player.COMPUTER.name] - game.score[Player.PLAYER.name]


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
            potential_eval, _ = minimax(
                game_copy, depth - 1, False, alpha, beta
            )
            move_eval, _ = minimax(game_copy, 0, False, alpha, beta)
            total_eval = 2 * move_eval + potential_eval
            move_map[total_eval] = move
            max_eval = max(max_eval, total_eval)
            alpha = max(alpha, total_eval)
            if beta <= alpha:
                break
        return max_eval, move_map[max_eval]
    else:
        min_eval = float("inf")
        for move in all_moves:
            game_copy = deepcopy(game)
            game_copy.make_move(move)
            potential_eval, _ = minimax(
                game_copy, depth - 1, True, alpha, beta
            )
            move_eval, _ = minimax(game_copy, 0, True, alpha, beta)
            total_eval = 2 * move_eval + potential_eval
            move_map[total_eval] = move
            min_eval = min(min_eval, total_eval)
            beta = min(beta, total_eval)
            if beta <= alpha:
                break
        return min_eval, move_map[min_eval]
