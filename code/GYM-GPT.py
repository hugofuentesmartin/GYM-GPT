print("Hola! Soc GYM-GPT, el teu assistent del gimnàs.")
nom = input("Com et dius? ")
print(f"Encantat, {nom}. T’ajudaré amb el teu entrenament.")

while True:
    resposta = input(f"\nSobre què vols parlar, {nom}? (entrenament, dieta, press banca)\n> ").lower()

    if "entrenament" in resposta:
        print("Entrenar és essencial. Quin dia t’agrada més anar al gimnàs?")
        input("> ")
        print("Bona elecció. La constància és la clau.")
    elif "dieta" in resposta:
        print("Prefereixes una dieta alta en proteïnes o equilibrada?")
        tipus = input("> ").lower()
        if "proteïna" in tipus:
            print("Menja ous, pollastre i iogurt.")
        else:
            print("Dieta equilibrada: fruita, verdures i cereals integrals.")

    elif "press" in resposta or "banca" in resposta:
        try:
            pes = float(input("Quin és el teu pes corporal (en kg)? "))
            nivell = input("Nivell (principiant/intermig/avançat): ").lower()
            if "principiant" in nivell:
                recomanat = pes * 0.6
            elif "intermig" in nivell:
                recomanat = pes * 1.0
            elif "avançat" in nivell or "avanzado" in nivell:
                recomanat = pes * 1.3
            else:
                recomanat = pes * 1.0
            print(f"Et recomano començar amb uns {recomanat:.1f} kg al press banca.")
        except ValueError:
            print("Introdueix un número vàlid per al pes.")

    elif "sortir" in resposta or "adeu" in resposta:
        print(f"Adéu, {nom}. Continua treballant fort.")
        break

    else:
        print("No he entès això. Prova amb entrenament, dieta o press banca.")
            
