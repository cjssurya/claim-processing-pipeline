import re

def extract_bill_data(pages, classification):
    items = []
    total = None

    for page in pages:
        page_num = page["page_number"]
        text = page["text"]

        if classification[page_num] == "itemized_bill":

            lines = text.split("\n")

            for line in lines:
                # Better matching (handles OCR noise)
                match = re.search(r"([A-Za-z ].+?)\s+(\d{2,5}\.\d{2})", line)
                if match:
                    description = match.group(1).strip()
                    amount = float(match.group(2))

                    items.append({
                        "description": description,
                        "amount": amount
                    })

            # Better total detection
            total_match = re.search(r"(Total Amount|TOTAL|Total)\s*[:\-]?\s*(\d+\.\d{2})", text, re.IGNORECASE)
            if total_match:
                total = float(total_match.group(2))

    return {
        "items": items,
        "total": total
    }