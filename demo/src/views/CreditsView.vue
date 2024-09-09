<script setup>
import Button from '@/components/Button.vue';
import { RouterLink } from 'vue-router';

</script>

<template>
    <RouterLink to="/">
        <Button color="orange">
            BACK
        </Button>
    </RouterLink>
    <p>
        Created by <a href="https://huyenngn.github.io/" target="_blank">Huyen Nguyen</a>
    </p>
    <p>
        Check out <a href="https://github.com/huyenngn/OAnQuan-AI" target="_blank">the code on GitHub</a>.
    </p>
</template>
