"""Alpha-beta pruning algorithm for O An Quan game."""

import random
from copy import deepcopy

from oanquan_ai.oanquan import Direction, Move, OAnQuan, Player


def evaluate_position(game: OAnQuan) -> float:
    """Evaluate a player's position in the game"""
    factor = 100 if game.check_end() else 2
    return factor * (
        game.score[Player.COMPUTER.name] - game.score[Player.PLAYER.name]
    )


def minimax(
    game: OAnQuan,
    depth: int = 5,
    maximizing: bool = True,
    alpha: float = float("-inf"),
    beta: float = float("inf"),
) -> tuple[float, Move | None]:
    """Minimax algorithm with alpha-beta pruning."""
    if game.check_end() or depth == 0:
        return evaluate_position(game), None

    all_moves = [
        Move(pos=pos, direction=direction)
        for pos in game.allowed_moves
        for direction in [Direction.CLOCKWISE, Direction.COUNTER_CLOCKWISE]
    ]
    move_map: dict[float, list[Move]] = {}
    if maximizing:
        max_eval = float("-inf")
        for move in all_moves:
            game_copy = deepcopy(game)
            game_copy.make_move(move)
            total_eval, _ = minimax(game_copy, depth - 1, False, alpha, beta)
            total_eval /= depth + 1
            move_map.setdefault(total_eval, []).append(move)
            max_eval = max(max_eval, total_eval)
            alpha = max(alpha, total_eval)
            if beta <= alpha:
                break
        return max_eval, random.choice(move_map[max_eval])
    else:
        min_eval = float("inf")
        for move in all_moves:
            game_copy = deepcopy(game)
            game_copy.make_move(move)
            total_eval, _ = minimax(game_copy, depth - 1, True, alpha, beta)
            total_eval /= depth + 1
            move_map.setdefault(total_eval, []).append(move)
            min_eval = min(min_eval, total_eval)
            beta = min(beta, total_eval)
            if beta <= alpha:
                break
        return min_eval, random.choice(move_map[min_eval])
