# 🏢 One Stop Insurance Policy Program  

A Python program to enter, calculate, and manage new insurance policy information for the **One Stop Insurance Company**.  

This project handles customer data entry, calculates premiums, applies optional coverages, manages payment options, and stores insurance policy details in a file for future use.  

---

## 📌 Features  
- Collects customer details (name, address, province, phone, etc.)  
- Validates input fields (postal codes, phone numbers, province codes, payment methods)  
- Calculates:  
  - Insurance premiums  
  - Extra liability coverage  
  - Glass coverage  
  - Loaner car fees  
  - HST and total cost  
  - Monthly or down-payment installment amounts  
- Generates a formatted invoice including:  
  - Customer details  
  - Payment breakdown  
  - Coverage details  
  - Previous claims list  
- Saves policy data to `InsurancePolicy.dat`  
- Updates and persists policy numbers using `const.dat`  
- Includes a progress bar effect for saving data  

---

## 🛠️ Technologies Used  
- **Python 3**  
- `datetime` – for date formatting and calculating first payment dates  
- `time` & `sys` – for progress bar and visual effects  
- File handling (`open`, `read`, `write`) for saving and updating records  

---

## 🚀 Getting Started  

### 1. Clone the repository  
```bash
git clone https://github.com/yourusername/insurance-policy-program.git
cd insurance-policy-program
```

### 2. Run the program
python insurance_policy.py

### 3. Files Used

- const.dat – Stores constants and the latest policy number (updated after each run)

- InsurancePolicy.dat – Stores saved customer insurance policy records
