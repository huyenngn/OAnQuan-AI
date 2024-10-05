<script setup>
import Button from '@/components/Button.vue';
import { RouterLink } from 'vue-router';
</script>

<template>
    <nav>
        <RouterLink to="/game/ab_v1">
            <Button color="blue">
                AlphaBeta v1
            </Button>
        </RouterLink>
        <RouterLink to="/game/ab_v2">
            <Button color="orange">
                AlphaBeta v2
            </Button>
        </RouterLink>
        <RouterLink to="/game/rl">
            <Button color="green">
                RL model
            </Button>
        </RouterLink>
        <RouterLink to="/tutorial">
            <Button color="red">
                Tutorial
            </Button>
        </RouterLink>
    </nav>
    <p>
        Created by <a href="https://huyenngn.github.io/" target="_blank">Huyen Nguyen</a>
    </p>
</template>

<style scoped>
nav {
    display: flex;
    flex-direction: column;
    gap: 0.75em;
    margin: 0.75em 0;
}

p {
    font-size: 1rem;
    font-weight: normal;
    margin-top: 0.25rem;
}
</style>
