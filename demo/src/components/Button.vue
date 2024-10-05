<script setup>
const props = defineProps(["color"]);
</script>

<template>
    <div :class="{
        'game-button': true,
        [color]: color
    }">
        <slot></slot>
    </div>
</template>

<style>
.game-button img {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #0066a2) drop-shadow(-0.5px -0.5px 0.5px #0066a2) drop-shadow(0.5px -0.5px 0.5px #0066a2) drop-shadow(-0.5px 0.5px 0.5px #0066a2) drop-shadow(2px 0 0.5px #0066a2) drop-shadow(0 3px 0.5px #004a87);
    width: 1.5rem;
}

.game-button.orange img {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #e78700) drop-shadow(-0.5px -0.5px 0.5px #e78700) drop-shadow(0.5px -0.5px 0.5px #e78700) drop-shadow(-0.5px 0.5px 0.5px #e78700) drop-shadow(2px 0 0.5px #e78700) drop-shadow(0 3px 0.5px #c96100);
}

.game-button.red img {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #d72d21) drop-shadow(-0.5px -0.5px 0.5px #d72d21) drop-shadow(0.5px -0.5px 0.5px #d72d21) drop-shadow(-0.5px 0.5px 0.5px #d72d21) drop-shadow(2px 0 0.5px #d72d21) drop-shadow(0 3px 0.5px #930704);
}


.game-button.green img {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #54d440) drop-shadow(-0.5px -0.5px 0.5px #54d440) drop-shadow(0.5px -0.5px 0.5px #54d440) drop-shadow(-0.5px 0.5px 0.5px #54d440) drop-shadow(2px 0 0.5px #54d440) drop-shadow(0 3px 0.5px #1d4c16);
}

.game-button.grey img {
    filter: invert(100%) drop-shadow(0.5px 0.5px 0.5px #b0b0b0) drop-shadow(-0.5px -0.5px 0.5px #b0b0b0) drop-shadow(0.5px -0.5px 0.5px #b0b0b0) drop-shadow(-0.5px 0.5px 0.5px #b0b0b0) drop-shadow(2px 0 0.5px #b0b0b0) drop-shadow(0 3px 0.5px #3b3b3b);
}
</style>

<style scoped>
/* https://codepen.io/Rybak/pen/xdzXNj */
.game-button {
    position: relative;
    top: 0;
    cursor: pointer;
    text-decoration: none !important;
    outline: none !important;
    font-family: 'Carter One', sans-serif;
    font-size: 1.5rem;
    line-height: 2rem;
    letter-spacing: .1rem;
    text-shadow: 2px 2px 1px #0066a2, -2px 2px 1px #0066a2, 2px -2px 1px #0066a2, -2px -2px 1px #0066a2, 0px 2px 1px #0066a2, 0px -2px 1px #0066a2, 0px 4px 1px #004a87, 2px 4px 1px #004a87, -2px 4px 1px #004a87;
    border: none;
    margin: 0 0.4rem 1.25rem;
    background: repeating-linear-gradient(45deg, #3ebbf7, #3ebbf7 5px, #45b1f4 5px, #45b1f4 10px);
    border-bottom: 3px solid rgba(16, 91, 146, 0.5);
    border-top: 3px solid rgba(255, 255, 255, .3);
    color: #fff !important;
    border-radius: 0.6rem;
    padding: 0.5rem 1.1rem 0.75rem;
    box-shadow: 0 6px 0 #266b91, 0 8px 1px 1px rgba(0, 0, 0, .3), 0 10px 0 5px #12517d, 0 12px 0 5px #1a6b9a, 0 15px 0 5px #0c405e, 0 15px 1px 6px rgba(0, 0, 0, .3);
}

.game-button:hover {
    top: .1rem;
    box-shadow: 0 4px 0 #266b91, 0 6px 1px 1px rgba(0, 0, 0, .3), 0 8px 0 5px #12517d, 0 10px 0 5px #1a6b9a, 0 13px 0 5px #0c405e, 0 13px 1px 6px rgba(0, 0, 0, .3);
}

.game-button::before {
    content: '';
    height: 10%;
    position: absolute;
    width: 40%;
    background: #fff;
    right: 13%;
    top: -3%;
    border-radius: 99px;
}

.game-button::after {
    content: '';
    height: 10%;
    position: absolute;
    width: 5%;
    background: #fff;
    right: 5%;
    top: -3%;
    border-radius: 99px;
}



.game-button.orange {
    background: repeating-linear-gradient(45deg, #ffc800, #ffc800 5px, #ffc200 5px, #ffc200 10px);
    box-shadow: 0 6px 0 #b76113, 0 8px 1px 1px rgba(0, 0, 0, .3), 0 10px 0 5px #75421f, 0 12px 0 5px #8a542b, 0 15px 0 5px #593116, 0 15px 1px 6px rgba(0, 0, 0, .3);
    border-bottom: 3px solid rgba(205, 102, 0, 0.5);
    text-shadow: 2px 2px 1px #e78700, -2px 2px 1px #e78700, 2px -2px 1px #e78700, -2px -2px 1px #e78700, 0px 2px 1px #e78700, 0px -2px 1px #e78700, 0px 4px 1px #c96100, 2px 4px 1px #c96100, -2px 4px 1px #c96100;
}

.game-button.orange:hover {
    top: .1rem;
    box-shadow: 0 4px 0 #b76113, 0 6px 1px 1px rgba(0, 0, 0, .3), 0 8px 0 5px #75421f, 0 10px 0 5px #8a542b, 0 13px 0 5px #593116, 0 13px 1px 6px rgba(0, 0, 0, .3);
}

.game-button.red {
    background: repeating-linear-gradient(45deg, #ff4f4c, #ff4f4c 5px, #ff4643 5px, #ff4643 10px);
    box-shadow: 0 6px 0 #ae2725, 0 8px 1px 1px rgba(0, 0, 0, .3), 0 10px 0 5px #831614, 0 12px 0 5px #a33634, 0 15px 0 5px #631716, 0 15px 1px 6px rgba(0, 0, 0, .3);
    border-bottom: 3px solid rgba(160, 25, 23, 0.5);
    text-shadow: 2px 2px 1px #d72d21, -2px 2px 1px #d72d21, 2px -2px 1px #d72d21, -2px -2px 1px #d72d21, 0px 2px 1px #d72d21, 0px -2px 1px #d72d21, 0px 4px 1px #930704, 2px 4px 1px #930704, -2px 4px 1px #930704;
}

.game-button.red:hover {
    top: .1rem;
    box-shadow: 0 4px 0 #ae2725, 0 6px 1px 1px rgba(0, 0, 0, .3), 0 8px 0 5px #831614, 0 10px 0 5px #a33634, 0 13px 0 5px #631716, 0 13px 1px 6px rgba(0, 0, 0, .3);
}

.game-button.green {
    background: repeating-linear-gradient(45deg, #54d440, #54d440 5px, #52cc3f 5px, #52cc3f 10px);
    box-shadow: 0 6px 0 #348628, 0 8px 1px 1px rgba(0, 0, 0, .3), 0 10px 0 5px #2a6d20, 0 12px 0 5px #39822e, 0 15px 0 5px #1d4c16, 0 15px 1px 6px rgba(0, 0, 0, .3);
    border-bottom: 3px solid rgba(40, 117, 29, 0.5);
    text-shadow: 2px 2px 1px #348628, -2px 2px 1px #348628, 2px -2px 1px #348628, -2px -2px 1px #348628, 0px 2px 1px #348628, 0px -2px 1px #348628, 0px 4px 1px #1d4c16, 2px 4px 1px #1d4c16, -2px 4px 1px #1d4c16;
}

.game-button.green:hover {
    top: .1rem;
    box-shadow: 0 4px 0 #348628, 0 6px 1px 1px rgba(0, 0, 0, .3), 0 8px 0 5px #2a6d20, 0 10px 0 5px #39822e, 0 13px 0 5px #1d4c16, 0 13px 1px 6px rgba(0, 0, 0, .3);
}



.game-button.grey {
    background: repeating-linear-gradient(45deg, #b0b0b0, #b0b0b0 5px, #a8a8a8 5px, #a8a8a8 10px);
    box-shadow: 0 6px 0 #7a7a7a, 0 8px 1px 1px rgba(0, 0, 0, .3), 0 10px 0 5px #4f4f4f, 0 12px 0 5px #6a6a6a, 0 15px 0 5px #3b3b3b, 0 15px 1px 6px rgba(0, 0, 0, .3);
    border-bottom: 3px solid rgba(80, 80, 80, 0.5);
    text-shadow: 2px 2px 1px #7a7a7a, -2px 2px 1px #7a7a7a, 2px -2px 1px #7a7a7a, -2px -2px 1px #7a7a7a, 0px 2px 1px #7a7a7a, 0px -2px 1px #7a7a7a, 0px 4px 1px #4f4f4f, 2px 4px 1px #4f4f4f, -2px 4px 1px #4f4f4f;
}

.game-button.grey:hover {
    top: .1rem;
    box-shadow: 0 4px 0 #7a7a7a, 0 6px 1px 1px rgba(0, 0, 0, .3), 0 8px 0 5px #4f4f4f, 0 10px 0 5px #6a6a6a, 0 13px 0 5px #3b3b3b, 0 13px 1px 6px rgba(0, 0, 0, .3);
}
</style>