from normalizer import normalize_phone

def merge_candidate(csv_data, resume_data):

    merged = {}

    # Name
    if csv_data["name"]:
        merged["name"] = {
            "value": csv_data["name"],
            "source": "CSV",
            "confidence": 0.9
        }
    else:
        merged["name"] = {
            "value": resume_data["name"],
            "source": "Resume",
            "confidence": 0.7
        }

    # Email
    if csv_data["email"]:
        merged["email"] = {
            "value": csv_data["email"],
            "source": "CSV",
            "confidence": 0.9
        }
    else:
        merged["email"] = {
            "value": resume_data["email"],
            "source": "Resume",
            "confidence": 0.7
        }

    # Phone
    if csv_data["phone"]:
        merged["phone"] = {
        "value": normalize_phone(csv_data["phone"]),
        "source": "CSV",
        "confidence": 0.9
    }
    else:
       merged["phone"] = {
        "value": normalize_phone(resume_data["phone"]),
        "source": "Resume",
        "confidence": 0.7
    }

    # Company
    merged["company"] = {
        "value": csv_data["company"],
        "source": "CSV",
        "confidence": 0.9
    }

    # Title
    merged["title"] = {
        "value": csv_data["title"],
        "source": "CSV",
        "confidence": 0.9
    }

    # Skills
    merged["skills"] = {
        "value": resume_data["skills"],
        "source": "Resume",
        "confidence": 0.7
    }

    return merged