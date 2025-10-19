# ProArcNexusBIM

Un sistem informational BIM.

## Descriere Generala

ProArcNexusBIM este o aplicatie web construita cu Django, conceputa pentru a gestiona clienti, articole, devize si pentru a genera rapoarte. Aceasta ofera un sistem de autentificare bazat pe roluri, functionalitati de audit si setari configurabile.

## Functionalitati

-   **Gestionare Conturi:**
    -   Inregistrare si autentificare utilizatori.
    -   Resetare parola.
    -   Profiluri de utilizator editabile.
    -   Sistem de permisiuni bazat pe roluri (admin, manager, user).

-   **Gestionare Clienti:**
    -   Adaugare, modificare si stergere clienti.
    -   Cautare si listare clienti cu paginatie.

-   **Gestionare Articole:**
    -   Adaugare, modificare si stergere articole.
    -   Cautare si listare articole cu paginatie.

-   **Gestionare Devize:**
    -   Creare, modificare si stergere devize.
    -   Adaugare de linii de deviz dintr-un catalog de articole.
    -   Calcul automat al valorii totale.
    -   Generare PDF pentru devize.

-   **Rapoarte:**
    -   Generare de rapoarte sumative pe o perioada selectata.
    -   Filtrare rapoarte dupa client.
    -   Vizualizare grafica a datelor.
    -   Export rapoarte in format PDF.

-   **Audit:**
    -   Inregistrarea automata a tuturor modificarilor (creare, actualizare, stergere) pentru modelele principale.
    -   Jurnal de actiuni detaliat, cu informatii despre utilizator, model, actiune si datele modificate.

-   **Setari:**
    -   Gestionarea setarilor generale ale aplicatiei (doar pentru admin).

## Structura Proiectului

Proiectul este impartit in mai multe aplicatii Django, fiecare responsabila pentru o functionalitate specifica:

-   `ProArcNexus2`: Aplicatia principala a proiectului, contine setarile si configuratiile URL.
-   `accounts`: Gestioneaza utilizatorii, autentificarea si permisiunile.
-   `clients`: Gestioneaza clientii.
-   `articles`: Gestioneaza articolele.
-   `estimates`: Gestioneaza devizele si liniile de deviz.
-   `reports`: Genereaza rapoarte.
-   `audit`: Implementeaza functionalitatea de audit.
-   `settings_app`: Gestioneaza setarile aplicatiei.

## Tehnologii Utilizate

-   **Backend:** Django, Python
-   **Baza de date:** Oracle
-   **Frontend:** HTML, CSS, JavaScript
-   **Generare PDF:** WeasyPrint
-   **Grafice:** Matplotlib

## Baza de Date

Aplicatia utilizeaza o baza de date Oracle. Modelele Django sunt mapate pe tabele existente, dupa cum este specificat in clasa `Meta` a fiecarui model (`managed = False`).

Principalele modele sunt:
- `Utilizator`
- `Client`
- `Articol`
- `Deviz`
- `LinieDeviz`
- `ChangeLog`
- `SetareGenerala`

## Roluri si Permisiuni

-   **Admin:** Are acces la toate functionalitatile, inclusiv la panoul de administrare Django, setari si stergerea datelor.
-   **Manager:** Are acces la majoritatea functionalitatilor, inclusiv crearea si editarea datelor, vizualizarea rapoartelor si a jurnalului de audit.
-   **User:** Are acces de vizualizare la date, poate crea devize si vizualiza PDF-uri.