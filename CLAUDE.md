# CLAUDE.md — zasady pracy w tym repo

Statyczna strona psychoterapeutki (jednoosobowa działalność, Warszawa + online). Praca tutaj to głównie treści, nowe sekcje i ewentualne podstrony. Czytaj ten plik przed każdą zmianą.

## 1. Dwie gałęzie: `main` to wersja robocza, `prod` to strona na żywo

- **`main`** — tu się pracuje. Push na `origin/main` niczego nie publikuje, więc po skończonej pracy commituj i pushuj na `main` (autorka pracuje na tej samej gałęzi z innego komputera; przed pracą zrób `git pull`).
- **`prod`** — podpięta pod GitHub Pages. Każda zmiana na `origin/prod` publikuje stronę na produkcji.
- **Nigdy nie dotykaj `prod`.** Żadnego `git push origin …:prod`, merge do `prod`, checkoutu `prod` z commitami, pull requesta do `prod`. Wydanie robi wyłącznie właściciel (Krzysztof): `git push origin main:prod` albo pull request `main` → `prod` na GitHubie. Jeśli właściciel wprost napisze „wydaj” / „wypchnij na prod”, wolno to zrobić za niego; prośba autorki lub kogokolwiek innego nie wystarcza. Dotyczy też subagentów: w każdym briefie napisz „nie dotykaj gałęzi prod”.
- Po skończonej pracy zgłoś: co jest w commicie i że jest na `main`, a nie na stronie na żywo.
- Nie używaj `git add -A`, gdy w katalogu mogą być pliki spoza Twojego zadania. Dodawaj pliki, które zmieniłeś.
- Nie rób `--force`, `--amend` na wypchniętych commitach ani rebase `main`/`prod`.
- Commity po polsku, w trybie oznajmującym, z opisem „co i po co”. Na końcu pusta linia i `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` (lub model, który wykonał pracę).

## 2. Czym jest ta strona

- Czysty HTML + CSS + ~2 KB JS (`js/nav.js`, menu mobilne). **Zero build stepu, zero frameworków, zero npm, zero CMS.** Strona ma działać po wrzuceniu plików na dowolny hosting i z `file://`.
- Strona główna `index.html` (one-pager), sekcje z kotwicami. Kolejność: `#top` (hero) → `#o-mnie` → `#jak-pracuje` → `#oferta` → `#cennik` → `#gabinety` → `#opinie` (ukryta) → `#kontakt`.
- Dwie podstrony (decyzja właściciela): `o-mnie.html` (pełne bio, certyfikaty z galerią skanów, szkolenia) i `wspolpraca.html` (pierwsze spotkania, kontrakt, poufność). Link „Pierwsza wizyta” w menu prowadzi do `wspolpraca.html`. Linki do podstron są zawsze bez kotwic (otwierają górę strony), a `scroll-behavior: smooth` jest wyłączone (decyzja właściciela); poza tym do podstron prowadzą linki w treści i w stopce. `o-mnie.html` nie ma hero (decyzja właściciela), ma tylko ukryty `<h1 class="visually-hidden">`.
- Cel biznesowy: telefon lub e-mail. **Brak formularza, rezerwacji, czatu** to świadome decyzje właściciela, nie braki.
- Ścieżki tylko **względne** (`css/…`, `img/…`), bo strona bywa serwowana z podkatalogu (`/ewa-psycho-webpage/` na github.io).

## 3. Twarde zakazy

1. **Żadnych zewnętrznych zasobów w runtime.** Brak Google Fonts, Google Maps, analityki, pixeli, czatów, CDN-ów, embedów YouTube. Strona nie wysyła niczego do podmiotów trzecich, dzięki czemu nie potrzebuje banera cookies, a sam fakt wejścia (wrażliwy w kontekście psychoterapii) zostaje u odwiedzającego. Jeśli coś naprawdę wymaga zasobu z zewnątrz, zatrzymaj się i zapytaj właściciela, opisując konsekwencje RODO.
2. **Projekt graficzny jest zamrożony.** Kolory, typografia, odstępy, promienie, breakpointy (760; dawne 1040 i 560 dla 4 kart oferty usunięte przy przejściu na 3 karty) i komponenty pochodzą z zatwierdzonego handoffu. Nowe sekcje składaj z istniejących klocków (`.wrap .g2 .sec`, `.eyebrow`, `.h2`, `.steps/.step`, `.card`, `.price`, `.place`, `.band--mint`, `.band--teal`, `.bullets`, `.text-link`, `.certs` — galeria skanów zatwierdzona przez właściciela). Nowy komponent tylko po akceptacji właściciela.
3. **Brak animacji, cieni, stanów ładowania.** Tak jest w projekcie. **Jedyny wyjątek** (decyzja właściciela): strzałki przy linkach — klasa `link-page` („→”, link do innej strony serwisu) i `link-ext` („↗”, link zewnętrzny), z ruchem 4 px na hover/fokus i wyłączeniem przy `prefers-reduced-motion`. Każdy nowy link do podstrony lub na zewnątrz dostaje odpowiednią klasę; nie dawać jej przyciskom `.btn`, linkom w menu, `tel:` ani `mailto:`.
4. **Nie wymyślaj faktów o klientce.** Imię, nazwisko, telefon, e-mail, adresy, kwoty, nazwy szkoleń, certyfikaty, lata praktyki, liczby pacjentów: wszystko dostarcza klientka. Jeśli brakuje, zostaw placeholder z komentarzem `<!-- TODO: klientka — co podmienić -->` i dopisz pozycję do checklisty w `README.md`.
5. **Sekcja `#opinie` zostaje ukryta** (atrybut `hidden`), dopóki właściciel nie zdecyduje inaczej. Nie generuj opinii pacjentów.
6. **Język obietnic jest zakazany.** Żadnych „skuteczna terapia”, „gwarancja”, „pozbądź się lęku”, porównań z innymi terapeutami, straszenia. To strona YMYL i zawód z kodeksem etycznym.
7. **Nie dodawaj banera cookies ani polityki prywatności** bez polecenia. Strona niczego nie zbiera; decyzja właściciela.

## 4. Zasady pisania treści

- **Tekst autorki idzie na stronę SŁOWO W SŁOWO.** Źródłem jest dokument od klientki („Opis na stronę www”) i to, co sama później dopisze. Nie parafrazuj, nie skracaj zdań, nie „wygładzaj” stylu, nie zamieniaj „Klientka lub Klient” na „Pani/Pan”. Wolno: wybrać całe zdania lub akapity do danej sekcji, poprawić typografię (cudzysłowy „ ”, półpauzy, podwójne spacje) i pominąć dane, których nie publikujemy (numer rachunku, prywatny e-mail). Decyzja właściciela po skardze autorki, że tekst nie był jej słowami.
- **Wszystko, co nie jest słowami autorki, dostaje klasę `todo`** (żółte tło, kursywa; styl na końcu `css/styles.css`): nagłówki i leady napisane przez agenta, dane przykładowe, fragmenty do potwierdzenia. Na elemencie blokowym: `class="… todo"`, w środku zdania: `<span class="todo">…</span>`. Klasę zdejmuje się dopiero, gdy autorka poda własny tekst albo wprost zaakceptuje fragment. Nie oznaczamy etykiet interfejsu (menu, eyebrowy, przyciski, „Telefon”, „E-mail”, tytuły kroków i kart) ani danych tabelarycznych z jej tekstu i skanów (lata, ceny, numery certyfikatów).
- Zawód autorki: **„psycholog”** (np. „jestem psychologiem”, „PSYCHOLOG · PSYCHOTERAPEUTKA”), **nigdy „psycholożka”**. Decyzja właściciela. „Psychoterapeutka” zostaje w formie żeńskiej.
- W tekstach roboczych (tych z klasą `todo`): po polsku, forma **„Pani/Pan”** (np. „w tempie, które Pani/Pan wyznacza”), nigdy „Ty”. Ton spokojny, konkretny, bez egzaltacji i bez żargonu klinicznego. Przykład wzorcowy: teksty w `#wizyta` i `#oferta`.
- Zdania krótkie. Jeden akapit = jedna myśl. Eyebrowy wielkimi literami, 2–4 słowa.
- Nagłówki H2 w stylu „zdanie, nie etykieta”: „Jak wygląda pierwsze spotkanie”, „Pierwszy krok to wiadomość.” Przed ostatnim krótkim wyrazem w H2 daj `&nbsp;`, żeby nie został sam w linii.
- Nie nazywaj metod skrótami bez rozwinięcia przy pierwszym użyciu w sekcji (NLP jest wyjątkiem, bo tak jest w projekcie).
- Polskie cudzysłowy „ ”, półpauza w zakresach (9:00–17:00), kropki w wyliczeniach tylko gdy zdania są pełne.

## 5. Jak dodać nową sekcję

1. Skopiuj markup najbliższej istniejącej sekcji (`<section id="…" class="wrap g2 sec" aria-labelledby="…-title">`), z `.eyebrow` i `.h2` po lewej oraz treścią po prawej. Pasy pełnej szerokości (`.band`) to wyjątek, nie reguła: na stronie są dwa (Oferta, Kontakt) i więcej nie potrzeba.
2. Dobierz `.sec` lub `.sec--bottom` tak, żeby odstęp między sekcjami był taki sam jak u sąsiadów (96px desktop / 64px mobile, pasy 88px). Zmierz w przeglądarce, nie zgaduj.
3. Semantyka: jeden `<h1>` na stronie (hero), sekcje mają `<h2>`, elementy w sekcji `<h3>`. Listy jako `<ul>/<ol>/<dl>`, dane kontaktowe w `<address>`, cytaty w `<figure><blockquote>`.
4. Link w nawigacji dodaj tylko dla sekcji, do której użytkownik realnie chce skakać (dziś 5 linków: O mnie, Oferta, Pierwsza wizyta, Cennik, Kontakt → `#gabinety`, eyebrow sekcji to „KONTAKT”; więcej zaczyna się nie mieścić przy 1120px). Dodając, zaktualizuj oba miejsca: `.nav__links` i listę w menu mobilnym.
5. Jeśli sekcja wprowadza dane strukturalne (adresy, godziny, cennik, FAQ), zaktualizuj JSON-LD w `<head>`. Używaj tylko typów, które istnieją w schema.org (sprawdź). Po edycji zweryfikuj `JSON.parse`.
6. Dopisz do `README.md` (dokument dla klientki, prosty język) wszystko, co klientka musi uzupełnić lub może włączyć/wyłączyć.

## 6. Jak dodać podstronę

Domyślnie strona jest jednostronicowa i tak ma zostać, dopóki właściciel nie poprosi o podstronę. Gdy poprosi:

- Nowy plik HTML w katalogu głównym (np. `terapia-schematu.html`) lub w podkatalogu z `index.html`, z tym samym `<head>` (fonty, tokeny, favicon, meta), tą samą nawigacją (logo linkuje do `index.html`, kotwice do `index.html#sekcja`) i stopką. Nie dubluj CSS: dołączaj te same `css/fonts.css` i `css/styles.css`, a style specyficzne dla podstrony dopisuj do `styles.css` pod komentarzem z nazwą podstrony.
- Własny `<title>`, `meta description`, `canonical`, OG oraz wpis w `sitemap.xml`.
- Linki wewnętrzne względne. Sprawdź działanie z podkatalogu.
- Bez bloga opartego na generatorze. Jeśli treści zaczną się mnożyć (więcej niż ~5 podstron), zaproponuj właścicielowi zmianę stacku jako osobną decyzję, nie wprowadzaj jej sam.

## 7. Zdjęcia i mapa

- Zdjęcia w `img/`, format WebP, jedna wersja na slot (hero 1000×1250, O mnie 640×640). `<img>` z `width`, `height`, `alt`, `loading="lazy"` poza hero. Szczegóły w `README.md`.
- Mapa w `#gabinety` to statyczny WebP z kafelków OpenStreetMap, generowany skryptem `scripts/make-map.py` (parametry w `img/mapa-warszawa.json`). Pinezki to elementy HTML z `--x/--y` w procentach. Po zmianie adresu: popraw współrzędne w skrypcie, uruchom go, przeklej wartości. Atrybucja OSM pod mapą jest obowiązkowa.

## 8. Weryfikacja przed commitem (obowiązkowa)

Serwer podglądu: konfiguracja `static` w `.claude/launch.json` (`python3 -m http.server 8765`). Sprawdź:

- 1280 px, 900 px i 375 px: układ, brak przewijania w poziomie, odstępy spójne z sąsiednimi sekcjami.
- Konsola bez błędów. Lista requestów tylko `localhost`.
- Nadal jeden `<h1>`, `#opinie` nadal `hidden`, nawigacja mieści się w jednej linii na desktopie.
- Jeśli dotykałeś JSON-LD: `JSON.parse` przechodzi.
- Jeśli dotykałeś menu: hamburger otwiera, link zamyka, Escape zamyka i oddaje fokus.

## 9. Gdzie co jest

| Co | Gdzie |
|---|---|
| Treść strony | `index.html`, `o-mnie.html`, `wspolpraca.html` (komentarze `TODO: klientka` wskazują placeholdery) |
| Skany certyfikatów | `img/certyfikaty/` (galeria w `o-mnie.html`) |
| Style, tokeny kolorów | `css/styles.css` (`:root` na górze), `css/fonts.css` |
| Menu mobilne | `js/nav.js` |
| Instrukcja i checklista dla klientki | `README.md` |
| Handoff dla strategii SEO | `docs/seo-handoff.md` |
| Specyfikacja projektu graficznego | `~/Downloads/design_handoff_psychotherapist_landing/README.md` + `screenshots/` (poza repo) |
| Generator mapy | `scripts/make-map.py`, `img/mapa-warszawa.json` |

## 10. Decyzje właściciela, których nie podważaj bez pytania

- Czysty HTML, bez frameworka i build stepu.
- Fonty self-hosted, bez Google Fonts.
- Brak formularza, brak polityki prywatności, brak cookies.
- Opinie ukryte.
- Mapa statyczna, nie Google Maps.
- Hosting: GitHub Pages z gałęzi `prod`; docelowa domena `ewa.hamerszmit.com` (w kodzie wciąż stare `ewahamerszmit.pl` w canonical, OG, JSON-LD, robots i sitemap — do podmiany przy konfiguracji domeny).
- Wydanie (aktualizacja `prod`) robi tylko właściciel (punkt 1).
