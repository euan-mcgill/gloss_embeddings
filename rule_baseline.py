def get_person(morph):
    if "Person=1" in morph and "Number=Sing":
        return "INDX.PRO:1SG"
    elif "Person=1" in morph and "Number=Plur":
        return "INDX.PRO:1PL"
    elif "Person=2" in morph and "Number=Sing":
        return "INDX.PRO:2SG"
    elif "Person=2" in morph and "Number=Plur":
        return "INDX.PRO:2PL"
    elif "Person=3" in morph and "Number=Sing":
        return "INDX.PRO:3SG"
    elif "Person=3" in morph and "Number=Plur":
        return "INDX.PRO:3PL"
    else:
        return "INDX" # cleaned up further with regex replacement

# Also replaced Aquí/Allí/Ahí with INDX.LOC and Eso/Esto... with INDX.DEM in regex
# In \b(ESTE|ESO|ESE|ESA)\b Out INDX.DEM
# In \b(AQUÍ|ALLÍ|ALLÁ|AHÍ)\b Out INDX.LOC
# In (indx.pro:...)( a )(indx.pro:...) Out INDX.AUX

def baseline_translation_word_pos(tokens):
    new_tokens = []
    skip_next = False
    for t1,t2 in zip(tokens,tokens[1:]):
        if skip_next:
            skip_next = False
            continue
        if t1["lemma"] == "tener" and t2["lemma"] == 'que':
            new_token = t1.copy()
            new_token["lemma"] = "necesitar"
            new_tokens.append(new_token)
            skip_next = True
        elif t1["pos"] == 'DET' and 'Poss=Yes' in t1["morph"] and t2["pos"] == 'NOUN':
            new_tokens.append(t2.copy())
            new_tokens.append({ "pre": True, "lemma": "PROPIO", "pos": "ADJ"})
            new_tokens.append({ "pre": True, "lemma": get_person(t1["morph"]), "pos": "PRON"})
            skip_next = True
        elif t1["text"] == "no" and t2["pos"] == "VERB":
            new_tokens.append(t2.copy())
            new_tokens.append(t1.copy())
        else:
            new_tokens.append(t1.copy())
    if not skip_next:
        new_tokens.append(tokens[-1].copy())

    result = []
    for t in new_tokens:
        if t["pre"]:
            result.append((t["lemma"],t["pos"]))
            continue

        if t["pos"] == 'DET':
            continue

        if t["pos"] == 'PUNCT':
            continue

        if t["pos"] == 'ADP' and t["text"] in ['de','en']:
            continue

        if t["dep"] == 'cop':
            continue

        if t["pos"] == 'VERB' and 'Tense=Fut' in t["morph"]:
            result.append(('FUTURO','ADV'))

        if t["pos"] == 'VERB' and 'Person=2' in t["morph"]:
            result.append(('INDX.PRO:2SG','PRON'))
            #result.append((t["lemma"],t["pos"]))

        # if t["pos"] == 'NOUN' and 'Number=Plur' in t["morph"]:
        #     result.append(('PLURAL','NUM'))

        if t["text"] == 'denei':
            result.append(('DNI','NOUN'))

        if t["text"] == 'como':
            result.append(('IGUAL','ADV'))

        # elif t["dep"] == 'cop':
        #     result.append(('SE-LLAMA','VERB'))
        else:
            result.append((t["lemma"].upper(),t["pos"]))
    return result

def baseline_translation(tokens):
    word_pos = baseline_translation_word_pos(tokens)
    # random reordering a la Moryossef here?
    return " ".join(w for (w,p) in word_pos)
