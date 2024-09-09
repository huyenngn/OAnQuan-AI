<script setup>
import Button from '@/components/Button.vue';
import { RouterLink } from 'vue-router';
</script>

<template>
    <nav>
        <RouterLink to="/game/easy">
            <Button>EASY</Button>
        </RouterLink>
        <RouterLink to="/game/hard">
            <Button color="orange">HARD</Button>
        </RouterLink>
        <RouterLink to="/game/impossible">
            <Button color="green">IMPOSSIBLE</Button>
        </RouterLink>
        <RouterLink to="/credits">
            <Button color="red">CREDITS</Button>
        </RouterLink>
    </nav>
</template>

<style scoped>
nav {
    display: flex;
    flex-direction: column;
}
</style>
