<script setup>
import Counter from "@/components/Counter.vue";
import Direction from "@/components/Direction.vue";

const props = defineProps(['id', 'count', 'selectedCitizen', 'makeMove', 'setSelectedCitizen']);

</script>


<template>
    <div class="citizen clickable" :id="'field' + id" @click="setSelectedCitizen(id)">
        <Counter :count="count" :id="'counter' + id" />
        <Direction v-if="selectedCitizen === id && count !== 0" @left="makeMove(id, 1)" @right="makeMove(id, -1)" />
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
}

.clickable {
    cursor: pointer;
    pointer-events: all;
}
</style>