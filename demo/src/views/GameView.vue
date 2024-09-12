<script setup>
import Button from '@/components/Button.vue';
import Game from '@/components/Game.vue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

let fast = ref(false);
</script>

<template>
    <div>
        <Button @click="$refs.game.start_game()">
            <img src="../assets/reload.png" />
        </Button>
        <RouterLink to="/">
            <Button color="orange">
                BACK
            </Button>
        </RouterLink>
        <Button v-if="fast" @click="fast = !fast" class="green">
            <img src="../assets/pause.png" class="green" />
        </Button>
        <Button v-else @click="fast = !fast">
            <img src="../assets/fast_forward.png" />
        </Button>
    </div>
    <Game :level="$route.params.level" :fast="fast" ref="game" />
</template>

<style scoped>
div {
    display: flex;
    flex-direction: row;
    align-items: center;
}

img {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #0066a2) drop-shadow(-0.5px -0.5px 0.5px #0066a2) drop-shadow(0.5px -0.5px 0.5px #0066a2) drop-shadow(-0.5px 0.5px 0.5px #0066a2) drop-shadow(2px 0 0.5px #0066a2) drop-shadow(0 3px 0.5px #004a87);
    width: 20px;
}

img.green {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #54d440) drop-shadow(-0.5px -0.5px 0.5px #54d440) drop-shadow(0.5px -0.5px 0.5px #54d440) drop-shadow(-0.5px 0.5px 0.5px #54d440) drop-shadow(2px 0 0.5px #54d440) drop-shadow(0 3px 0.5px #1d4c16);
}
</style>
