import pandas as pd
import json

f = open("annotation.json")
data = json.load(f)
f.close()
schema = data["schema"]
classess = [classification_type["name"] for classification_type in schema["classification_types"]]
examples = data["examples"]

print(data)

annotators: {
    1: "Katarina-Glorija",
    2: "Dejan",
    3: "Jelena",
    4: "Alek",
    5: "Milica"
}

def get_comments(comments):
    made_comment = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }

    for comment in comments:
        made_comment[str(comment["made_by_id"])].append(comment["text"])

    ret_val = dict()
    for key, value in made_comment.items():
        if len(made_comment[key]) == 0:
            ret_val[key] = None
        else:
            ret_val[key] = value[0]

    return ret_val


def get_classifications(classifications):
    clfs = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }

    for classification in classifications:
        class_name = classification["classname"]
        for annotator in classification["classified_by"]:
            clfs[str(annotator["annotator_id"])].append(class_name)

    return clfs


def get_aspekti_and_emocije(classifications):
    aspekti = ['Instrukcioni materijali', 'Zadaci', 'Lekcija', 'Projekat', 'Drugi aspekt', 'Tutor']
    emocije = ['Angažovanost', 'Frustracija', 'Neutralno', 'Nezainteresovanost', 'Umor', 'Zbunjenost']

    a = []
    e = []

    for classification in classifications:
        if classification in aspekti:
            a.append(classification)
        elif classification in emocije:
            e.append(classification)
        else:
            pass

    if len(a) == 0:
        ret_a = None
    else:
        ret_a = a[0]

    if len(e) == 0:
        ret_e = None
    else:
        ret_e = e[0]

    return ret_a, ret_e


text = []
katarina_aspekt = []
katarina_emocija = []
katarina_comment = []

dejan_aspekt = []
dejan_emocija = []
dejan_comment = []

jelena_aspekt = []
jelena_emocija = []
jelena_comment = []

alek_aspekt = []
alek_emocija = []
alek_comment = []

milica_aspekt = []
milica_emocija = []
milica_comment = []

for example in examples:
    text.append(example["content"])

    comments = get_comments(example["comments"])
    katarina_comment.append(comments["1"])
    dejan_comment.append(comments["2"])
    jelena_comment.append(comments["3"])
    alek_comment.append(comments["4"])
    milica_comment.append(comments["5"])

    classifications = get_classifications(example["classifications"])
    aspekt, emocija = get_aspekti_and_emocije(classifications["1"])
    katarina_aspekt.append(aspekt)
    katarina_emocija.append(emocija)

    aspekt, emocija = get_aspekti_and_emocije(classifications["2"])
    dejan_aspekt.append(aspekt)
    dejan_emocija.append(emocija)

    aspekt, emocija = get_aspekti_and_emocije(classifications["3"])
    jelena_aspekt.append(aspekt)
    jelena_emocija.append(emocija)

    aspekt, emocija = get_aspekti_and_emocije(classifications["4"])
    alek_aspekt.append(aspekt)
    alek_emocija.append(emocija)

    aspekt, emocija = get_aspekti_and_emocije(classifications["5"])
    milica_aspekt.append(aspekt)
    milica_emocija.append(emocija)

d = {
    "tekst": text,
    "Katarina_aspekt": katarina_aspekt,
    "Katarina_emocija": katarina_emocija,
    "Dejan_aspekt": dejan_aspekt,
    "Dejan_emocija": dejan_emocija,
    "Jelena_aspekt": jelena_aspekt,
    "Jelena_emocija": jelena_emocija,
    "Alek_aspekt": alek_aspekt,
    "Alek_emocija": alek_emocija,
    "Milica_aspekt": milica_aspekt,
    "Milica_emocija": milica_emocija,
    "Katarina_komentar": katarina_comment,
    "Dejan_komentar": dejan_comment,
    "Jelena_komentar": jelena_comment,
    "Alek_komentar": alek_comment,
    "Milica_komentar": milica_comment
}

df = pd.DataFrame(d)
df.to_excel("emotions_annotators.xlsx", index=False)