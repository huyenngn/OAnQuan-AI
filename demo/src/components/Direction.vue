<script setup>
const emit = defineEmits(['left', 'right']);
</script>

<template>
    <div class="direction">
        <img class="clickable" src="@/assets/arrow_left.png" @click="emit('left')" />
        <img class="clickable" src="@/assets/arrow_right.png" @click="emit('right')" />
    </div>
</template>

<style scoped>
.direction {
    position: absolute;
    display: flex;
    justify-content: space-between;
    width: 130%;
    z-index: 10;
}

.clickable {
    width: 40%;
    cursor: pointer;
    pointer-events: all;
}
</style>