import re

def extract_id_data(pages, classification):
    data = {
        "name": None,
        "dob": None,
        "policy_number": None,
        "id_number": None
    }

    for page in pages:
        page_num = page["page_number"]
        text = page["text"]

        if classification[page_num] in ["identity_document", "claim_forms"]:
            
            # Name
            name_match = re.search(r"Patient Name:\s*(.*)", text)
            if name_match:
                data["name"] = name_match.group(1).strip()

            # DOB
            dob_match = re.search(r"Date of Birth:\s*(.*)", text)
            if dob_match:
                data["dob"] = dob_match.group(1).strip()

            # Policy
            policy_match = re.search(r"Policy Number:\s*(.*)", text)
            if policy_match:
                data["policy_number"] = policy_match.group(1).strip()

            # ID Number (from ID card)
            id_match = re.search(r"ID Number:\s*(.*)", text)
            if id_match:
                data["id_number"] = id_match.group(1).strip()

    return data