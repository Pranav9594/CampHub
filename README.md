# CampHub

A clean and responsive **college file storage and management web application** built with **Flask, Supabase, HTML, CSS, and JavaScript**.

CampHub provides students with a simple platform to upload, organize, search, download, and manage their academic files in one place.

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
* ☁️ Supabase integration for cloud database and file storage
* 📱 Responsive interface for desktop and mobile
* ⚡ Flask backend for application logic

## 🛠️ Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Backend programming             |
| Flask      | Web framework and API handling  |
| Supabase   | Cloud database and file storage |
| PostgreSQL | Database used by Supabase       |
| HTML       | Page structure                  |
| CSS        | Styling and responsive design   |
| JavaScript | Frontend interactions           |

## 🏗️ Architecture

```text
                         CampHub
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
camphub/
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

> The exact project structure may vary depending on the Supabase configuration and deployment setup.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/camphub.git
cd camphub
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

Add your Supabase credentials to your environment variables:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

> Never commit your Supabase keys or `.env` file to GitHub.

Add the following to `.gitignore`:

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

CampHub uses **Supabase** for cloud-based database and storage functionality.

### Database

File metadata can be stored in the Supabase PostgreSQL database, including:

* File name
* File path
* Semester
* Subject
* Category
* Upload date

### Storage

Academic files can be stored in a Supabase Storage bucket, allowing files to be managed in the cloud rather than relying only on local storage.

## 📂 File Management

Users can:

1. Upload academic files
2. Select semester, subject, and category
3. Search files
4. View file information
5. Download files
6. Delete files

## 📊 Dashboard

CampHub provides a responsive dashboard with organized file cards and metadata, making it easier for students to quickly find and manage their academic resources.

## 🔐 Security

Sensitive configuration values should never be hard-coded into the application.

Use environment variables:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

For production deployments, configure appropriate **Supabase Row Level Security (RLS)** and Storage policies.

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
* ☁️ Enhanced cloud storage management
* 📱 Progressive Web App support

## 📌 Project Status

**🚧 Currently in development**

CampHub is designed as an academic file management platform that helps students keep notes, presentations, documents, and other study materials organized in one place.

## 🎯 Purpose

The goal of CampHub is to provide students with a centralized platform for managing college-related files instead of keeping academic documents scattered across different folders and devices.
