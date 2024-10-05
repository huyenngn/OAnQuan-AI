<script setup>
import Button from '@/components/Button.vue';

const tutorial = [
    {
        title: "The Ô Ăn Quan board",
        text: "The Ô Ăn Quan board consists of 10 'dân' fields, 5 on each side, and 2 larger 'quan' fields at both ends. Understanding the layout helps you plan your moves effectively.",
    },
    {
        title: "Move your seeds",
        text: "On your turn, pick up all the seeds from one of your 'dân' fields and distribute them in either direction, one by one. Once you've placed all the seeds, you pick up the seeds from the next field and distribute them in the same way. This continues until you capture or reach a 'quan' field.",
        image: "src/assets/tutorial_imgs/move.gif",
    },
    {
        title: "Capture seeds",
        text: "If the last seed you place lands in front of an empty field, you capture all the seeds in the opposite field. If the opposite field is also empty, you lose your turn. Capturing seeds key to winning.",
        image: "src/assets/tutorial_imgs/capture.gif",
    },
    {
        title: "Chain capture",
        text: "If you capture seeds and the next field is empty, you can continue capturing seeds from the next field. Plan ahead and set up chain captures to gain an advantage.",
        image: "src/assets/tutorial_imgs/chain.gif",
    },
    {
        title: "Stay defensive",
        text: "Avoid leaving a full field directly behind an empty one to prevent your opponent from capturing a lot of seeds in one turn.",
    },
    {
        title: "Plan ahead",
        text: "Try to avoid leaving your seeds in a position where your opponent can easily capture them. Instead, aim to capture your opponent's seeds and the 'quan' fields to gain an advantage. The player with the most seeds at the end of the game wins.",
    },
    {
        title: "Control the Quan",
        text: "Capturing seeds in the 'quan' fields can give you a big advantage. But be careful, if all the quan fields get captured, while you're behind, you lose the game.",
    },
    {
        title: "Win the game",
        text: "The game ends when all the 'quan' fields are empty. Seeds that remain on either side of the board go to the respective player. The player with the most seeds wins the game.",
    },
];
</script>

<template>
    <Button color="orange" @click="$router.push('/')">
        Back
    </Button>
    <div v-for="step in tutorial">
        <h1>{{ step.title }}</h1>
        <p>
            {{ step.text }}
        </p>
        <img v-if="step.image" :src="step.image" />
    </div>
</template>

<style scoped>
div {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 800px;
    margin-top: 2rem;
}

h1 {
    font-size: 1.75rem;
    font-weight: bold;
    display: flex;
}

p {
    font-size: 1.25rem;
    font-weight: normal;
}
</style>