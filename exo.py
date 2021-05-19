# TODO étape 1 - Remplacez les ?? par le code adéquat pour créer une liste vide
invites = []

# TODO étape 2 - Ajoutez 3 invités à la liste: Joey, Martin et Marie
invites.append('Joey')
invites.append('Martin')
invites.append('Marie')

# TODO étape 3 – Affichez la taille de la liste
print(len(invites))

# TODO étape 4 - Remplacez Martin par John dans la liste
invites.insert(2, 'John')

# TODO étape 5 - Supprimez Joey de la liste
invites.remove('Joey')

# affichez le contenu de la liste
for invite in invites :
	print(invite)
