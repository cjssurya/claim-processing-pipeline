import re

def extract_discharge_data(pages, classification):
    data = {
        "diagnosis": None,
        "admission_date": None,
        "discharge_date": None,
        "doctor": None
    }

    for page in pages:
        page_num = page["page_number"]
        text = page["text"]

        if classification[page_num] == "discharge_summary":

            # Diagnosis
            diag_match = re.search(r"Diagnosis:\s*(.*)", text)
            if diag_match:
                data["diagnosis"] = diag_match.group(1).strip()

            # Admission Date
            admit_match = re.search(r"Admission Date:\s*(.*)", text)
            if admit_match:
                data["admission_date"] = admit_match.group(1).strip()

            # Discharge Date
            discharge_match = re.search(r"Discharge Date:\s*(.*)", text)
            if discharge_match:
                data["discharge_date"] = discharge_match.group(1).strip()

            # ✅ FIXED Doctor Extraction (handles OCR text)
            doctor_match = re.search(r"Dr\.\s*[A-Za-z\s]+", text)
            if doctor_match:
                data["doctor"] = doctor_match.group(0).strip()

    return data