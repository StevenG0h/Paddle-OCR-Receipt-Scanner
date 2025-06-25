from paddleocr import PaddleOCR
from db import Receipt, session

def extract_total_from_texts(rec_texts):
    total = None
    subtotal = None
    tax = None

    norm_texts = [text.strip().lower().replace(":", "").replace("rp", "") for text in rec_texts]

    for i, text in enumerate(norm_texts):
        if text in ["grand total", "total", "total harga"]:
            if i + 1 < len(norm_texts):
                value = norm_texts[i + 1].replace(".", "").replace(",", ".")
                if value.replace(".", "").isdigit():
                    total = float(value)
        elif text in ["subtotal", "jumlah", "total sementara"]:
            if i + 1 < len(norm_texts):
                value = norm_texts[i + 1].replace(".", "").replace(",", ".")
                if value.replace(".", "").isdigit():
                    subtotal = float(value)
        elif "pb1" in text or "pajak" in text:
            if i + 1 < len(norm_texts):
                value = norm_texts[i + 1].replace(".", "").replace(",", ".")
                if value.replace(".", "").isdigit():
                    tax = float(value)

    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

def extractReceipt(image):
    try :
        ocr = PaddleOCR(lang='en')
        results = ocr.predict(image)
        total = extract_total_from_texts(results[0]['rec_texts'])
        receipt = Receipt(total=total["total"], subtotal=total["subtotal"], tax=total["tax"])
        session.add(receipt)
        session.commit()
    except Exception as e:
        print(e)
        total = None
    return total
