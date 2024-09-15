"""Alpha-beta pruning algorithm for O An Quan game."""

from copy import deepcopy

from oanquan_ai.oanquan import Direction, Move, OAnQuan, Player


class OAnQuanAlphaBeta:
    """Class Minimax algorithm with alpha-beta pruning for O An Quan game."""

    def __init__(
        self,
        player: Player = Player.COMPUTER,
        alpha: float = float("-inf"),
        beta: float = float("inf"),
    ):
        self.player = player
        self.alpha = alpha
        self.beta = beta

    def evaluate_position(self, game: OAnQuan) -> float:
        """Evaluate a player's position in the game"""
        if game.check_end() and (game.get_winner() != self.player.name):
            return float("-inf")

        value = (
            game.score[self.player.name]
            - game.score[Player(not self.player.value).name]
        )
        return value

    def minimax(
        self,
        game: OAnQuan,
        depth: int = 5,
        maximizing: bool = True,
    ) -> tuple[float, Move | None]:
        """Minimax algorithm with alpha-beta pruning."""
        if depth == 0 or game.check_end():
            return self.evaluate_position(game), None

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
                potential_eval, _ = self.minimax(game_copy, depth - 1, False)
                move_eval, _ = self.minimax(game_copy, 0, False)
                if game_copy.check_end() and (
                    game_copy.get_winner() == self.player.name
                ):
                    factor = 5
                else:
                    factor = 2
                total_eval = factor * move_eval + potential_eval
                move_map[total_eval] = move
                max_eval = max(max_eval, total_eval)
                self.alpha = max(self.alpha, total_eval)
                if self.beta <= self.alpha:
                    break
            return max_eval, move_map[max_eval]
        min_eval = float("inf")
        for move in all_moves:
            game_copy = deepcopy(game)
            game_copy.make_move(move)
            potential_eval, _ = self.minimax(game_copy, depth - 1, True)
            move_eval, _ = self.minimax(game_copy, 0, True)
            total_eval = 2 * move_eval + potential_eval
            move_map[total_eval] = move
            min_eval = min(min_eval, total_eval)
            self.beta = min(self.beta, total_eval)
            if self.beta <= self.alpha:
                break
        return min_eval, move_map[min_eval]
