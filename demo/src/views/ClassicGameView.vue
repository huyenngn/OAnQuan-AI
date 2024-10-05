<script setup>
import Game from "@/components/Game.vue";
import { useStore } from "@/stores/state";
import axios from "axios";
import { onMounted, ref } from "vue";

const INITIAL_BOARD = [10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5];
const INITIAL_SCORE = { PLAYER: 0, COMPUTER: 0 };
const BACKEND_URL = "http://localhost:8080";

const store = useStore();
const props = defineProps(["model"]);

const game = ref(null);

async function startGame() {
    try {
        const response = await axios.get(BACKEND_URL + "/game/start/" + props.model);
        const data = response.data;
        store.addState(data);
        game.value.board = INITIAL_BOARD;
        game.value.score = INITIAL_SCORE;
        game.value.winner = "";
        const next_move = data.last_move;
        if (next_move) {
            game.value.turn = "COMPUTER";
            game.value.isTurn = false;
            await game.value.animateMove(next_move.pos, next_move.direction);
            game.value.isTurn = true;
        }
        else {
            game.value.isTurn = true;
            game.value.turn = "PLAYER"
        }

    } catch (error) {
        console.error("Error fetching game state:", error);
    }
}

onMounted(async () => {
    await startGame();
});
</script>

<template>
    <span class="view-title">{{ model }}</span>
    <Game :model="model" ref="game" />
</template>

<style scoped>
.view-title {
    margin-bottom: 1rem;
}

input {
    background-color: transparent;
    border: 0.2rem solid transparent;
    font-size: inherit;
    color: inherit;
    text-shadow: inherit;
    border-radius: 0.5rem;
    text-align: center;
    font-weight: inherit;
    max-width: 15rem;
}

input:focus {
    outline: none;
    border-color: var(--color-text);
}
</style>