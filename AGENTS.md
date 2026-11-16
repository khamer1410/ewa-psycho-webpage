# AGENTS.md

Pełne zasady pracy w tym repo są w [`CLAUDE.md`](CLAUDE.md). **Przeczytaj go przed każdą zmianą.** Obowiązują każdego agenta (Cursor, Claude, inne).

Najważniejsze w skrócie:

1. **Push na `main` = publikacja strony na produkcji.** Commituj lokalnie. Nie rób `git push` bez wyraźnej zgody użytkownika w czacie. Przed pushem pokaż, co się zmieniło.
2. **Czysty HTML + CSS.** Bez frameworków, npm, build stepu. Żadnych zewnętrznych skryptów, fontów, map, analityki, embedów.
3. **Wygląd strony jest zamrożony.** Nie zmieniaj kolorów, fontów, odstępów ani `css/styles.css` bez wyraźnej prośby. Nowe treści wstawiaj w istniejące sekcje i klasy.
4. **Język:** forma „Pani/Pan”, nigdy „Ty”. Zawód: „psycholog”, nigdy „psycholożka”. Bez obietnic („skuteczna terapia”, „gwarancja”, „pozbądź się lęku”).
5. **Nie wymyślaj faktów** (adresy, godziny, ceny, certyfikaty). Brakujące dane oznaczone są komentarzem `<!-- TODO: klientka … -->`. Po uzupełnieniu usuń komentarz i odhacz pozycję w `README.md`.
6. **Sekcja `#opinie` zostaje ukryta** (`hidden`). Nie generuj opinii.
7. **Zmieniając adres lub godziny**, popraw je też w JSON-LD w `<head>` pliku `index.html`.
8. **Nie publikuj** numeru konta bankowego ani prywatnego adresu e-mail.
