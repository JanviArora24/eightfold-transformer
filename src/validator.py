def validate(candidate):

    required = [
        "name",
        "email",
        "phone"
    ]

    for field in required:

        if not candidate[field]["value"]:

            print(field,"missing")