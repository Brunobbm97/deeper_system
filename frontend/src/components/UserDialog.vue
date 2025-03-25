<template>
    <Dialog :visible="visible" modal header="User" :style="{ width: '30rem' }"
        @update:visible="$emit('update:visible', $event)">
        <div class="p-fluid">
            <div class="field">
                <label for="username">Username</label>
                <InputText id="username" v-model="form.username" required autofocus />
            </div>

            <div class="field">
                <label for="password" class="mr-2">Password</label>
                <span class="p-input-icon-right w-full">
                    <i :class="passwordVisible ? 'pi pi-eye-slash' : 'pi pi-eye'" @click="togglePassword"
                        class="cursor-pointer" />
                    <InputText id="password" v-model="form.password" :type="passwordVisible ? 'text' : 'password'"
                        required class="w-full" />
                </span>
            </div>

            <div class="field">
                <label for="roles">Roles</label>
                <div class="flex gap-2">
                    <div v-for="role in allRoles" :key="role">
                        <label class="mr-2">
                            <input type="checkbox" v-model="form.roles" :value="role" /> {{ role }}
                        </label>
                    </div>
                </div>
            </div>

            <div class="field">
                <label for="timezone">Timezone</label>
                <InputText id="timezone" v-model="form.preferences.timezone" />
            </div>

            <div class="field">
                <label for="active">Active</label>
                <InputSwitch id="active" v-model="form.active" />
            </div>

            <div class="flex justify-end mt-4">
                <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="close" />
                <Button label="Save" icon="pi pi-check" class="ml-2" @click="save" />
            </div>
        </div>

        <ConfirmDialog />
    </Dialog>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'
import { useToast } from 'primevue/usetoast'

const props = defineProps({
    visible: Boolean,
    user: Object
})
const emit = defineEmits(['update:visible', 'saved'])

const toast = useToast()
const API = 'http://localhost:5000/users'
const allRoles = ['admin', 'manager', 'tester']

const defaultForm = () => ({
    username: '',
    password: '',
    roles: [],
    preferences: { timezone: '' },
    active: true
})

const form = ref(defaultForm())

watch(() => props.user, (newUser) => {
    form.value = newUser
        ? { ...newUser, preferences: { ...newUser.preferences } }
        : defaultForm()
}, { immediate: true })

import { useConfirm } from 'primevue/useconfirm'

const confirm = useConfirm()

const save = async () => {
    try {
        if (props.user && props.user._id) {
            confirm.require({
                message: `Do you want to update the user "${form.value.username}"?`,
                header: 'Confirm Update',
                icon: 'pi pi-exclamation-triangle',
                accept: async () => {
                    await axios.put(`${API}/${props.user._id}`, form.value)
                    toast.add({ severity: 'success', summary: 'Updated', detail: 'User successfully updated', life: 3000 })
                    emit('update:visible', false)
                    emit('saved')
                }
            })
        } else {
            await axios.post(API, form.value)
            toast.add({ severity: 'success', summary: 'Created', detail: 'User created successfully', life: 3000 })
        }
        emit('update:visible', false)
        emit('saved')
    } catch (err) {
        toast.add({ severity: 'error', summary: 'Erro', detail: 'Unable to save user', life: 3000 })
    }
}

const close = () => {
    emit('update:visible', false)
}

const passwordVisible = ref(false)
const togglePassword = () => {
    passwordVisible.value = !passwordVisible.value
}
</script>