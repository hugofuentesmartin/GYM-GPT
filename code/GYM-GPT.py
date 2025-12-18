# GYM-GPT: el teu assistent del gimnàs 💪
# Aquest programa interactua amb l’usuari per parlar sobre entrenament, dieta, press banca i descans.

print("Hola! Soc GYM-GPT, el teu assistent del gimnàs.")
nom = input("Com et dius? ").strip().capitalize()
print(f"Encantat, {nom}. T’ajudaré amb el teu entrenament.")

while True:
    resposta = input(f"\nSobre què vols parlar, {nom}? (entrenament, dieta, press banca, descans, sortir)\n> ").lower().strip()

    if "sortir" in resposta or "adeu" in resposta or "adéu" in resposta:
        print(f"Adéu, {nom}. Continua treballant fort i cuida’t!")
        break

    if "entrenament" in resposta:
        print("Entrenar és essencial per progressar. Quin dia t’agrada més anar al gimnàs?")
        dia = input("> ").strip()

        if dia.lower() in ("sortir", "adeu", "adéu"):
            print(f"Adéu, {nom}. Continua treballant fort i cuida’t!")
            break

        print(f"Bona elecció! Els {dia} són perfectes per mantenir la constància. 💪")

    elif "dieta" in resposta:
        print("Prefereixes una dieta alta en proteïnes o més equilibrada?")
        tipus = input("> ").lower().strip()

        if tipus in ("sortir", "adeu", "adéu"):
            print(f"Adéu, {nom}. Continua treballant fort i cuida’t!")
            break

        if "proteïna" in tipus or "proteines" in tipus:
            print("Perfecte. Prioritza ous, pollastre, peix, llegums i iogurt grec.")
        else:
            print("Molt bé. Mantén un equilibri entre fruita, verdures, cereals integrals i proteïnes magres.")

    elif "press" in resposta or "banca" in resposta:
        try:
            pes = input("Quin és el teu pes corporal (en kg)? ").strip()

            if pes.lower() in ("sortir", "adeu", "adéu"):
                print(f"Adéu, {nom}. Continua treballant fort i cuida’t!")
                break

            pes = float(pes)

            nivell = input("Nivell (principiant/intermig/avançat): ").lower().strip()

            if nivell in ("sortir", "adeu", "adéu"):
                print(f"Adéu, {nom}. Continua treballant fort i cuida’t!")
                break

            if "principiant" in nivell:
                recomanat = pes * 0.6
            elif "intermig" in nivell:
                recomanat = pes * 1.0
            elif "avançat" in nivell or "avanzado" in nivell:
                recomanat = pes * 1.3
            else:
                recomanat = pes * 1.0
                print("No he reconegut el nivell, així que t’he posat com a intermig.")

            print(f"Et recomano començar amb uns {recomanat:.1f} kg al press banca.")
        except ValueError:
            print("Introdueix un número vàlid per al pes, si us plau.")

    elif "descans" in resposta:
        print("Dormir bé és tan important com entrenar. Quantes hores dorms normalment?")
        hores = input("> ").strip()

        if hores.lower() in ("sortir", "adeu", "adéu"):
            print(f"Adéu, {nom}. Continua treballant fort i cuida’t!")
            break

        try:
            hores = float(hores)
            if hores < 6:
                print("Necessites dormir més! El teu cos es recupera mentre descanses.")
            elif 6 <= hores <= 8:
                print("Perfecte! Un bon descans ajuda al creixement muscular i a evitar lesions.")
            else:
                print("Dormir massa també pot ser contraproduent. Mantén un equilibri.")
        except ValueError:
            print("Introdueix un número vàlid d’hores, si us plau.")

    else:
        print("No he entès això. Pots parlar d’entrenament, dieta, press banca, descans o escriure ‘sortir’ per acabar.")
