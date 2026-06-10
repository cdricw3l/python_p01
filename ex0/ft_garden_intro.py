# l'idiome __name__ == "__main__"
# il permet d'exécuter du code lorsque le fichier est exécuté comme un script,
# mais pas lorsqu'il est importé comme un module

if __name__ == "__main__":
    # https://docs.python.org/fr/3.14/library/__main__.html
    # https://datascientist.fr/en/blog/tutoriel-python-que-fait-if-name-main-en-programmation
    name:  str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")
