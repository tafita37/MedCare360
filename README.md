# 📘 MedCare360

## 1. Overview

### 📝 Project description
MedCare360 is an Odoo-based modular healthcare management system comprising three key modules — hospital, medical_consultation, and infirmary_management — designed to ensure streamlined patient care, comprehensive consultations, and efficient nursing rounds management.

### 🎯 Objective
MedCare360 aims to provide an integrated and modular healthcare platform to improve patient management, facilitate medical consultations, and optimize nursing workflows.

---

## 2. Features

### ✅ Features list

- Manager side:
    - CRUD for Disease Type
    - CRUD for Disease
    - CRUD for Symptom
    - CRUD for Medication
    - List of patients held on site
    - List of requests + assignment to a nurse
    - List of nurses with the number of requests each needs to handle
- Patient side:
    - Request form
    - View their status
- Doctor side:
    - Prescription form + final action
    - List of medication recommendations during treatment
    - View records with the same symptom as a disease
    - Final action
    - List of consultations
    - Export patient record to PDF
- Nurse side:
    - List of requests + assignment to a doctor to create a consultation
    - Daily and weekly rounds (filter: done/to be done)
    - Create a round
    - Click on a round to release a patient or reschedule it and change the status
    - Export weekly round report to PDF


---

## 3. Requirements

### 🛠️ Required environment
- **Operating System**: Windows / macOS / Linux
- **Languages & Frameworks**: Odoo 18, Python 3.11.9
- **Database**: PostgreSQL

---

## 4. Installation

🔧 Installation instructions :

### Clone the repository
```bash
git clone https://github.com/tafita37/MedCare360.git
```

### Setup the project in the Odoo modules directory, create a virtual environment, install dependencies, and run the project:

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python odoo-bin -c odoo.conf -u <module_name> -d <base_name> --dev xml
```