<script setup>
import Counter from "@/components/Counter.vue";

const props = defineProps(['id', 'count', 'setSelectedCitizen']);

</script>


<template>
    <div class="citizen" :id="'field' + id" @click="setSelectedCitizen(id)">
        <Counter :count="count" :id="'counter' + id" />
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
</style>