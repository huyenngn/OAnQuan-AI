import { createRouter, createWebHistory } from "vue-router";
import CreditsView from "../views/CreditsView.vue";
import GameView from "../views/GameView.vue";
import MenuView from "../views/MenuView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "menu",
            component: MenuView,
        },
        {
            path: "/game/:level",
            name: "game",
            component: GameView,
        },
        {
            path: "/credits",
            name: "credits",
            component: CreditsView,
        },
    ],
});

export default router;
