# 🎓 Student OS

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

<p align="center">
A productivity operating system built specifically for students to manage academics, events, priorities, deadlines and personal growth from a single dashboard.
</p>

---

## 📖 Overview

Student OS helps students organize every aspect of their academic and personal life through an integrated productivity dashboard.

Instead of using multiple apps for tasks, scheduling, priorities and analytics, Student OS combines everything into one centralized platform.

---

## ✨ Features

### 📊 Smart Dashboard

- Real time productivity metrics
- Focus card for highest priority task
- Life area overview
- Upcoming events summary
- Task completion statistics

### ✅ Task Management

- Create tasks
- Set importance and urgency levels
- Automatic priority scoring
- Mark tasks as completed
- Delete tasks instantly

### 📅 Calendar System

- Schedule events
- Categorize activities
- Conflict detection
- Timeline organization

### 📈 Analytics

- Productivity insights
- Completion tracking
- Category wise distribution
- Performance monitoring

### 🎨 Theme Engine

- Aurora Theme
- Sunset Theme
- Dynamic UI updates

### 🎯 Focus Mode

- Automatically highlights highest priority task
- Displays progress visualization
- Helps students focus on what matters most

---

# 🏗 System Architecture

```text
                ┌─────────────────┐
                │      User       │
                └────────┬────────┘
                         │
                         ▼

                ┌─────────────────┐
                │   Streamlit UI  │
                └────────┬────────┘
                         │

     ┌───────────────────┼───────────────────┐
     ▼                   ▼                   ▼

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Dashboard   │  │    Tasks     │  │   Calendar   │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────┬───────┴───────┬─────────┘
                 ▼               ▼

        ┌───────────────────────┐
        │     Service Layer      │
        │ Dashboard Service      │
        │ Conflict Detection     │
        └───────────┬───────────┘
                    │
                    ▼

         ┌─────────────────────┐
         │   SQLite Database   │
         └─────────────────────┘
```

---

# ⚙ Dashboard Flow

```text
Tasks + Events
       │
       ▼

SQLite Database
       │
       ▼

Dashboard Queries
       │
       ▼

Dashboard Service
       │
       ▼

Metrics Calculation
       │
       ▼

Dashboard Rendering
```

---

# 🧠 Priority Calculation Logic

Each task receives a priority score.

```text
Importance (1-10)
         │
         ▼

Urgency (1-10)
         │
         ▼

Priority Score
=
Importance × Urgency
```

Example:

```text
Importance = 9
Urgency = 10

Priority Score = 90
```

The highest scoring task becomes the Focus Task on the dashboard.

---

# 📂 Project Structure

```text
Managing-Tasks
│
├── assets
│   ├── layout.py
│   ├── sidebar.py
│   ├── theme.py
│   ├── themes.py
│   └── typography.py
│
├── components
│   ├── dashboard.py
│   ├── hero.py
│   ├── priorities.py
│   ├── life_areas.py
│   ├── productivity.py
│   ├── focus.py
│   ├── deadlines.py
│   ├── activity_chart.py
│   └── alerts.py
│
├── database
│   ├── db.py
│   ├── init_db.py
│   ├── dashboard_queries.py
│   ├── task_queries.py
│   └── event_queries.py
│
├── models
│   └── task.py
│
├── pages
│   ├── 1_Tasks.py
│   ├── 2_Calendar.py
│   └── 3_Analytics.py
│
├── services
│   ├── dashboard_service.py
│   └── conflict_detector.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🗄 Database Design

### Tasks Table

```text
id
title
category
deadline
importance
urgency
completed
scheduled_date
```

### Events Table

```text
id
title
category
event_date
start_time
end_time
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Student-OS.git
```

Move into project directory

```bash
cd Student-OS
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

## Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Tasks

![Tasks](screenshots/tasks.png)

---

## Calendar

![Calendar](screenshots/calendar.png)

---

## Analytics

![Analytics](screenshots/analytics.png)

---

# 🎯 Use Cases

### Student Planning

- Assignment tracking
- Exam preparation
- Project deadlines

### Career Growth

- Internship preparation
- Skill development
- Placement tracking

### Personal Development

- Habit tracking
- Personal goals
- Fitness planning

### Event Management

- Club activities
- College events
- Competition schedules

---

# 📊 Current Tech Stack

| Layer | Technology |
|---------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite |
| Data Processing | Pandas |
| Scheduling Logic | Python Datetime |
| Analytics | Plotly |

---

# 🔮 Future Enhancements

- [x] Dashboard
- [x] Tasks Module
- [x] Calendar Module
- [x] Analytics Module
- [x] Theme System
- [x] Focus Engine
- [ ] AI Schedule Generator
- [ ] Notification System
- [ ] Mobile Responsive UI
- [ ] Cloud Synchronization
- [ ] User Authentication
- [ ] Multi User Support

---

# 👨‍💻 Contributors

### Jatin Choudhary

Frontend Development  
UI Design  
Dashboard Architecture

### Team Members

Backend Development  
Database Design  
Scheduling Logic

---

# 📄 License

This project is licensed under the MIT License.

---

<p align="center">
Built with ❤️ using Streamlit and Python
</p>