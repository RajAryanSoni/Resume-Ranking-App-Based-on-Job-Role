def remove_bias(text):
    bias_terms = [
        "he", "she", "him", "her", "male", "female",
        "age", "years old", "iit", "nit", "bits", "college"
    ]

    for term in bias_terms:
        text = text.replace(term, "")

    return text
