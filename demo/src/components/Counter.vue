<script setup>
import { ref, watch } from 'vue';

const props = defineProps(['count', 'id']);

let diff = ref(0);

watch(() => props.count, (newVal, oldVal) => {
    const element = document.getElementById(props.id);
    const diff_element = element.previousElementSibling
    if (element) {
        diff.value = newVal - oldVal;
        diff_element.classList.add('fadeIn');
        element.classList.add('waviy');
        setTimeout(() => {
            element.classList.remove('waviy');
            diff_element.classList.remove('fadeIn');
        }, 1000);
    }
});
</script>

<template>
    <div>
        <div class="diff"> {{ diff > 0 ? '+' + diff : diff }} </div>
        <span :id="props.id">
            {{ props.count }}
        </span>
    </div>
</template>

<style scoped>
/* https://codepen.io/alvarotrigo/pen/xxLvyOG */
div {
    position: relative;
}

span {
    position: relative;
    display: inline-block;
    text-transform: uppercase;
    font-weight: 900;
}

.diff {
    position: absolute;
    top: -1em;
    right: -1em;
    color: red;
    opacity: 0%;
    font-size: 0.75em;
}

.fadeIn {
    animation: fadeIn 1s;
}

@keyframes fadeIn {

    0%,
    100% {
        opacity: 0;
    }

    50% {
        opacity: 1;
    }
}

.waviy {
    animation: waviy 1s;
}

@keyframes waviy {

    0%,
    40%,
    100% {
        transform: translateY(0)
    }

    20% {
        transform: translateY(-20%)
    }
}
</style>