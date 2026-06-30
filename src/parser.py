import pdfplumber
import pandas as pd
import re


def parse_csv(file_path):
    df = pd.read_csv(file_path)

    candidate = df.iloc[0]

    return {
        "name": candidate["name"],
        "email": candidate["email"],
        "phone": str(candidate["phone"]),
        "company": candidate["current_company"],
        "title": candidate["title"]
    }


def parse_resume(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    name = ""
    email = ""
    phone = ""
    skills = []

    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)

    if email_match:
        email = email_match.group()

    phone_match = re.search(r'\d{10}', text)

    if phone_match:
        phone = phone_match.group()

    lines = text.split("\n")

    for line in lines:

        if line.lower().startswith("name"):

            name = line.split(":")[1].strip()

    if "Skills" in lines:

        index = lines.index("Skills")

        skills = [
            line.strip()
            for line in lines[index+1:]
            if line.strip()
        ]

    return {

        "name": name,

        "email": email,

        "phone": phone,

        "skills": skills
    }