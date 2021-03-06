def fill_mini_bio_kafka(nomfamille, prenom, idBio, topic, producer):
    json_minibio = {
        "idBio": idBio,
        "nom": nomfamille,
        "prenom": prenom
    }
    producer.send(topic, value=(json_minibio))


def fill_googlethon_kafka(nomfamille, prenom, idBio, idDictionary, depthLevel, numberUrl, topic, producer):
    json_minibio = {
        "idBio": idBio,
        "nom": nomfamille,
        "prenom": prenom,
        "idDictionary": idDictionary,
        "depthLevel": depthLevel,
        "numberUrl": numberUrl
    }
    producer.send(topic, value=(json_minibio))


def fill_travelthon_kafka(destination, idBio, topic, producer):
    json_togo = {
        "destination": destination,
        "idBio": idBio
    }
    producer.send(topic, value=(json_togo))


def fill_housTOcompara(nom, prenom, bytified_picture, picture_extension, bio_id, producer, topic):
    producer.send(topic, value=(nom, prenom, bytified_picture, picture_extension, bio_id))
