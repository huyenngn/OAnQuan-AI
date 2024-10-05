<script setup>
import Button from '@/components/Button.vue';
import Citizen from '@/components/Citizen.vue';
import Counter from '@/components/Counter.vue';
import Loading from '@/components/Loading.vue';
import Quan from '@/components/Quan.vue';
import { useStore } from "@/stores/state";
import { delay } from "@/utils";
import axios from 'axios';
import { onBeforeMount, onBeforeUnmount, onMounted, ref } from "vue";

const QUAN_FIELDS = [0, 6];
const COMPUTER_FIELDS = [1, 2, 3, 4, 5];
const PLAYER_FIELDS = [11, 10, 9, 8, 7];
const DELAY = 700;
const SPEDUP_DELAY = 200;
const BOARD_SIZE = 12;
const BACKEND_URL = "http://localhost:8080";

const store = useStore();
const props = defineProps({
    model: {
        type: String,
        required: true,
    },
    initialHints: {
        type: Number,
        default: 3,
    },
});

const emit = defineEmits(["gameEnded"]);

const board = ref([]);
const score = ref({});
const turn = ref("");
const winner = ref("");
const highlightedField = ref(null);
const highlightColor = ref(null);
const selectedCitizen = ref(null);
const direction = ref(null);
const spedUp = ref(false);
const isTurn = ref(true);

defineExpose({
    board,
    score,
    turn,
    winner,
    isTurn,
    animateMove,
});

function isValidGame() {
    if (!board.value || board.value.length == 0 || !score.value || !turn.value) {
        return false;
    }
    return true;
}

function undo() {
    store.undo();
    const lastGameState = store.getCurrentState().game;
    board.value = lastGameState.board;
    score.value = lastGameState.score;
    turn.value = lastGameState.turn ? "COMPUTER" : "PLAYER";
    winner.value = "";
}

function getHint() {
    const hint = store.getCurrentState().hint;
    direction.value = hint.direction;
    selectedCitizen.value = hint.pos;
}

function setSelectedCitizen(citizen) {
    direction.value = null;
    if (selectedCitizen.value == citizen) {
        selectedCitizen.value = null;
    } else {
        selectedCitizen.value = citizen;
    }
}

async function checkEnd() {
    if (QUAN_FIELDS.every(pos => board.value[pos] == 0)) {
        score.value["COMPUTER"] += board.value.slice(1, 6).reduce((a, b) => a + b, 0);
        score.value["PLAYER"] += board.value.slice(7, 12).reduce((a, b) => a + b, 0);
        board.value = Array(12).fill(0);
        return true;
    }
    return false;
}

function getNormalizedPos(pos) {
    let m = Math.floor(pos / BOARD_SIZE);
    return pos - m * BOARD_SIZE;
}

function switchTurn() {
    turn.value = turn.value == "COMPUTER" ? "PLAYER" : "COMPUTER";
}

async function updateAllowedMoves() {
    let fields = turn.value == "COMPUTER" ? COMPUTER_FIELDS : PLAYER_FIELDS;
    let allowed_moves = fields.filter(pos => board.value[pos] > 0);
    let isEnd = await checkEnd();
    if (allowed_moves.length > 0 || isEnd) {
        return
    }
    score.value[turn.value] -= fields.length;
    for (let i = 0; i < fields.length; i++) {
        board.value[fields[i]] = 1;
    }
}

async function animateMove(pos, direction) {
    highlightColor.value = turn.value == "PLAYER" ? "blue" : "green";
    highlightedField.value = pos;
    const toDistribute = board.value[pos];
    board.value[pos] = 0;
    let index = pos;
    await delay(spedUp.value ? SPEDUP_DELAY : DELAY);

    for (let i = 1; i <= toDistribute; i++) {
        index = getNormalizedPos(pos + i * direction);
        board.value[index] += 1;
        await delay(spedUp.value ? SPEDUP_DELAY : DELAY);
    }

    highlightedField.value = null;
    index = getNormalizedPos(index + direction);
    if (board.value[index] == 0) {
        let next_index = getNormalizedPos(index + direction);
        while ((board.value[index] == 0) && (board.value[next_index] != 0)) {
            highlightColor.value = "red";
            highlightedField.value = index;
            await delay(spedUp.value ? SPEDUP_DELAY : DELAY);
            score.value[turn.value] += board.value[next_index];
            board.value[next_index] = 0;
            highlightedField.value = null;
            index = getNormalizedPos(next_index + direction);
            next_index = getNormalizedPos(index + direction);
        }
        switchTurn();
        await updateAllowedMoves();
    }
    else if (QUAN_FIELDS.includes(index)) {
        switchTurn();
        await updateAllowedMoves();
    } else {
        await animateMove(index, direction);
    }
    await delay(spedUp.value ? SPEDUP_DELAY : DELAY);
}


async function makeMove(pos, direction) {
    highlightedField.value = null;
    try {
        isTurn.value = false;
        turn.value = "PLAYER";
        const animated = animateMove(pos, direction);
        const response = await axios.post(BACKEND_URL + "/game/move/" + props.model, {
            game: store.getCurrentState().game,
            move: { pos, direction },
        });
        const data = response.data;
        store.addState(data);
        await animated;
        let next_move = data.last_move;
        if (next_move) {
            turn.value = "COMPUTER";
            await animateMove(next_move.pos, next_move.direction);
        }
        if (await checkEnd()) {
            isTurn.value = false;
            winner.value = data.winner;
            emit("gameEnded");
        }
        if (JSON.stringify(board.value) != JSON.stringify(store.getCurrentState().game.board)) {
            console.error("Board state mismatch:", board.value, store.getCurrentState().game.board);
        } else {
            isTurn.value = true;
        }
    } catch (error) {
        console.error("Error making move:", error);
    }
}

function toggleSpeed() {
    spedUp.value = !spedUp.value;
    try {
        localStorage.setItem("spedUp", spedUp.value);
    } catch (error) { }
}

function handleClickOutside(event) {
    if (event.target.closest('.exclude-click-outside')) {
        return;
    }
    if (!event.target.closest('.citizen')) {
        selectedCitizen.value = null;
    }
}

onBeforeMount(async () => {
    document.addEventListener('click', handleClickOutside);
});

onMounted(() => {
    try {
        spedUp.value = localStorage.getItem("spedUp") == "true";
    } catch (error) { }
});

onBeforeUnmount(() => {
    store.clearHistory();
    document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
    <div class="controls">
        <Button @click="undo()" :class="{ 'unclickable': !isTurn, 'grey': !isTurn }">
            <img src="../assets/undo.svg" />
        </Button>
        <Button @click="$router.go()">
            <img src="../assets/reload.png" />
        </Button>
        <Button color="orange" @click="$router.go(-1)">
            Back
        </Button>
        <Button v-if="spedUp" @click="toggleSpeed" class="green exclude-click-outside">
            <img src="../assets/pause.png" />
        </Button>
        <Button v-else @click="toggleSpeed" class="exclude-click-outside">
            <img src="../assets/fast_forward.png" />
        </Button>
        <Button @click="getHint()" :class="{ 'unclickable': !isTurn, 'exclude-click-outside': true, 'grey': !isTurn }">
            <img src="../assets/hint.svg" />
        </Button>
    </div>
    <span v-if="!isValidGame()">
        Loading...
    </span>
    <span v-else-if="winner == 'Draw'">
        It's a draw! 🤝
    </span>
    <span v-else-if="winner == 'PLAYER'">
        You win! 🎉
    </span>
    <span v-else-if="winner == 'COMPUTER'">
        You lose! 😢
    </span>
    <span v-else-if="turn == 'PLAYER'">
        Your turn!
    </span>
    <span v-else>
        Computer is playing...
    </span>
    <div v-if="isValidGame()" class="game">
        <span>🤖
            <Counter :count="score['COMPUTER']" id="comp_score" />
        </span>
        <div class="board">
            <Quan v-for="id in QUAN_FIELDS" :key="id" :id="id" :count="board[id]"
                :highlightedField="highlightedField" />
            <Citizen v-for="id in COMPUTER_FIELDS" :key="id" :id="id" :count="board[id]"
                :highlightedField="highlightedField" :color="highlightColor" />
            <Citizen v-for="id in PLAYER_FIELDS" :key="id" :id="id" :count="board[id]"
                :highlightedField="highlightedField" :color="highlightColor" :selectedCitizen="selectedCitizen"
                :direction="direction" :setSelectedCitizen="setSelectedCitizen" :makeMove="makeMove"
                :clickable="isTurn" />
        </div>
        <span>🫵
            <Counter :count="score['PLAYER']" id="you_score" />
        </span>
    </div>
    <Loading v-else />
</template>

<style>
.unclickable {
    pointer-events: none !important;
    cursor: default;
}
</style>

<style scoped>
.game {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.controls {
    margin-bottom: 1.5rem;
    display: grid;
    grid-template-columns: repeat(5, auto);
    align-items: center;
    gap: 0.75rem;
}

.controls>div {
    display: flex;
}


.board {
    display: grid;
    grid-template-columns: 1.25fr repeat(5, 1fr) 1.27fr;
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 0;
    grid-row-gap: 0;
    background-image: url('@/assets/board.svg');
    background-repeat: no-repeat;
    background-size: 100%;
    z-index: 1;
    width: 100%;
}

.board>* {
    font-size: 4cqw;
}

span {
    font-weight: 900;
    display: flex;
    flex-direction: row;
}

#field0 {
    grid-area: 1 / 1 / 3 / 2;
    border-radius: 100% 0 0 100% / 50% 0 0 50%;
    margin: 5% 0 5% 2%;
}

#field6 {
    grid-area: 1 / 7 / 3 / 8;
    border-radius: 0 100% 100% 0 / 0 50% 50% 0;
    margin: 5% 10% 5% 0;
}
</style>