<template>
    <div class="pl">
        <div class="pl__coin">
            <div class="pl__coin-flare"></div>
            <div class="pl__coin-flare"></div>
            <div class="pl__coin-flare"></div>
            <div class="pl__coin-flare"></div>
            <div class="pl__coin-layers">
                <div class="pl__coin-layer">
                    <div class="pl__coin-inscription"></div>
                </div>
                <div class="pl__coin-layer"></div>
                <div class="pl__coin-layer"></div>
                <div class="pl__coin-layer"></div>
                <div class="pl__coin-layer">
                    <div class="pl__coin-inscription"></div>
                </div>
            </div>
        </div>
        <div class="pl__shadow"></div>
    </div>
</template>

<style scoped>
/* https://codepen.io/jkantner/pen/gONXWLe */
.pl {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 9.1em;
    height: 9.1em;
}

.pl__coin,
.pl__coin-flare,
.pl__coin-inscription,
.pl__coin-layers,
.pl__shadow {
    animation-duration: 2s;
    animation-timing-function: cubic-bezier(0.37, 0, 0.63, 1);
    animation-iteration-count: infinite;
}

.pl__coin {
    animation-name: bounce;
    position: relative;
    transform: translateY(0.5em);
    z-index: 1;
}

.pl__coin-flare,
.pl__coin-inscription,
.pl__coin-layer {
    position: absolute;
}

.pl__coin-flare {
    animation-name: flare1;
    background-color: #fff;
    clip-path: polygon(50% 0, 67% 33%, 100% 50%, 67% 67%, 50% 100%, 33% 67%, 0 50%, 33% 33%);
    top: 0;
    left: -0.5em;
    width: 1em;
    height: 1em;
    transform: scale(0);
    z-index: 1;
}

.pl__coin-flare:nth-child(2) {
    animation-name: flare2;
    top: -0.5em;
    left: 0;
}

.pl__coin-flare:nth-child(3) {
    animation-name: flare3;
    left: 3em;
}

.pl__coin-flare:nth-child(4) {
    animation-name: flare4;
    top: -0.5em;
    left: 3.5em;
}

.pl__coin-inscription {
    animation-name: inscription-front;
    background-color: #da950b;
    box-shadow: 0.1875em 0 0 #c2850a inset;
    top: 50%;
    left: 50%;
    width: 0.5em;
    height: 2.5em;
    transform: translate(-50%, -50%) rotateZ(30deg);
}

.pl__coin-layer {
    background-color: #f2aa0d;
    backface-visibility: hidden;
    border-radius: 50%;
    box-shadow: 0 0 0 0.375em #f7ce6e inset;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.pl__coin-layer:first-child {
    transform: translate3d(0, 0, 0.5em);
}

.pl__coin-layer:nth-child(2) {
    transform: translate3d(0, 0, 0.49em) rotateY(180deg);
}

.pl__coin-layer:nth-child(3) {
    backface-visibility: visible;
    border-radius: 0;
    left: 50%;
    width: 0.98em;
    transform: translateX(-50%) rotateY(90deg);
}

.pl__coin-layer:nth-child(4) {
    transform: translate3d(0, 0, -0.49em);
}

.pl__coin-layer:last-child {
    transform: translate3d(0, 0, -0.5em) rotateY(180deg);
}

.pl__coin-layer:nth-child(n + 2):nth-last-child(n + 2) {
    background-color: #c28b0a;
    box-shadow: none;
}

.pl__coin-layer:last-child .pl__coin-inscription {
    animation-name: inscription-back;
    transform: translate(-50%, -50%) rotateZ(-30deg);
}

.pl__coin-layers {
    animation-name: roll;
    position: relative;
    width: 4em;
    height: 4em;
    transform: rotateY(-15deg) rotateZ(-30deg);
    transform-style: preserve-3d;
}

.pl__shadow {
    animation-name: shadow;
    background-color: rgba(48, 3, 3, 0.3);
    border-radius: 50%;
    width: 4em;
    height: 0.5em;
}

/* Animations */
@keyframes bounce {

    from,
    50%,
    to {
        animation-timing-function: cubic-bezier(0.33, 0, 0.67, 0);
        transform: translateY(0.5em);
    }

    25%,
    75% {
        animation-timing-function: cubic-bezier(0.33, 1, 0.67, 1);
        transform: translateY(5.1em);
    }
}

@keyframes flare1 {

    from,
    75%,
    to {
        animation-timing-function: cubic-bezier(0.33, 0, 0.67, 0);
        transform: scale(0);
    }

    87.5% {
        animation-timing-function: cubic-bezier(0.33, 1, 0.67, 1);
        transform: scale(1);
    }
}

@keyframes flare2 {

    from,
    to {
        animation-timing-function: cubic-bezier(0.33, 1, 0.67, 1);
        transform: scale(1);
    }

    12.5%,
    87.5% {
        animation-timing-function: cubic-bezier(0.33, 0, 0.67, 0);
        transform: scale(0);
    }
}

@keyframes flare3 {

    from,
    25%,
    50%,
    to {
        animation-timing-function: cubic-bezier(0.33, 0, 0.67, 0);
        transform: scale(0);
    }

    37.5% {
        animation-timing-function: cubic-bezier(0.33, 1, 0.67, 1);
        transform: scale(1);
    }
}

@keyframes flare4 {

    from,
    37.5%,
    62.5%,
    to {
        animation-timing-function: cubic-bezier(0.33, 0, 0.67, 0);
        transform: scale(0);
    }

    50% {
        animation-timing-function: cubic-bezier(0.33, 1, 0.67, 1);
        transform: scale(1);
    }
}

@keyframes inscription-front {

    from,
    75% {
        animation-timing-function: cubic-bezier(0.12, 0, 0.39, 0);
        box-shadow: 0.1875em 0 0 #b77f07 inset;
    }

    87.49% {
        animation-timing-function: steps(1);
        box-shadow: 0.875em -0.75em 0 #b77f07 inset;
    }

    87.5% {
        animation-timing-function: cubic-bezier(0.61, 1, 0.88, 1);
        box-shadow: -0.875em 0.75em 0 #b77f07 inset;
    }

    to {
        box-shadow: 0.1875em 0 #b77f07 inset;
    }
}

@keyframes inscription-back {

    from,
    75% {
        box-shadow: -1em -0.875em 0 #c2910a inset;
    }

    to {
        box-shadow: 1.125em 1em 0 #c2910a inset;
    }
}

@keyframes roll {

    from,
    75% {
        transform: rotateY(-15deg) rotateZ(-30deg) rotateY(0);
    }

    to {
        transform: rotateY(-15deg) rotateZ(-30deg) rotateY(-1turn);
    }
}

@keyframes shadow {

    from,
    50%,
    to {
        animation-timing-function: cubic-bezier(0.33, 0, 0.67, 0);
        background-color: rgba(48, 3, 3, 0.3);
        transform: scale(0.6);
    }

    25%,
    75% {
        animation-timing-function: cubic-bezier(0.33, 1, 0.67, 1);
        background-color: rgba(48, 3, 3, 0.5);
        transform: scale(1);
    }
}
</style>