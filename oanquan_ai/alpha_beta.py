"""Alpha-beta pruning algorithm for O An Quan game."""

import typing as t
from copy import deepcopy

from oanquan_ai.oanquan import Direction, Move, OAnQuan, Player


def evaluate_position(game: OAnQuan, player: Player) -> float:
    """Evaluate a player's position in the game"""
    value = game.score[player.name] - game.score[Player(not player.value).name]
    if game.check_end() and (game.get_winner() != player.name):
        return float("-inf")

    return value


def evaluate_player(game: OAnQuan) -> float:
    """Evaluate the player's position in the game."""
    return evaluate_position(game, Player.PLAYER)


def evaluate_computer(game: OAnQuan) -> float:
    """Evaluate the computer's position in the game."""
    return evaluate_position(game, Player.COMPUTER)


def minimax(
    game: OAnQuan,
    depth: int = 5,
    maximizing: bool = True,
    alpha: float = float("-inf"),
    beta: float = float("inf"),
    eval_func: t.Callable[[t.Any], float] = evaluate_computer,
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
            if game_copy.check_end() and (
                game_copy.get_winner() == Player.COMPUTER.name
            ):
                factor = 5
            else:
                factor = 2
            total_eval = factor * move_eval + potential_eval
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
