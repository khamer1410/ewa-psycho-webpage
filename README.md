# Strona psychoterapeutki — instrukcja

Statyczna strona internetowa: strona główna (`index.html`) i dwie podstrony (`kwalifikacje.html`, `pierwsza-wizyta.html`). Nie wymaga bazy danych, PHP, WordPressa ani instalowania czegokolwiek. Działa po wrzuceniu plików na dowolny hosting, a także po otwarciu `index.html` bezpośrednio z dysku.

Strona nie używa cookies, analityki ani zewnętrznych skryptów i fontów (wszystko jest w tym folderze). Nie ma też formularza kontaktowego, kontakt odbywa się telefonicznie lub mailowo.

## Co jest w folderze

| Plik / folder | Do czego służy |
|---|---|
| `index.html` | Strona główna (wszystkie sekcje: O mnie, Jak pracuję, Oferta, Cennik, Gabinety, Kontakt…). |
| `kwalifikacje.html` | Podstrona „Kwalifikacje”: pełne bio, certyfikaty (lista i galeria skanów), szkolenia. |
| `pierwsza-wizyta.html` | Podstrona „Pierwsza wizyta”: pierwsze spotkania, zasady współpracy (kontrakt), poufność. |
| `css/styles.css` | Wygląd strony (kolory, odstępy, układ na telefonie i komputerze). |
| `css/fonts.css` | Podpięcie fontów z folderu `fonts/`. |
| `fonts/` | Fonty Newsreader i Lato (pliki `.woff2`, z polskimi znakami). |
| `js/nav.js` | Menu rozwijane na telefonie (przycisk z trzema kreskami). |
| `img/` | Zdjęcia (na razie brak) oraz mapa sekcji Gabinety (`mapa-warszawa.webp` i jej parametry w `mapa-warszawa.json`). |
| `img/certyfikaty/` | Skany dyplomów i certyfikatów (WebP) do galerii na podstronie „Kwalifikacje”. |
| `scripts/make-map.py` | Skrypt generujący mapę z OpenStreetMap (uruchamiany ręcznie, tylko przy zmianie adresu). |
| `favicon.svg` | Ikonka w karcie przeglądarki (litera „E”). |
| `robots.txt` | Informacja dla wyszukiwarek, że stronę można indeksować. |
| `sitemap.xml` | Mapa strony dla wyszukiwarek (strona główna i obie podstrony). |

## Jak opublikować stronę

Przed publikacją uzupełnij dane z listy poniżej („Do uzupełnienia”).

**Opcja A: zwykły hosting (FTP)**
1. Połącz się z serwerem programem FTP (np. FileZilla), danymi od firmy hostingowej.
2. Wejdź do katalogu publicznego (zwykle `public_html`, `www` lub `htdocs`).
3. Skopiuj tam **całą zawartość** tego folderu (nie sam folder), tak aby `index.html` leżał bezpośrednio w katalogu publicznym.
4. Nie trzeba kopiować folderu `.git` ani pliku `README.md`.

**Opcja B: Netlify (za darmo, bez FTP)**
1. Załóż konto na netlify.com.
2. Wejdź w „Sites” i przeciągnij cały ten folder na pole „Drag and drop your site output folder here”.
3. Po chwili strona będzie dostępna pod adresem `*.netlify.app`. Własną domenę podpina się w „Domain settings”.

## Do uzupełnienia (checklista)

**Żółte fragmenty na stronie.** Klasa `todo` (żółte tło, kursywa) oznacza tekst roboczy, który nie jest Pani słowami. Treść strony została zweryfikowana i wszystkie żółte oznaczenia zdjęto; klasa zostaje do oznaczania nowych propozycji.

Każde miejsce do zmiany jest w plikach oznaczone komentarzem `TODO: klientka`. Najprościej wyszukać w edytorze tekstu frazę `TODO`.

**Do potwierdzenia lub dostarczenia przez klientkę**
- [ ] Telefon: czy numer +48 502 733 097 (podany przy BLIK-u) jest też numerem kontaktowym. Występuje w sekcji powitalnej, w Kontakcie, w JSON-LD (`"telephone"`) i na obu podstronach.
- [ ] Certyfikat Polskiej Rady Psychoterapii: po otrzymaniu wpisać rok i numer w `kwalifikacje.html` (teraz „w trakcie”) i dodać skan do galerii.
- [ ] Faktura: w cenniku źródłowym jest „faktura lub rachunek imienny”, w kontrakcie tylko rachunek. Na stronie jest tylko rachunek imienny; jeśli wystawiane są też faktury, dopisać.
- [ ] Adresy gabinetów: wpisane ul. Łucka 18, 00-845 i ul. Gagarina 17, 00-753 (kody pocztowe z OpenStreetMap). Jeśli trzeba, dopisać numer lokalu.
- [ ] Mapa: po podaniu dokładnych adresów przegenerować ją skryptem i przekleić pozycje pinezek (opis w „Gabinety i mapa”).
- [ ] Opinie: 3 cytaty, tylko jeśli sekcja ma być widoczna (opis poniżej).
- [ ] Obrazek do udostępniania (`og-image.png`, 1200×630 px): plik trzeba przygotować i wrzucić do głównego folderu; na razie go nie ma.

**Domena i e-mail**
- [ ] Kupić domenę `ewahamerszmit.pl`. Adres jest już wpisany w `canonical`, `og:url`, `og:image` i JSON-LD na wszystkich trzech stronach oraz w `robots.txt` i `sitemap.xml`.
- [ ] Ustawić skrzynkę lub przekierowanie `kontakt@ewahamerszmit.pl` na prywatną skrzynkę Gmail. Ten adres jest na stronie głównej (Kontakt, JSON-LD) i w `pierwsza-wizyta.html` (rachunek imienny). Prywatny adres Gmail celowo nie jest publikowany.

**Świadomie nie na stronie**
- Numer rachunku bankowego. W treści jest „przelewem na rachunek podany po pierwszej sesji”. Numeru nie należy dopisywać do żadnego pliku w tym folderze (repozytorium jest publiczne).

## Podstrony

Menu u góry jest takie samo na wszystkich stronach i prowadzi do sekcji strony głównej (`index.html#…`). Do podstron prowadzą linki w treści i w stopce:

- **`kwalifikacje.html` („Kwalifikacje”)**: pełny tekst o wykształceniu i doświadczeniu, lista certyfikatów z galerią skanów, lista szkoleń. Link „Pełne wykształcenie, szkolenia i certyfikaty” na końcu sekcji O mnie na stronie głównej oraz w stopce.
- **`pierwsza-wizyta.html` („Pierwsza wizyta”)**: pełny opis pierwszych spotkań, zasady współpracy (czas sesji, ceny, umawianie, płatności, rachunek, częstotliwość, odwołania, kodeks etyczny, superwizja) i poufność z wyjątkami. Linki pod krokami „Pierwsza wizyta” i pod cennikiem na stronie głównej oraz w stopce.

Każda podstrona ma własny tytuł, opis i adres kanoniczny w `<head>`. Przy zmianie cen trzeba je poprawić w trzech miejscach: cennik na stronie głównej, JSON-LD w `index.html` i sekcja „Zasady współpracy” w `pierwsza-wizyta.html`.

**Galeria certyfikatów** (w `kwalifikacje.html`): każda miniatura to link do pliku w `img/certyfikaty/`, który otwiera skan w nowej karcie. Aby dodać nowy skan (np. certyfikat PRP): **nigdy nie wrzucać PDF-a do repo**, bo repozytorium jest publiczne, a w PDF-ie zakrycia bywają osobną warstwą, którą da się zdjąć. Zamienić PDF na obraz (np. `qlmanage -t -s 1600 -o /tmp plik.pdf`, potem `cwebp -q 80 -metadata none plik.png -o img/certyfikaty/nazwa.webp`), obejrzeć wynik i dodać miniaturę jak pozostałe, z prawdziwymi `width` i `height`.

## Gabinety i mapa

Sekcja z gabinetami (nagłówek „KONTAKT”, między Cennikiem a pasem kontaktu; prowadzi do niej link „Kontakt” w menu) pokazuje dwa gabinety w Warszawie i spotkania online: mapę z dwiema pinezkami oraz trzy karty z adresem. Dni i godzin przyjęć celowo nie podajemy (terminy ustalane przy pierwszym kontakcie).

**Co podmienić w `index.html`** (miejsca oznaczone `TODO: klientka`):
- te same dane w JSON-LD w `<head>` (blok `"location"`): adres i współrzędne (`"geo"`).
- Linki „Jak dojechać” prowadzą do wyszukiwania ulicy w Google Maps. Po wpisaniu numeru można go dodać do adresu w linku (np. `query=ul.%20%C5%81ucka%2012%2C%20Warszawa`).

**Mapa** to zwykły obrazek (`img/mapa-warszawa.webp`, 1200×900 px) wygenerowany raz z kafelków OpenStreetMap. Strona nie łączy się z żadnym serwerem map, nie ma Google Maps ani cookies. Pinezki to elementy HTML nałożone na obrazek; ich położenie zapisane jest w procentach w atrybucie `style="--x:..%;--y:..%"`. Podpis „© OpenStreetMap contributors” pod mapą jest wymagany licencją OSM i nie wolno go usuwać.

**Jak przegenerować mapę po zmianie adresu:**
1. Ustal współrzędne budynku (np. na openstreetmap.org: prawy przycisk myszy na budynku → „Pokaż adres”, współrzędne pojawią się w panelu).
2. W pliku `scripts/make-map.py`, w sekcji „Konfiguracja”, zmień `lat` i `lon` w liście `PINS`.
3. Uruchom z głównego folderu: `python3 scripts/make-map.py` (wymaga Pythona 3 i biblioteki Pillow: `python3 -m pip install pillow`; na macOS z Homebrew najprościej w środowisku wirtualnym: `python3 -m venv .venv && .venv/bin/pip install pillow && .venv/bin/python scripts/make-map.py`, folder `.venv` usuń po użyciu).
4. Skrypt nadpisze `img/mapa-warszawa.webp` i `img/mapa-warszawa.json`, a w terminalu wypisze gotowe wartości `--x`/`--y`. Przeklej je do atrybutów `style` obu pinezek (`<a class="pin" ...>`) w `index.html`.
5. Te same współrzędne wpisz w JSON-LD (`"geo"`).

Jeśli gabinety będą bardzo daleko od siebie, skrypt ostrzeże, że pinezki się nie mieszczą; wtedy zmniejsz `ZOOM` o 1.

## Jak dodać zdjęcia

Na stronie jest jedno zdjęcie: portret w sekcji powitalnej strony głównej (`img/portret-hero.webp`, pion 4:5, 1000 × 1250 px). Puste miejsce na drugie zdjęcie w sekcji „O mnie” zostało usunięte, a podstrona „Kwalifikacje” nie ma nagłówka ze zdjęciem.

Nowe zdjęcie: format WebP, skompresowany do ok. 200–400 KB (np. w squoosh.app), w folderze `img/`, z atrybutami `width`, `height` i `alt` w kodzie.

## Sekcja Opinie

Sekcja z opiniami pacjentów jest gotowa, ale **celowo ukryta**. Kodeksy etyczne psychoterapeutów są sceptyczne wobec publikowania opinii pacjentów, dlatego warto ją włączać tylko przy pisemnych zgodach.

Aby ją pokazać: w `index.html` znajdź `<section id="opinie" ... hidden>` i usuń słowo `hidden`. Następnie podmień trzy przykładowe cytaty i podpisy. Jeśli ma się pojawić również w menu, dodaj do listy linków `<li><a href="#opinie">Opinie</a></li>`.

## SEO (widoczność w Google)

Strona ma **podstawowe** ustawienia SEO: tytuł i opis strony, adres kanoniczny, dane do udostępniania (Open Graph), mapę strony oraz dane strukturalne (JSON-LD) z adresami obu gabinetów, telefonem i cennikiem. Imię i nazwisko, telefon, adresy, ceny, certyfikaty i członkostwa są już prawdziwe; e-mail (domena) to nadal wartość przykładowa.

Po wpisaniu prawdziwych danych warto dopracować:
- tytuł i opis strony o frazy lokalne (np. dzielnica Warszawy, „psychoterapeuta Mokotów”, „terapia traumy Warszawa”),
- profil firmy w Google (Google Business Profile) z tym samym adresem i telefonem co na stronie,
- prawdziwy obrazek `og-image.png`,
- zgłoszenie strony i `sitemap.xml` w Google Search Console.

## Zmiany wyglądu

Kolory są zebrane na początku pliku `css/styles.css` (sekcja „Tokeny”), np. `--teal: #3F7F86;` to główny kolor morski. Zmiana wartości w jednym miejscu zmienia kolor na całej stronie.
