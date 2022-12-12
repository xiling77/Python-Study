favorite_language = {
    'jen':['Python','ruby'],
    'sarah':['c'],
    'edward':['ruby'],
    'jen':['Python','haskell'],
    }
    
    
    
for name,languages in favorite_language.items():
    print("\n" + name.title() + "'s favorite language are: ")
    for language in languages:
        print("\t" + language.title())