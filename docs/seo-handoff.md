# Handoff: strategia SEO dla strony psychoterapeutki

Dokument dla agenta lub osoby, która ma przygotować strategię SEO i rekomendacje on-page. Strona już istnieje, jest statyczna i ma zamrożony projekt graficzny. Zadaniem jest strategia i konkretne zmiany w treści, metadanych i ekosystemie wokół strony, nie przebudowa.

## 1. Co to za strona

- Jednostronicowy serwis osobisty psychoterapeutki prowadzącej jednoosobową działalność w Warszawie.
- Nurt: terapia schematu, praca z traumą, narzędzia NLP, konsultacje. Pacjenci dorośli. Spotkania stacjonarne w dwóch gabinetach (Wola, ul. Łucka; Mokotów, ul. Sielecka) oraz online.
- Cel biznesowy: kontakt telefoniczny lub mailowy. Nie ma formularza, koszyka ani rezerwacji online. To świadoma decyzja.
- Język: polski. Ton: spokojny, forma „Pani/Pan”, bez obietnic wyleczenia.
- Imię i nazwisko klientki: Ewa Hamerszmit (w kodzie nadal placeholder „Anna Kowalska”). Planowana domena: `ewahamerszmit.pl` (wolna, jeszcze nie kupiona).

## 2. Stan techniczny

- Repozytorium: `github.com/khamer1410/ewa-psycho-webpage`, gałąź `main`, publiczne.
- Hosting: GitHub Pages, deploy przy każdym pushu na `main`. Adres tymczasowy `https://khamer1410.github.io/ewa-psycho-webpage/`. Docelowo własna domena przez Custom domain w ustawieniach Pages.
- Stack: czysty HTML + CSS + ~2 KB JS (menu mobilne). Zero build stepu, zero frameworków, zero CMS. Każda zmiana treści to edycja `index.html`.
- Pliki: `index.html`, `css/styles.css`, `css/fonts.css`, `js/nav.js`, `fonts/*.woff2` (Newsreader, Figtree, self-hosted), `img/`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `README.md` (instrukcja dla klientki z checklistą TODO).
- Sekcje i kotwice: `#top` (hero), `#o-mnie`, `#oferta`, `#wizyta` (pierwsza wizyta), `#cennik`, `#gabinety` (w trakcie dodawania), `#opinie` (zakodowana, ukryta atrybutem `hidden`), `#kontakt`. Planowana jeszcze sekcja „dlaczego terapia z człowiekiem, a nie porady od AI”.
- Wszystkie miejsca z danymi do podmiany mają komentarz `<!-- TODO: klientka — ... -->` (ponad 20 sztuk).

## 3. Co z SEO już jest

- `<html lang="pl">`, jeden `<h1>`, semantyczny HTML (`header/nav/main/section/footer`, `<address>`, `<dl>`, `<ol>`), skip link, `alt` przygotowane dla przyszłych zdjęć.
- `<title>` i `meta description` oparte na frazach z eyebrowa: psychoterapia schematu, NLP, Warszawa, online.
- `<link rel="canonical">`, Open Graph, `twitter:card`, `theme-color`, `favicon.svg`.
- `robots.txt` (allow all + Sitemap), `sitemap.xml` z jednym URL.
- JSON-LD: `@type: ["MedicalBusiness","LocalBusiness"]` z name, telephone, email, address, areaServed, priceRange, `hasOfferCatalog` (3 pozycje cennika w PLN), `knowsAbout`, `paymentAccepted`. Po sekcji Gabinety dojdzie `location[]` z dwoma `Place` (GeoCoordinates, OpeningHoursSpecification).
- Wydajność: brak zewnętrznych requestów, fonty z preloadem, brak JS poza menu. Core Web Vitals powinny być zielone bez pracy; po dodaniu zdjęć sprawdzić LCP.
- Wszystkie adresy URL, domena, nazwisko, telefon, adresy i godziny to placeholdery.

## 4. Twarde ograniczenia

1. **Projekt graficzny jest zamrożony.** Układ, kolory, typografia, odstępy pochodzą z zatwierdzonego handoffu projektowego. Można zmieniać treść nagłówków i akapitów w ramach istniejących komponentów. Nie można dodawać nowych typów bloków, zmieniać struktury sekcji ani stylów bez osobnej decyzji właściciela.
2. **Zero skryptów zewnętrznych i zero cookies.** Nie ma Google Analytics, Tag Managera, Pixela, czatów, map Google ani fontów z CDN. Dzięki temu nie ma banera cookies i strona nie przekazuje IP odwiedzających podmiotom trzecim, co dla strony psychoterapeutki jest istotne (sam fakt wejścia jest wrażliwy). Każda propozycja analityki musi być zgłoszona jako decyzja z opisem konsekwencji. Dopuszczalny kierunek do rozważenia: Google Search Console (bez skryptu na stronie, weryfikacja przez DNS) oraz ewentualnie analityka bezcookie z własnego hostu, ale to decyzja właściciela.
3. **YMYL i etyka zawodu.** Treści dotyczą zdrowia psychicznego, Google traktuje je jako Your Money or Your Life i ocenia przez pryzmat E-E-A-T. Jednocześnie kodeksy etyczne psychoterapeutów ograniczają reklamę: żadnych obietnic skuteczności, „gwarancji”, porównań z innymi terapeutami, straszenia. Sekcja Opinie jest ukryta celowo i zostaje ukryta, dopóki klientka nie zdecyduje inaczej. Nie wolno wymyślać certyfikatów, nazw szkoleń ani liczby lat praktyki; te dane dostarczy klientka.
4. **Jedna strona, bez CMS.** Jeśli strategia zakłada blog lub podstrony tematyczne, trzeba to zaproponować jako osobny etap z oceną kosztu utrzymania (klientka nie jest techniczna; każdy wpis to plik HTML albo zmiana stacku). Nie zakładać, że blog istnieje.
5. **Brak formularza i rezerwacji.** Konwersja to kliknięcie w `tel:` lub `mailto:`. Nie proponować formularzy bez uzasadnienia, które przebije decyzję właściciela.
6. **RODO.** Brak banera, brak profilowania. Rekomendacje nie mogą tego naruszać.

## 5. Czego oczekujemy od strategii

Dostarczyć dokument w Markdown po polsku, z konkretami, które da się wykonać w `index.html` i wokół strony. Minimalny zakres:

1. **Badanie fraz** dla polskiego rynku: intencja lokalna (Warszawa, Wola, Mokotów, online), nurt (terapia schematu, terapia traumy, psychoterapeuta schematu), problemowe (np. „terapia schematu na czym polega”, „psychoterapia po traumie Warszawa”), markowe (imię i nazwisko). Dla każdej grupy: szacowana trudność, intencja, gdzie na stronie ją obsłużyć. Zaznaczyć, które frazy są realne dla nowej domeny bez linków.
2. **Rekomendacje on-page per sekcja**: propozycje `<title>`, `meta description`, H1 (uwaga: obecny H1 „Po trudnych doświadczeniach można wrócić do siebie” jest decyzją projektową i copywriterską; jeśli proponujesz zmianę, podaj wariant, który zachowuje ton, i uzasadnij), H2 sekcji, eyebrowy, teksty kart Oferta, `alt` zdjęć. Wskazać dokładnie, który fragment w `index.html` zmienić.
3. **Dane strukturalne**: audyt obecnego JSON-LD i propozycje (np. `sameAs` do profili, `hasCredential`, `medicalSpecialty`, `availableService`, poprawne `openingHoursSpecification` dla dwóch lokalizacji, `FAQPage` jeśli dojdzie sekcja FAQ). Tylko typy istniejące w schema.org, zweryfikowane.
4. **Google Business Profile**: plan dla sytuacji z dwoma gabinetami używanymi w różne dni (jedna wizytówka z główną lokalizacją vs dwie, ryzyka weryfikacji, kategoria „Psychoterapeuta”, godziny, usługi, zdjęcia, zasady odpowiadania na recenzje w zawodzie objętym tajemnicą).
5. **Katalogi i linki**: lista sensownych miejsc w Polsce (ZnanyLekarz, katalogi towarzystw terapeutycznych, listy certyfikowanych terapeutów schematu, Psychologia.edu i podobne), z oceną wartości i kosztu. Bez kupowania linków, bez wymiany linków, bez katalogów śmieciowych.
6. **Treści dodatkowe**: czy i jaki FAQ (jako sekcja, bo FAQ dobrze obsługuje frazy problemowe), czy blog ma sens na tym etapie, jakie 3 do 5 tematów miałyby największy zwrot. Każda propozycja z kosztem utrzymania.
7. **Technikalia po podpięciu domeny**: canonical, sitemap, robots z prawdziwą domeną; www vs bez www; przekierowanie z `github.io` na domenę (GitHub Pages robi to samo po ustawieniu Custom domain, zweryfikować); HTTPS; Search Console (weryfikacja przez DNS, zgłoszenie sitemapy); sprawdzenie Core Web Vitals po dodaniu zdjęć; rozmiary obrazów (hero 1000×1250 WebP, O mnie 640×640 WebP, og-image 1200×630 JPG).
8. **Pomiar bez cookies**: co da się mierzyć z Search Console i logów GitHub Pages (praktycznie nic), jakie są opcje bezcookie i co rekomendujesz jako decyzję dla właściciela.
9. **Kolejność wdrożenia** w trzech falach: przed startem (razem z danymi klientki), pierwszy miesiąc po starcie, kwartał.

## 6. Czego nie robić

- Nie edytować plików w repo bez wyraźnego polecenia; dostarczyć rekomendacje, które właściciel wdroży lub zleci.
- Nie proponować zmian w projekcie graficznym.
- Nie dodawać skryptów zewnętrznych, cookies ani banerów.
- Nie pokazywać sekcji Opinie i nie generować opinii.
- Nie wymyślać kwalifikacji, nazw szkoleń, liczb pacjentów ani lat doświadczenia.
- Nie używać języka obietnic („skuteczna terapia”, „pozbądź się lęku w 10 sesji”).

## 7. Pytania otwarte do właściciela, które strategia powinna oznaczyć

- Czy klientka zgadza się na Google Business Profile z adresem gabinetu (to publiczne ujawnienie, gdzie przyjmuje)?
- Czy ma certyfikaty, które można pokazać (np. certyfikat terapeuty schematu ISST), i czy jest w publicznych rejestrach terapeutów?
- Czy chce bloga lub FAQ i kto będzie pisał treści?
- Czy akceptuje jakąkolwiek analitykę, nawet bezcookie?
- Jaka ma być główna lokalizacja dla wyników lokalnych, jeśli wizytówka ma być jedna?

## 8. Gdzie szukać

- Kod i treści: `index.html` (komentarze TODO wskazują placeholdery).
- Instrukcja i checklista dla klientki: `README.md`.
- Specyfikacja projektu graficznego (tokeny, układ, decyzje): `/Users/krzysztof.hamerszmit/Downloads/design_handoff_psychotherapist_landing/README.md` oraz screenshoty `screenshots/desktop.png`, `mobile.png` w tym samym folderze.
- Podgląd lokalny: `python3 -m http.server 8765` w katalogu repo albo konfiguracja `static` w `.claude/launch.json`.
