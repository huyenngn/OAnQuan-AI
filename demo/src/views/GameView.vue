<script setup>
import Button from '@/components/Button.vue';
import Game from '@/components/Game.vue';
import { RouterLink } from 'vue-router';

const props = defineProps(["level"]);
</script>

<template>
    <RouterLink to="/">
        <Button color="orange">
            BACK
        </Button>
    </RouterLink>
    <Game :level="level" />
</template>
