# 2017-01 Hackinscience Python

## 2017-01-16 Intro
* set: list with no duplicates (useful to de-duplicate)
    * basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    * set('apple', 'pear', 'apple', 'pear', 'pear', 'banana')
* dictionary with key: value
    * {'jack': 4098, 'sape': 4139}

## 2017-01-21 Advice in email exchanges
* about "Password Generator"
* module `string`
* respecter PEP8
* éviter "import *" hors du REPL
* les strings sont itérables en Python, donc choice("abc") et choice(["a", "b", "c"]) sont sémantiquement extrêmement proches
* `if with_digits == True:` est une tautologie, `if with_digits:` est la manière canonique de l'écrire
* préférer `is True` à `== True`, `is None` à `== None`
* fort répétitives les lignes 27-96 : ne pourrais-tu pas te débrouiller avec un "ajouter une lettre dans tous les cas puis, if with_digits ajouter un digit sinon une lettre puis if with_uppercase rajouter une majuscule sinon une lettre" ?
