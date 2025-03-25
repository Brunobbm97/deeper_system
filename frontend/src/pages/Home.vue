<template>
    <div class="p-4">
        <div class="flex justify-between items-center mb-4">
            <h1 class="text-2xl font-bold mr-4">Users</h1>
            <Button label="Novo Usuário" icon="pi pi-plus" @click="openCreateDialog" />
        </div>

        <DataTable :value="users" dataKey="_id" responsiveLayout="scroll">
            <Column field="username" header="Username">
                <template #body="slotProps">
                    <router-link :to="`/users/${slotProps.data._id}`" class="text-blue-500 hover:underline">
                        {{ slotProps.data.username }}
                    </router-link>
                </template>
            </Column>

            <Column field="roles" header="Roles">
                <template #body="slotProps">
                    <Tag v-for="role in slotProps.data.roles" :key="role" :value="role" class="mr-1" />
                </template>
            </Column>

            <Column field="preferences.timezone" header="Timezone" />
            <Column header="Is Active?">
                <template #body="slotProps">
                    <i
                        :class="['pi', slotProps.data.active ? 'pi-check-circle text-green-500' : 'pi-times-circle text-red-500']"></i>
                </template>
            </Column>

            <Column header="Last Updated At">
                <template #body="slotProps">
                    {{ formatDate(slotProps.data.updated_ts || slotProps.data.created_ts) }}
                </template>
            </Column>

            <Column field="created_ts" header="Created At">
                <template #body="slotProps">
                    {{ formatDate(slotProps.data.created_ts) }}
                </template>
            </Column>

            <Column header="Actions">
                <template #body="slotProps">
                    <Button icon="pi pi-pencil" class="p-button-text" @click="editUser(slotProps.data)" />
                    <Button icon="pi pi-trash" class="p-button-text text-red-600"
                        @click="confirmDelete(slotProps.data)" />
                </template>
            </Column>
        </DataTable>

        <UserDialog v-model:visible="dialogVisible" :user="selectedUser" @saved="fetchUsers" />
        <ConfirmDialog />
        <Toast />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import UserDialog from '../components/UserDialog.vue'
import { useConfirm } from 'primevue/useconfirm'
import { useToast } from 'primevue/usetoast'

const users = ref([])
const dialogVisible = ref(false)
const selectedUser = ref(null)
const confirm = useConfirm()
const toast = useToast()

const API = 'http://localhost:5000/users'

const fetchUsers = async () => {
    const res = await axios.get(API)
    users.value = res.data
}

const openCreateDialog = () => {
    selectedUser.value = null
    dialogVisible.value = true
}

const editUser = (user) => {
    selectedUser.value = { ...user }
    dialogVisible.value = true
}

const confirmDelete = (user) => {
    confirm.require({
        message: `Do you want to delete the user? ${user.username}?`,
        header: 'Confirmation',
        icon: 'pi pi-exclamation-triangle',
        accept: async () => {
            await axios.delete(`${API}/${user._id}`)
            toast.add({ severity: 'success', summary: 'Deleted', detail: 'User deleted successfully', life: 3000 })
            fetchUsers()
        }
    })
}

const formatDate = (ts) => {
    return new Date(ts * 1000).toLocaleString()
}

onMounted(fetchUsers)
</script>