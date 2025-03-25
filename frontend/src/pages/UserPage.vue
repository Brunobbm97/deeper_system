<template>
    <div class="p-4">
        <div class="flex justify-between items-center mb-4 flex-wrap gap-4 ">
            <h1 class="text-2xl font-bold m-0">User Detail</h1>
            <div class="flex gap-2">
                <Button label="Editar" icon="pi pi-pencil" class="mr-2" @click="editUser" />
                <Button label="Deletar" icon="pi pi-trash" class="p-button-danger" @click="confirmDelete" />
            </div>
        </div>

        <div v-if="user" class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div><strong>Username:</strong> {{ user.username }}</div>
            <div><strong>Roles:</strong> {{ user.roles.join(', ') }}</div>
            <div><strong>Timezone:</strong> {{ user.preferences?.timezone }}</div>
            <div><strong>Ativo:</strong> {{ user.active ? 'Yes' : 'No' }}</div>
            <div><strong>Created At:</strong> {{ formatDate(user.created_ts) }}</div>
            <div><strong>Last Updated:</strong> {{ formatDate(user.updated_ts || user.created_ts) }}</div>
        </div>

        <UserDialog v-model:visible="dialogVisible" :user="user" @saved="fetchUser" />
        <ConfirmDialog />
        <Toast />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useConfirm } from 'primevue/useconfirm'
import { useToast } from 'primevue/usetoast'
import UserDialog from '../components/UserDialog.vue'

const route = useRoute()
const router = useRouter()
const confirm = useConfirm()
const toast = useToast()

const API = 'http://localhost:5000/users'
const user = ref(null)
const dialogVisible = ref(false)

const fetchUser = async () => {
    try {
        const res = await axios.get(`${API}/${route.params.id}`)
        user.value = res.data
    } catch {
        toast.add({ severity: 'error', summary: 'Erro', detail: 'User not Found', life: 3000 })
        router.push('/')
    }
}

const editUser = () => {
    dialogVisible.value = true
}

const confirmDelete = () => {
    confirm.require({
        message: 'Do you want to delete this user?',
        header: 'Confirmation',
        icon: 'pi pi-exclamation-triangle',
        accept: async () => {
            await axios.delete(`${API}/${user.value._id}`)
            toast.add({ severity: 'success', summary: 'Deleted', detail: 'User deleted successfully', life: 3000 })
            router.push('/')
        }
    })
}

const formatDate = (ts) => {
    return new Date(ts * 1000).toLocaleString()
}

onMounted(fetchUser)
</script>