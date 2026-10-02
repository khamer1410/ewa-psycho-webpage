# Strona psychoterapeutki — instrukcja

Jednostronicowa, statyczna strona internetowa. Nie wymaga bazy danych, PHP, WordPressa ani instalowania czegokolwiek. Działa po wrzuceniu plików na dowolny hosting, a także po otwarciu `index.html` bezpośrednio z dysku.

Strona nie używa cookies, analityki ani zewnętrznych skryptów i fontów (wszystko jest w tym folderze). Nie ma też formularza kontaktowego, kontakt odbywa się telefonicznie lub mailowo.

## Co jest w folderze

| Plik / folder | Do czego służy |
|---|---|
| `index.html` | Cała treść strony. Tu wpisuje się dane klientki. |
| `css/styles.css` | Wygląd strony (kolory, odstępy, układ na telefonie i komputerze). |
| `css/fonts.css` | Podpięcie fontów z folderu `fonts/`. |
| `fonts/` | Fonty Newsreader i Figtree (pliki `.woff2`, z polskimi znakami). |
| `js/nav.js` | Menu rozwijane na telefonie (przycisk z trzema kreskami). |
| `img/` | Zdjęcia (na razie brak) oraz mapa sekcji Gabinety (`mapa-warszawa.webp` i jej parametry w `mapa-warszawa.json`). |
| `scripts/make-map.py` | Skrypt generujący mapę z OpenStreetMap (uruchamiany ręcznie, tylko przy zmianie adresu). |
| `favicon.svg` | Ikonka w karcie przeglądarki (litera „A”). |
| `robots.txt` | Informacja dla wyszukiwarek, że stronę można indeksować. |
| `sitemap.xml` | Mapa strony dla wyszukiwarek. |

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

Każde miejsce do zmiany jest w plikach oznaczone komentarzem `TODO: klientka`. Najprościej wyszukać w edytorze tekstu frazę `TODO`.

**`index.html`**
- [ ] Imię i nazwisko: tytuł strony (`<title>`), `og:title`, logo w nawigacji, stopka, JSON-LD (`"name"`).
- [ ] Telefon: przycisk w sekcji powitalnej i sekcja Kontakt. Zmień zarówno widoczny tekst, jak i `href="tel:+48..."` (bez spacji). Również w JSON-LD (`"telephone"`).
- [ ] E-mail: sekcja Kontakt (tekst i `href="mailto:..."`) oraz JSON-LD (`"email"`).
- [ ] Adresy gabinetów (Wola, ul. Łucka i Mokotów, ul. Sielecka): numer budynku/lokalu i kod pocztowy w kartach sekcji Gabinety (obecnie `00/0` i `00-000`), krótki zapis w sekcji Kontakt oraz JSON-LD (`"location"` → `"streetAddress"`, `"postalCode"`).
- [ ] Dni i godziny przyjęć: 3 karty w sekcji Gabinety (obecnie przykładowe) oraz JSON-LD (`"openingHoursSpecification"`: `"dayOfWeek"`, `"opens"`, `"closes"`).
- [ ] Platforma spotkań online (Google Meet, Zoom lub inna): karta „Online” w sekcji Gabinety.
- [ ] Mapa: po podaniu dokładnych adresów przegenerować ją skryptem i przekleić pozycje pinezek (opis w „Gabinety i mapa”).
- [ ] Wykształcenie i szkolenia: 4 pozycje (rok i nazwa), sekcja O mnie. Można dodać lub usunąć pozycje, kopiując parę `<dt>rok</dt><dd>opis</dd>`.
- [ ] Ceny: 3 kwoty w sekcji Cennik oraz te same kwoty w JSON-LD (`"price"`) i `"priceRange"`.
- [ ] Zdjęcia: 2 portrety (opis poniżej).
- [ ] Opinie: 3 cytaty, tylko jeśli sekcja ma być widoczna (opis poniżej).
- [ ] Domena: zamień `https://example.pl/` na prawdziwy adres w `<link rel="canonical">`, `og:url`, `og:image` i JSON-LD (`"url"`).
- [ ] Obrazek do udostępniania (`og-image.png`, 1200×630 px): pojawia się przy wklejaniu linku na Facebooku czy w komunikatorach. Plik trzeba przygotować i wrzucić do głównego folderu; na razie go nie ma.

**`robots.txt`**
- [ ] Zamień `example.pl` na prawdziwą domenę.

**`sitemap.xml`**
- [ ] Zamień `example.pl` na prawdziwą domenę.

## Gabinety i mapa

Sekcja „Gabinety” (między Cennikiem a Kontaktem) pokazuje dwa gabinety w Warszawie i spotkania online: mapę z dwiema pinezkami oraz trzy karty z adresem, dniami i godzinami.

**Co podmienić w `index.html`** (miejsca oznaczone `TODO: klientka`):
- numery budynków/lokali i kody pocztowe w kartach (`ul. Łucka 00/0, 00-000 Warszawa`, `ul. Sielecka 00/0, 00-000 Warszawa`),
- dni i godziny w każdej karcie (format: małe litery, zakres z półpauzą, np. `poniedziałek, środa` / `9:00–17:00`),
- platformę w karcie „Online”,
- te same dane w JSON-LD w `<head>` (blok `"location"`): adres, współrzędne (`"geo"`) i godziny (`"openingHoursSpecification"`, dni po angielsku, np. `https://schema.org/Monday`, godziny w formacie `09:00`).
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

Na stronie są dwa miejsca na zdjęcia, na razie wypełnione jednolitym beżowym tłem.

| Miejsce | Nazwa pliku | Proporcje | Minimalny rozmiar |
|---|---|---|---|
| Sekcja powitalna (u góry) | `img/portret-hero.jpg` | pion 4:5 | 1200 × 1500 px |
| Sekcja O mnie | `img/portret-o-mnie.jpg` | kwadrat 1:1 | 800 × 800 px |

Format: JPG lub WebP, najlepiej skompresowany do ok. 200–400 KB (np. w squoosh.app).

1. Wrzuć zdjęcia do folderu `img/` pod nazwami z tabeli. Jeśli używasz innej nazwy lub formatu WebP, zmień ją także w `src="..."`.
2. W `index.html` znajdź komentarz `<!-- <img src="img/portret-hero.jpg" ...> -->` i usuń znaki `<!--` na początku oraz `-->` na końcu tej linii. To samo zrób dla `portret-o-mnie.jpg`.
3. Jeśli zdjęcie ma inne wymiary niż w tabeli, popraw atrybuty `width` i `height` na rzeczywiste (zapobiega to „skakaniu” strony podczas ładowania).
4. Sprawdź opis w atrybucie `alt` (np. „Anna Kowalska, psychoterapeutka, portret”) i wpisz prawdziwe imię i nazwisko.

## Sekcja Opinie

Sekcja z opiniami pacjentów jest gotowa, ale **celowo ukryta**. Kodeksy etyczne psychoterapeutów są sceptyczne wobec publikowania opinii pacjentów, dlatego warto ją włączać tylko przy pisemnych zgodach.

Aby ją pokazać: w `index.html` znajdź `<section id="opinie" ... hidden>` i usuń słowo `hidden`. Następnie podmień trzy przykładowe cytaty i podpisy. Jeśli ma się pojawić również w menu, dodaj do listy linków `<li><a href="#opinie">Opinie</a></li>`.

## SEO (widoczność w Google)

Strona ma **podstawowe** ustawienia SEO: tytuł i opis strony, adres kanoniczny, dane do udostępniania (Open Graph), mapę strony oraz dane strukturalne (JSON-LD) z adresami obu gabinetów, godzinami, telefonem i cennikiem. Wszystkie te wartości są teraz przykładowe.

Po wpisaniu prawdziwych danych warto dopracować:
- tytuł i opis strony o frazy lokalne (np. dzielnica Warszawy, „psychoterapeuta Mokotów”, „terapia traumy Warszawa”),
- profil firmy w Google (Google Business Profile) z tym samym adresem i telefonem co na stronie,
- prawdziwy obrazek `og-image.png`,
- zgłoszenie strony i `sitemap.xml` w Google Search Console.

## Zmiany wyglądu

Kolory są zebrane na początku pliku `css/styles.css` (sekcja „Tokeny”), np. `--teal: #3F7F86;` to główny kolor morski. Zmiana wartości w jednym miejscu zmienia kolor na całej stronie.
