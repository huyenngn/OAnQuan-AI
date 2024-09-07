<script setup>
import GameInstance from '@/components/GameInstance.vue';
import { RouterLink } from 'vue-router';
</script>

<template>
    <RouterLink to="/">
        <div>BACK</div>
    </RouterLink>
    <GameInstance />
</template>
