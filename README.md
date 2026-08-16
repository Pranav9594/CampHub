# College Storage

A clean, responsive **college file storage web application** built with **Flask, Supabase, HTML, CSS, and JavaScript**.

College Storage provides students with a simple platform to upload, organize, search, download, and manage their academic files in one place.

## ✨ Features

* 📁 Upload academic files
* 📄 Supports:

  * PDF
  * DOCX
  * PPT
  * PPTX
  * Images
* 🎓 Organize files by:

  * Semester
  * Subject
  * Category
* 🔍 Search files by name
* ⬇️ Download files
* 🗑️ Delete files
* 📊 Responsive dashboard with file metadata
* ☁️ Supabase integration for cloud-based data and file storage
* 📱 Responsive interface for desktop and mobile
* ⚡ Flask backend for handling application logic

## 🛠️ Tech Stack

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Backend programming            |
| Flask      | Web framework and API handling |
| Supabase   | Cloud database and storage     |
| PostgreSQL | Database used by Supabase      |
| HTML       | Page structure                 |
| CSS        | Styling and responsive design  |
| JavaScript | Frontend interactions          |

## 🏗️ Architecture

```text
                    College Storage
                           │
                           ▼
                    ┌─────────────┐
                    │   Frontend  │
                    │ HTML / CSS  │
                    │ JavaScript  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Flask    │
                    │   Backend   │
                    └──────┬──────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
           ┌─────────────┐   ┌─────────────┐
           │  Supabase   │   │  Supabase   │
           │  Database   │   │   Storage   │
           │ PostgreSQL  │   │    Files    │
           └─────────────┘   └─────────────┘
```

## 📂 Project Structure

```text
college-storage/
│
├── app.py
├── requirements.txt
│
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

> The exact project structure may vary depending on your Supabase configuration and deployment setup.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/college-storage.git
cd college-storage
```

### 2. Create a Virtual Environment

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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase

Create a project on Supabase and configure the required database and storage bucket.

Add your Supabase credentials to your environment variables.

Example:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

> Never commit your Supabase keys or `.env` file to GitHub.

Add `.env` to `.gitignore`:

```text
.env
venv/
__pycache__/
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Your Browser

```text
http://127.0.0.1:5000
```

## ☁️ Supabase Integration

Supabase is used to provide cloud-based storage and database functionality.

### Database

File metadata can be stored in a Supabase PostgreSQL database, including information such as:

* File name
* File path
* Semester
* Subject
* Category
* Upload date

### Storage

Uploaded academic files can be stored in a Supabase Storage bucket.

This allows files to be managed independently from the Flask application's local filesystem.

## 🔍 File Management

Users can:

1. Upload files
2. Select semester, subject, and category
3. Search uploaded files
4. View file information
5. Download files
6. Delete files

## 📊 Dashboard

The dashboard provides a simple overview of stored academic materials using responsive cards and file metadata.

The interface is designed to make it easy for students to quickly find and manage their study materials.

## 🔐 Security

The application should keep sensitive configuration values outside the source code.

Example:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

Do not upload `.env` files or private API keys to GitHub.

For production, configure appropriate **Supabase Row Level Security (RLS)** and Storage policies.

## 🔮 Future Improvements

* 🔐 User authentication
* 👤 Student-specific file storage
* 👨‍💼 Admin dashboard
* 👁️ File preview
* 🔗 File sharing
* 📤 Drag-and-drop uploads
* 🔎 Advanced search and filtering
* 📈 Storage usage tracking
* 🏷️ File tagging
* ☁️ Improved cloud storage management
* 📱 Progressive Web App support

## 📌 Project Status

**🚧 Currently in development**

College Storage is designed as an academic file management platform that helps students keep notes, presentations, documents, and other study materials organized in one place.

## 🎯 Purpose

The goal of College Storage is to provide a simple and centralized solution for managing college-related files instead of keeping academic documents scattered across different folders and devices.

## 👨‍💻 Author

**Your Name**

Built with ❤️ using **Flask, Supabase, PostgreSQL, HTML, CSS, and JavaScript**.
