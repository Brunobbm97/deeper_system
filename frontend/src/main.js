import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import ToastService from 'primevue/toastservice'
import Toast from 'primevue/toast'
import ConfirmDialog from 'primevue/confirmdialog'
import ConfirmationService from 'primevue/confirmationservice'
import InputSwitch from 'primevue/inputswitch'
import Tag from 'primevue/tag'
import router from './router'

import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'

const app = createApp(App)

app.use(PrimeVue)
app.use(ToastService)
app.use(ConfirmationService)
app.use(router)

app.component('Button', Button)
app.component('Dialog', Dialog)
app.component('InputText', InputText)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('Toast', Toast)
app.component('ConfirmDialog', ConfirmDialog)
app.component('InputSwitch', InputSwitch)
app.component('Tag', Tag)

app.mount('#app')
