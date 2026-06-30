import phonenumbers


def normalize_phone(phone):

    try:

        number = phonenumbers.parse(phone, "IN")

        return phonenumbers.format_number(
            number,
            phonenumbers.PhoneNumberFormat.E164
        )

    except:

        return phone