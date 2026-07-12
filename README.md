# 🌍 EcoSphere - ESG Management Platform

> **AI-Powered ESG Management Platform built on Odoo 18**

EcoSphere is a comprehensive Environmental, Social, and Governance (ESG) management platform developed on **Odoo 18** for the Odoo Hackathon. It enables organizations to measure, manage, and improve sustainability by integrating ESG directly into daily ERP operations.

The platform combines environmental tracking, employee engagement, governance compliance, gamification, real-time analytics, and AI-powered insights into a single unified solution.

---

# 📖 Table of Contents

- Overview
- Problem Statement
- Solution
- Features
- Module Architecture
- Technology Stack
- Project Structure
- Installation
- Demo Users
- AI Integration
- Reports
- Security (RBAC)
- Future Enhancements
- Team

---

# 🎯 Problem Statement

Organizations collect operational data through ERP systems, but ESG information is often scattered across multiple systems, manually maintained, and difficult to analyze.

EcoSphere solves this problem by integrating ESG management directly into Odoo, providing:

- Environmental monitoring
- Employee engagement
- Governance compliance
- Real-time dashboards
- AI-driven insights
- Gamification

---

# 💡 Solution

EcoSphere provides a modular ESG ecosystem consisting of:

- Environmental Management
- Social Responsibility
- Governance Compliance
- Employee Gamification
- AI Assistant
- Analytics Dashboard
- Enterprise Reporting

---

# 🚀 Features

## 🌱 Environmental

- Carbon Accounting
- Emission Factors
- Carbon Transactions
- Sustainability Goals
- Department Carbon Tracking
- Environmental Dashboard
- Environmental Reports

---

## 🤝 Social

- CSR Activities
- Employee Participation
- Volunteer Tracking
- Diversity Metrics
- Engagement Analytics
- Social Score Engine

---

## 🏛 Governance

- ESG Policies
- Policy Acknowledgements
- Governance Audits
- Compliance Issues
- Risk Tracking
- Governance Reports

---

## 🏆 Gamification

- Sustainability Challenges
- XP System
- Badges
- Rewards
- Reward Redemption
- Department Leaderboards
- Employee Leaderboards

---

## 🤖 AI Assistant

Powered by **Groq LLM**.

Capabilities include:

- ESG Summary
- Department Analysis
- Sustainability Recommendations
- Carbon Insights
- Compliance Suggestions
- Natural Language Queries

Example:

> "Why is the Engineering department's ESG score decreasing?"

---

# 📊 Dashboard

The dashboard provides:

- Overall ESG Score
- Environmental Score
- Social Score
- Governance Score
- Department Rankings
- Challenge Statistics
- CSR Analytics
- Carbon Trends
- Leaderboards
- Recent Activities

---

# 📑 Reports

Generate:

- Environmental Report
- Social Report
- Governance Report
- ESG Summary Report
- Custom Reports

Export Formats:

- PDF
- Excel
- CSV

---

# 🏗 Module Architecture

```text
eco_base
│
├── eco_platform
│
├── eco_environment
├── eco_social
├── eco_governance
│
├── eco_gamification
│
├── eco_dashboard
├── eco_reports
│
└── eco_ai
```

---

# 🛠 Technology Stack

| Component | Technology |
|------------|------------|
| ERP | Odoo 18 |
| Backend | Python |
| Database | PostgreSQL |
| Frontend | OWL, JavaScript, XML |
| ORM | Odoo ORM |
| AI | Groq API |
| Charts | OWL Dashboard |
| Reports | Odoo Reporting Engine |

---

# 📂 Project Structure

```text
ecosphere/

addons/

├── eco_base/

├── eco_platform/

├── eco_environment/

├── eco_social/

├── eco_governance/

├── eco_gamification/

├── eco_dashboard/

├── eco_reports/

└── eco_ai/

README.md

requirements.txt

.env.example
```

---

# 🔐 Role-Based Access Control (RBAC)

EcoSphere implements four security roles.

| Role | Access |
|-------|---------|
| Employee | Participate in challenges, CSR activities, rewards |
| Department Head | Approvals, department monitoring |
| ESG Manager | ESG configuration, reports, governance |
| Eco Administrator | Full system administration |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecosphere.git
cd ecosphere
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Odoo

Update:

```text
odoo.conf
```

Example:

```ini
addons_path = odoo/addons,ecosphere/addons

db_host = localhost
db_port = 5432
db_user = odoo
db_password =
```

---

## Run Odoo

```bash
python odoo-bin -c odoo.conf -d ecosphere
```

---

# 🤖 AI Configuration

Create:

```text
.env
```

```ini
GROQ_API_KEY=YOUR_GROQ_API_KEY
GROQ_MODEL=llama-3.1-8b-instant
```

---

# 👥 Demo Users

| Role | Login |
|------|------|
| Administrator | admin |
| ESG Manager | esg@eco.com |
| Department Head | hr@eco.com |
| Employee | pooja@eco.com |

---

# 🔄 Business Workflow

```text
Department

↓

Business Activities

↓

Environmental
Social
Governance

↓

Department ESG Score

↓

Organization ESG Score

↓

Dashboard

↓

Reports

↓

AI Insights
```

---

# 🎯 Hackathon Highlights

✅ Modular Odoo Architecture

✅ Real-time ESG Dashboard

✅ AI-powered ESG Assistant

✅ Event-driven Gamification

✅ Enterprise Reporting

✅ Role-Based Access Control

✅ Production-ready Odoo 18 Modules

---

# 🔮 Future Enhancements

- IoT Carbon Sensors
- Predictive ESG Analytics
- Mobile Application
- External ESG Reporting Standards
- ERP Integrations (Purchase, Manufacturing, Fleet)
- Sustainability Benchmarking

---

# 🏆 Built For

**Odoo Hackathon 2026**

EcoSphere demonstrates how organizations can seamlessly integrate ESG management into their ERP ecosystem while encouraging employee participation and providing actionable AI-driven insights.

---

# 📄 License

This project is developed for the Odoo Hackathon.

---

# ❤️ Acknowledgements

- Odoo 18
- PostgreSQL
- Groq
- Python
- OWL Framework
