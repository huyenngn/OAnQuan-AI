<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <nav>
        <RouterLink to="/easy">
            <div>EASY</div>
        </RouterLink>
        <RouterLink to="/impossible">
            <div>IMPOSSIBLE</div>
        </RouterLink>
        <RouterLink to="/credits">
            <div>CREDITS</div>
        </RouterLink>
    </nav>
</template>

<style scoped>
nav {
    display: flex;
    flex-direction: column;
}

div {
    padding: 10px;
    margin: 10px;
    background-color: lightblue;
    text-align: center;
    cursor: pointer;
}
</style>
