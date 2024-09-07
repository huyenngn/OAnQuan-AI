import { createRouter, createWebHistory } from "vue-router";
import CreditsView from "../views/CreditsView.vue";
import EasyView from "../views/EasyView.vue";
import ImpossibleView from "../views/ImpossibleView.vue";
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
            path: "/easy",
            name: "easy",
            component: EasyView,
        },
        {
            path: "/impossible",
            name: "impossible",
            component: ImpossibleView,
        },
        {
            path: "/credits",
            name: "credits",
            component: CreditsView,
        },
    ],
});

export default router;
