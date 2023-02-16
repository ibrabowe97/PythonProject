#coding:utf-8
"""
mode d'ouvertures: r, w, a, x -> (lecture / ecriture), r+ (lecture / ecriture dans un meme fichier);
    open(NomVarFic, modeLecture) -> ouvrir
    nomVarFic.close() -> fermer
   if nomVarFic.closed -> verifier si fermer
   nomVarFic.read() -> lire le contenu du fichier (readline -> une ligne, readlines -> toute les lignes comme liste)

autre mode :
    with open(nomFile, modeOuv) as NomVar :
     // code...
     pas besoin de fermeture

------------------------------------------------------------------------
"""
