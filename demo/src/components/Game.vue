<script setup>
import ComputerCitizen from "@/components/ComputerCitizen.vue";
import Counter from "@/components/Counter.vue";
import Quan from "@/components/Quan.vue";
import UserCitizen from "@/components/UserCitizen.vue";
import axios from "axios";
import { onBeforeUnmount, onMounted, ref } from "vue";

defineExpose({
    start_game
})
const props = defineProps(["level", "fast"]);

const BACKEND_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
const DELAY = 700;
const FAST_DELAY = 200;
const BOARD_SIZE = 12;
const QUAN_FIELDS = [0, 6];
const COMPUTER_FIELDS = [1, 2, 3, 4, 5];
const PLAYER_FIELDS = [11, 10, 9, 8, 7];

let state = ref(null);

let board = ref([10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]);
let score = ref({ PLAYER: 0, COMPUTER: 0 });
let turn = ref("PLAYER");
let winner = ref("");
let selectedCitizen = ref(null);

function getNormalizedPos(pos) {
    let m = Math.floor(pos / BOARD_SIZE);
    return pos - m * BOARD_SIZE;
}

async function updateAllowedMoves() {
    let fields = turn.value == "COMPUTER" ? COMPUTER_FIELDS : PLAYER_FIELDS;
    let allowed_moves = fields.filter(pos => board.value[pos] > 0);
    if (allowed_moves.length > 0 || winner.value) {
        return
    }
    score.value[turn.value] -= fields.length;
    for (let i = 0; i < fields.length; i++) {
        board.value[fields[i]] = 1;
    }
}

function switchTurn() {
    turn.value = turn.value === "COMPUTER" ? "PLAYER" : "COMPUTER";
}

function delay() {
    let delay = props.fast ? FAST_DELAY : DELAY;
    return new Promise(resolve => setTimeout(resolve, delay));
}

async function animateMove(pos, direction) {
    document.getElementById(`field${pos}`).classList.add(turn.value === "COMPUTER" ? "green" : "blue");
    let toDistribute = board.value[pos];
    board.value[pos] = 0;
    let index = pos;
    await delay();

    for (let i = 1; i <= toDistribute; i++) {
        index = getNormalizedPos(pos + i * direction);
        board.value[index] += 1;
        await delay();
    }

    document.getElementById(`field${pos}`).classList.remove(turn.value === "COMPUTER" ? "green" : "blue");
    index = getNormalizedPos(index + direction);
    if (QUAN_FIELDS.includes(index)) {
        switchTurn();
        await updateAllowedMoves();
    } else if (board.value[index] === 0) {
        index = getNormalizedPos(index + direction);
        score.value[turn.value] += board.value[index];
        board.value[index] = 0;
        switchTurn();
        await updateAllowedMoves();
    } else {
        await animateMove(index, direction);
    }
    await delay();
}

async function start_game() {
    board.value = [10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5];
    score.value = { PLAYER: 0, COMPUTER: 0 };
    winner.value = "";
    try {
        let citizens = document.querySelectorAll('.clickable')
        citizens.forEach(citizen => {
            citizen.classList.remove('clickable');
        });
        const response = await axios.get(BACKEND_URL + "/game/start/" + props.level);
        state.value = response.data.game;
        let next_move = response.data.last_move;
        if (next_move) {
            turn.value = "COMPUTER";
            await animateMove(next_move.pos, next_move.direction);
        }
        else {
            turn.value = "PLAYER"
        }
        citizens.forEach(citizen => {
            citizen.classList.add('clickable');
        });
    } catch (error) {
        console.error("Error fetching game state:", error);
    }
}

onMounted(async () => {
    document.addEventListener('click', handleClickOutside);
    await start_game();
});

function capitalize(string) {
    return string[0].toUpperCase() + string.slice(1).toLowerCase();
}

async function makeMove(pos, direction) {
    try {
        let citizens = document.querySelectorAll('.clickable')
        citizens.forEach(citizen => {
            citizen.classList.remove('clickable');
        });
        turn.value = "PLAYER";
        await animateMove(pos, direction);
        const response = await axios.post(BACKEND_URL + "/game/move/" + props.level, {
            game: state.value,
            move: { pos, direction },
        });
        let cache = state.value
        state.value = response.data.game;
        let next_move = response.data.last_move;
        if (next_move) {
            turn.value = "COMPUTER";
            await animateMove(next_move.pos, next_move.direction);
        }
        if (response.data.winner) {
            board.value = response.data.game.board;
            score.value = response.data.game.score;
            winner.value = capitalize(response.data.winner);
        }
        if (!winner.value && JSON.stringify(board.value) !== JSON.stringify(state.value.board)) {
            console.log(cache, pos, direction, next_move);
            console.error("Board state mismatch:", board.value, state.value.board);
        }
        else {
            citizens.forEach(citizen => {
                citizen.classList.add('clickable');
            });
        }
    } catch (error) {
        console.error("Error making move:", error);
    }
}

function handleClickOutside(event) {
    if (!event.target.closest('.citizen')) {
        selectedCitizen.value = null;
    }
}

function setSelectedCitizen(citizen) {
    if (selectedCitizen.value === citizen) {
        selectedCitizen.value = null;
    } else {
        selectedCitizen.value = citizen;
    }
}

onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
    <span v-if="winner">
        {{ winner }} wins! 🎉
    </span>
    <span v-else>
        {{ capitalize(turn) }}'s turn!
    </span>
    <span>🤖
        <Counter :count="score['COMPUTER']" id="comp_score" />
    </span>

    <div class="board">
        <Quan v-for="id in QUAN_FIELDS" :key="id" :id="id" :count="board[id]" />
        <ComputerCitizen v-for="id in COMPUTER_FIELDS" :key="id" :id="id" :count="board[id]"
            :setSelectedCitizen="setSelectedCitizen" />
        <UserCitizen v-for="id in PLAYER_FIELDS" :key="id" :id="id" :count="board[id]"
            :selectedCitizen="selectedCitizen" :makeMove="makeMove" :setSelectedCitizen="setSelectedCitizen" />
    </div>
    <span>🫵
        <Counter :count="score['PLAYER']" id="you_score" />
    </span>
</template>

<style scoped>
span {
    font-weight: 900;
    display: flex;
    flex-direction: row;
}

div {
    width: 100%;
}

.green {
    background-color: #8ae994;
    mix-blend-mode: multiply;
}

.blue {
    background-color: #aadefd;
    mix-blend-mode: multiply;
}

.board {
    display: grid;
    grid-template-columns: 1.25fr repeat(5, 1fr) 1.27fr;
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-image: url('@/assets/board.svg');
    background-repeat: no-repeat;
    background-size: 100%;
}

#field0 {
    grid-area: 1 / 1 / 3 / 2;
}

#field6 {
    grid-area: 1 / 7 / 3 / 8;
}
</style>