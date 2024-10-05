import ClassicGameView from "@/views/ClassicGameView.vue";
import MenuView from "@/views/MenuView.vue";
import TutorialView from "@/views/TutorialView.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "menu",
            component: MenuView,
        },
        {
            path: "/game/:model",
            name: "game",
            component: ClassicGameView,
            props: true,
        },
        {
            path: "/tutorial",
            name: "tutorial",
            component: TutorialView,
        },
    ],
});

export default router;
