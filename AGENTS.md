# AGENTS.md

Pełne zasady pracy w tym repo są w [`CLAUDE.md`](CLAUDE.md). **Przeczytaj go przed każdą zmianą.** Obowiązują każdego agenta (Cursor, Claude, inne).

Najważniejsze w skrócie:

1. **Pracujemy tylko na gałęzi `main`.** Przed pracą `git pull`, po pracy commit i `git push` na `main`. To wersja robocza: push na `main` niczego nie publikuje. **Gałęzi `prod` (strona na żywo) nie wolno dotykać**: żadnego pusha, merge ani pull requesta do `prod`. Publikację robi wyłącznie Krzysztof.
2. **Czysty HTML + CSS.** Bez frameworków, npm, build stepu. Żadnych zewnętrznych skryptów, fontów, map, analityki, embedów.
3. **Wygląd strony jest zamrożony.** Nie zmieniaj kolorów, fontów, odstępów ani `css/styles.css` bez wyraźnej prośby. Nowe treści wstawiaj w istniejące sekcje i klasy.
4. **Tekst autorki zostaje słowo w słowo.** Nie parafrazuj, nie skracaj, nie poprawiaj stylu. Jeśli autorka dyktuje lub wkleja nowy tekst, wstaw go dokładnie tak, jak go podała (popraw tylko literówki, o które poprosi).
5. **Żółte fragmenty (klasa `todo`)** to teksty robocze i dane przykładowe, które nie są słowami autorki. Gdy autorka poda własny tekst albo zaakceptuje fragment, podmień treść i usuń klasę `todo` z tego elementu. Nowy tekst wymyślony przez agenta zawsze oznacz klasą `todo`.
6. **Język tekstów roboczych:** forma „Pani/Pan”, nigdy „Ty”. Zawód: „psycholog”, nigdy „psycholożka”. Bez obietnic („skuteczna terapia”, „gwarancja”, „pozbądź się lęku”).
7. **Nie wymyślaj faktów** (adresy, godziny, ceny, certyfikaty). Brakujące dane oznaczone są komentarzem `<!-- TODO: klientka … -->`. Po uzupełnieniu usuń komentarz i odhacz pozycję w `README.md`.
8. **Sekcja `#opinie` zostaje ukryta** (`hidden`). Nie generuj opinii.
9. **Zmieniając adres lub godziny**, popraw je też w JSON-LD w `<head>` pliku `index.html`.
10. **Nie publikuj** numeru konta bankowego ani prywatnego adresu e-mail.
