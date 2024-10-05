<script setup>
import Counter from "@/components/Counter.vue";
import Direction from "@/components/Direction.vue";

const props = defineProps({
    id: Number,
    count: Number,
    highlightedField: Number,
    color: String,
    selectedCitizen: [Number, null],
    direction: {
        type: [Number, null],
        default: null,
    },
    setSelectedCitizen: {
        type: [Function, null],
        default: null
    },
    makeMove: {
        type: [Function, null],
        default: null
    },
    clickable: {
        type: Boolean,
        default: false
    }
});
</script>

<template>
    <div :id="'field' + id" @click="setSelectedCitizen(id)" :class="{
        'citizen': true,
        [color]: highlightedField == id,
        'unclickable': !clickable || count == 0
    }">
        <Counter :count="count" :id="'counter' + id" />
        <Direction v-if="selectedCitizen == id" :display="direction" @left="makeMove(id, 1)"
            @right="makeMove(id, -1)" />
    </div>
</template>

<style scoped>
.citizen {
    grid-row: span 1;
    display: flex;
    justify-content: center;
    align-items: center;
    aspect-ratio: 0.93;
    pointer-events: none;
    position: relative;
    z-index: 10;
    cursor: pointer;
    pointer-events: all;
}

.red {
    background-color: #ff9595;
    mix-blend-mode: multiply;
}

.blue {
    background-color: #aadefd;
    mix-blend-mode: multiply;
}

.green {
    background-color: #8ae994;
    mix-blend-mode: multiply;
}
</style>