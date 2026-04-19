def classify_page(text):
    text = text.lower()

    if "claim form" in text:
        return "claim_forms"
    
    elif "bank" in text or "account number" in text or "cheque" in text:
        return "cheque_or_bank_details"
    
    elif "government id" in text or "id card" in text:
        return "identity_document"
    
    elif "discharge summary" in text:
        return "discharge_summary"
    
    elif "itemized" in text or "hospital bill" in text or "total amount" in text:
        return "itemized_bill"
    
    elif "prescription" in text or "rx" in text:
        return "prescription"
    
    elif "laboratory" in text or "report" in text:
        return "investigation_report"
    
    elif "receipt" in text or "cash receipt" in text:
        return "cash_receipt"
    
    else:
        return "other"


def segregate_pages(pages):
    result = {}

    for page in pages:
        page_num = page["page_number"]
        text = page["text"]

        doc_type = classify_page(text)
        result[page_num] = doc_type

    return result