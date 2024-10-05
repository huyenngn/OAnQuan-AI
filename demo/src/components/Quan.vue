<script setup>
import Counter from "@/components/Counter.vue";

const props = defineProps(['id', 'count', 'highlightedField']);

</script>

<template>
    <div :class="'quan' + (highlightedField == id ? 'background-color: #ff9595' : '')" :id="'field' + id">
        <Counter :count="count" :id="'counter' + id" />
    </div>
</template>

<style scoped>
.quan {
    display: flex;
    justify-content: center;
    align-items: center;
}

.red {
    background-color: #ff9595;
    mix-blend-mode: multiply;
}
</style>