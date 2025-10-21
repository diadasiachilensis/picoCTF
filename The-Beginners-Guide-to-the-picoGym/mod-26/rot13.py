def rot13(word):
    abc=[chr(i) for i in range(97,123)]
    for a in range(word):
        for b in range(abc):
            if a == b:
                
