import unittest
import re
import random
import unittest

def is_even(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
    return nbr % 2 == 0

class MyTest(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(1))
        self.assertEqual(is_even(0), True)

if __name__ == '__main__':
    unittest.main()
    
def clean_text(text):
    """
    Nettoyage d'une pavé de texte pour respecter la typographie française.
    """
    ret = re.sub(r'^(\s*)(.*?)(\s*)$', r'\2', text) # Suppression des espaces au début et à la fin du texte
    ret = re.sub(r'\s*\!{2,}', u'!', ret)
    ret = re.sub(r'\s*\?{2,}', u'?', ret)
    ret = re.sub(r"\s*\,+", u',', ret)
    ret = re.sub(r'\,([^\s])', r', \1', ret)
    ret = re.sub(r'\s*\.{3,}', u'…', ret) # Remplacement de "(espace)...(x fois)" par "…"
    ret = re.sub(r'\s\.', u'.', ret) # Remplacement de " ." par "."
    ret = re.sub(r'\.{2}', u'…', ret) # Remplacement de ".." par "…"
    ret = re.sub(r'([^0-9])\1{3,}', r'\1', ret) # Suppression des multiples répétitions de caractères (plus de 3) sauf pour les chiffres
    ret = re.sub(r'([^\s])([?!:])', r'\1 \2', ret) # Remplacement de "blabla!" par "blabla !"
    ret = re.sub(r'([?!])([^\s:\)])', r'\1 \2', ret) # Remplacement de "?blabla" par "? blabla"
    return ret

class TestText(unittest.TestCase):
    def setUp(self):
        self.text_checks = (
            (u'Un texte avec pluuuuuuusieurs', u'Un texte avec plusieurs'),
            (u'Collage!', u'Collage !'),
            (u'!Collage', u'! Collage'),
            (u'Espaces      en trop', u'Espaces en trop'),
            (u"Trop d'exclamation!!!! ou d'interrogation ??", u"Trop d\'exclamation ! ou d\'interrogation ?"),
            (u'   Espaces debut ou fin ', u'Espaces debut ou fin'),
            (u'Smileys :), ;):)', u'Smileys :), ;) :)'),
            (u'(Une ponctuation avant une parenthese !)', u'(Une ponctuation avant une parenthese !)'),
            (u'Quelques paquerettes . .', u'Quelques paquerettes…'),
            (u'[color=red][Edit : merci de respecter les regles et de proposer des titres explicites.][/color]', u'[color=red][Edit : merci de respecter les regles et de proposer des titres explicites.][/color]'),
            (u'60000 ans', u'60000 ans'),
            (u'Une , virgule', u'Une, virgule'),
            (u'Deux,, virgules', u'Deux, virgules'),
            (u'Virgule,collée', u'Virgule, collée'),
        )

    def test_clean_text(self):
        for check in self.text_checks:
            self.assertEqual(clean_text(check[0]), check[1])

def trait(mot):
    if mot[0] == "a" or mot[0] == "A" :
        return("Appartement")
    elif  mot[0] == "m" or mot[0] == "M":
            return("Maison")
    else:
            return("")
            
class MyTest2(unittest.TestCase):
    def test_is_even(self):
        self.assertIsNone(trait("yes"))
        

if __name__ == '__main__':
    unittest.main()