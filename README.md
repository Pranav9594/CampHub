# CampHub

A clean and responsive **college file storage web application** built with **Flask, SQLite, HTML, CSS, and JavaScript**.

College Storage allows students to upload, organize, search, download, and manage academic files from a simple dashboard.

## ✨ Features

* 📁 Upload academic files
* 📄 Supports **PDF, DOCX, PPT, PPTX, and image files**
* 🎓 Organize files by:

  * Semester
  * Subject
  * Category
* 🔍 Search files by name
* ⬇️ Download files
* 🗑️ Delete files
* 📊 Responsive dashboard with file metadata
* 💾 SQLite database for file information
* 📱 Responsive design for desktop and mobile

## 🛠️ Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Backend programming           |
| Flask      | Web framework                 |
| SQLite     | Database                      |
| HTML       | Page structure                |
| CSS        | Styling and responsive design |
| JavaScript | Frontend interactions         |

## 📂 Project Structure

```text
college-storage/
│
├── app.py
├── requirements.txt
├── college_storage.db
├── uploads/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
└── templates/
    ├── base.html
    └── index.html
```

> `college_storage.db` and the `uploads/` folder are created automatically when the application starts.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/college-storage.git
cd college-storage
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```text
http://127.0.0.1:5000
```

## 💾 File Storage

Uploaded files are stored inside:

```text
uploads/
```

File information such as the filename, semester, subject, category, and upload details is stored in the SQLite database.

## 🗄️ Database

The application automatically creates:

```text
college_storage.db
```

with a `files` table when the application starts.

To completely reset the application, you can delete the database file and restart the server.

## 🔮 Future Improvements

* User authentication
* Student-specific storage
* Admin dashboard
* File preview
* Cloud storage integration
* File sharing
* Storage usage tracking
* Drag-and-drop uploads
* Advanced filtering and sorting

## 📌 Project Status

**Currently in development.**

College Storage is designed as a simple academic file management system for students to keep their study materials organized in one place.

## 👨‍💻 Author

**Your Name**

Built as a college project using Flask and SQLite.
