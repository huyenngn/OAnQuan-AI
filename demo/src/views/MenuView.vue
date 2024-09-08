<script setup>
import Button from '@/components/Button.vue';
import { RouterLink } from 'vue-router';
</script>

<template>
    <nav>
        <RouterLink to="/game/easy">
            <Button color="green">EASY</Button>
        </RouterLink>
        <RouterLink to="/game/normal">
            <Button>NORMAL</Button>
        </RouterLink>
        <RouterLink to="/game/hard">
            <Button color="orange">HARD</Button>
        </RouterLink>
        <RouterLink to="/game/impossible">
            <Button color="red">IMPOSSIBLE</Button>
        </RouterLink>
    </nav>
    <p>
        Created by <a href="https://huyenngn.github.io/" target="_blank">Huyen Nguyen</a>
    </p>
    <p>
        Check out the code on <a href="https://github.com/huyenngn/OAnQuan-AI" target="_blank">GitHub</a>.
    </p>
</template>

<style scoped>
nav {
    display: flex;
    flex-direction: column;
}

p {
    font-size: 1rem;
}

a {
    font-weight: bold;
}
</style>
