import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import UserPage from '../pages/UserPage.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/users/:id',
        name: 'UserPage',
        component: UserPage
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
