# User Management CRUD App

This is a full-stack CRUD (Create, Read, Update, Delete) application built with:

- **Frontend:** Vue 3 + Vite + PrimeVue  
- **Backend:** Flask (Python) + MongoDB  
- **Purpose:** Simple, intuitive user management interface

## 📁 Project Structure

```
root/
├── backend/           # Flask API (Python)
│   ├── app.py
│   ├── config.py
│   ├── parser.py
│   ├── routes.py
│   └── models.py
├── frontend/          # Vue 3 + PrimeVue frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── router/
│   │   ├── App.vue
│   │   └── main.js
│   └── index.html
```

## 🚀 Features

### ✅ Home Page (`/`)

- Displays all users in a table
- Columns: `Username`, `Roles`, `Timezone`, `Is Active`, `Last Updated`, `Created At`
- Actions:
  - Create new user (via modal)
  - Edit user (via modal)
  - Delete user (with confirmation)
- Clicking on username navigates to user details page

### ✅ User Page (`/users/:id`)

- Shows individual user details
- Actions:
  - Edit user (via modal)
  - Delete user (with confirmation)

## 🧱 Tech Stack

### Frontend:

- [Vue 3](https://vuejs.org/)
- [Vite](https://vitejs.dev/)
- [PrimeVue](https://primevue.org/)
- [Axios](https://axios-http.com/)

### Backend:

- [Flask](https://flask.palletsprojects.com/)
- [PyMongo](https://pymongo.readthedocs.io/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

## ⚙️ Setup Instructions

### 📥 Clone the repository

```
git clone https://github.com/Brunobbm97/deeper_system.git 
cd deeper_system
```

### 🖥 Backend (Flask + MongoDB)

1. Navigate to `backend/`
2. Create a `.env` file:

```
DB_USERNAME=your_mongodb_user         # 👉 Replace with your actual MongoDB username
DB_PASSWORD=your_encoded_password     # 👉 Replace with your actual password (URL encoded if needed)
DB_NAME=your_database_name            # 👉 Replace with the name of your database
# ⚠️ Important: Use the real credentials you created on MongoDB Atlas — do not keep the placeholders like your_mongodb_user.
```

3. Install dependencies:

```bash
pip install flask pymongo python-dotenv flask-cors
```

4. Run the Flask server:

```bash
python app.py
```

> Server runs at: `http://localhost:5000`

### :globe_with_meridians: Frontend (Vue + PrimeVue)

1. Navigate to `frontend/`
2. Install dependencies:

```bash
npm install
```

3. Run the development server:

```bash
npm run dev
```

> Frontend runs at: `http://localhost:5173` (default Vite port)

## 📦 API Endpoints

| Method | Endpoint     | Description          |
| ------ | ------------ | -------------------- |
| GET    | `/users`     | List all users       |
| GET    | `/users/:id` | Get single user      |
| POST   | `/users`     | Create a new user    |
| PUT    | `/users/:id` | Update existing user |
| DELETE | `/users/:id` | Delete a user        |

## 🧪 Example User JSON (for import)

```json
{
  "users": [
    {
      "user": "john_doe_1",
      "password": "9X$mK2pL",
      "is_user_admin": false,
      "is_user_manager": true,
      "is_user_tester": false,
      "user_timezone": "America/New_York",
      "is_user_active": true,
      "created_at": "2023-09-15T08:30:45Z"
    }
  ]
}
```

> You can import this using `parser.py`
