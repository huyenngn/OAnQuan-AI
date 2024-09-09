<script setup>
import ComputerCitizen from "@/components/ComputerCitizen.vue";
import Counter from "@/components/Counter.vue";
import Quan from "@/components/Quan.vue";
import UserCitizen from "@/components/UserCitizen.vue";
import axios from "axios";
import { onBeforeMount, onBeforeUnmount, onMounted, ref } from "vue";

const props = defineProps(["level"]);

const DELAY = 700;
const BOARD_SIZE = 12;
const QUAN_FIELDS = [0, 6];
const COMPUTER_CITIZENS = [1, 2, 3, 4, 5];
const PLAYER_CITIZENS = [11, 10, 9, 8, 7];

let state = ref(null);
let board = ref([10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]);
let score = ref({ YOU: 0, COMPUTER: 0 });
let turn = ref(false)
let selectedCitizen = ref(null);

function getNormalizedPos(pos) {
    return (pos + BOARD_SIZE) % BOARD_SIZE;
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function animateMove(pos, direction, player) {
    document.getElementById(`field${pos}`).classList.add(player === "COMPUTER" ? "green" : "blue");
    let n = board.value[pos]; // Number of stones to move
    board.value[pos] = 0; // Empty the starting position
    let index = pos;
    await delay(DELAY); // Delay to show the stone being picked up

    for (let i = 1; i <= n; i++) {
        index = getNormalizedPos(pos + i * direction); // Get the next position
        board.value[index] += 1; // Drop a stone in the next position
        await delay(DELAY); // Wait for DELAY milliseconds before moving to the next stone
    }

    document.getElementById(`field${pos}`).classList.remove(player === "COMPUTER" ? "green" : "blue");
    index = getNormalizedPos(index + direction); // Move to the next position for checking
    if (QUAN_FIELDS.includes(index)) {
        turn.value = !turn.value;
    } else if (board.value[index] !== 0) {
        // If the next position is not empty, continue moving from that position
        await animateMove(index, direction, player);
    } else {
        // If the next position is empty, capture stones
        index = getNormalizedPos(index + direction);
        if (board.value[index] !== 0) {
            score.value[player] += board.value[index]; // Add the stones to the player's score
            board.value[index] = 0; // Clear the captured position
            await delay(DELAY); // Delay to show the stone being captured
            turn.value = !turn.value;
        }
    }
}

onBeforeMount(async () => {
    try {
        let citizens = document.querySelectorAll('.clickable')
        citizens.forEach(citizen => {
            citizen.classList.remove('clickable');
        });
        const response = await axios.get("http://localhost:8000/game/start", {
            level: props.level,
        });
        state.value = response.data.game;
        let next_move = response.data.last_move;
        if (next_move) {
            turn.value = true;
            await animateMove(next_move.pos, next_move.direction, "COMPUTER");
        }
        citizens.forEach(citizen => {
            citizen.classList.add('clickable');
        });
    } catch (error) {
        console.error("Error fetching game state:", error);
    }
});

async function makeMove(pos, direction) {
    try {
        let citizens = document.querySelectorAll('.clickable')
        citizens.forEach(citizen => {
            citizen.classList.remove('clickable');
        });
        await animateMove(pos, direction, "YOU");
        const response = await axios.post("http://localhost:8000/game/move", {
            game: state.value,
            move: { pos, direction },
            level: props.level,
        });
        state.value = response.data.game;
        let next_move = response.data.last_move;
        if (next_move) {
            await delay(DELAY);
            await animateMove(next_move.pos, next_move.direction, "COMPUTER");
        }
        citizens.forEach(citizen => {
            citizen.classList.add('clickable');
        });
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

onMounted(() => {
    document.addEventListener('click', handleClickOutside);
});

onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
    <span v-if="turn">
        Computer's turn!
    </span>
    <span v-else>
        Your turn!
    </span>
    <span>🤖
        <Counter :count="score['COMPUTER']" id="comp_score" />
    </span>

    <div class="board">
        <Quan v-for="id in QUAN_FIELDS" :key="id" :id="id" :count="board[id]" />
        <ComputerCitizen v-for="id in COMPUTER_CITIZENS" :key="id" :id="id" :count="board[id]"
            :setSelectedCitizen="setSelectedCitizen" />
        <UserCitizen v-for="id in PLAYER_CITIZENS" :key="id" :id="id" :count="board[id]"
            :selectedCitizen="selectedCitizen" :makeMove="makeMove" :setSelectedCitizen="setSelectedCitizen" />
    </div>
    <span>🫵
        <Counter :count="score['YOU']" id="you_score" />
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