<script setup>
const props = defineProps(['display']);
const emit = defineEmits(['left', 'right']);
</script>

<template>
    <div class="direction">
        <img :class="!props.display || props.display == 1 ? 'clickable' : ''" src=" @/assets/arrow_left.png"
            @click="emit('left')" />
        <img :class="!props.display || props.display == -1 ? 'clickable' : ''" src="@/assets/arrow_right.png"
            @click="emit('right')" />
    </div>
</template>

<style scoped>
.direction {
    position: absolute;
    display: grid;
    grid-template-rows: 1fr;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    width: 140%;
    z-index: 20;
}

img {
    opacity: 0;
    width: 100%;
    justify-self: center;
}

.clickable {
    width: 100%;
    cursor: pointer;
    pointer-events: all;
    opacity: 1 !important;
}
</style>