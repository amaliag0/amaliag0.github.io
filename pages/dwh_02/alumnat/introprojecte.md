
# Pràctica: Introducció al Projecte

> Llegenda:  
> :pencil2: Tasca per a l'alumnat.  
> :fishing_pole_and_fish: Ajuda/material proporcionat pel professorat.  

Durant la major part d'aquest mòdul, l’alumnat desenvoluparà un **projecte pràctic** que simula un cas real d’aprofitament de dades. L’objectiu és construir un **magatzem de dades** que integre múltiples fonts i permeta visualitzar informació clau en un **quadre de comandament**, dins d'un context i ús concrets definits.

--- 

## Objectius del projecte

<mark>REDEFINIR AMB SABER FER</mark>

- Aprendre a capturar dades des de diferents fonts.
- Entendre els principis dels processos d'extracció, preprocessament, 
- Dissenyar un model de dades relacional.
- Implementar processos ETL amb Python.
- Emmagatzemar les dades en PostgreSQL.
- Visualitzar els resultats amb Grafana.

- aprenga a entendre les necessitats d'una entitat/client respecte a l'ús de les dades que genera la seua activitat
- guanye habilitats per entendre la realitat tecnològica i estructural dels sistemes d'informació de l'entitat/client i les relacions i fluxes entre ells
- conega tecnologies, ferramentes i terminologia dels àmbits de l'arquitectura, el modelat i l'enginyeria de dades
- aprenga a dissenyar models de dades de manera crítica, segons usos concretos
- aprenga bones pràctiques dels àmbits de l'arquitectura i l'enginyeria de dades
- desenvolupe habilitats de comunicació, tant oral com escrita, de cara a l'entitat/client i per crear documentació  

## Fases del projecte
<mark>AFEGIR N. SESSIONS I LINK UT i ferramentes</mark>

1. **Exploració del cas**: Definició de l'entitat i cas de negoci. Quines dades necessitem? Quines decisions volem recolzar?
2. **UT1 Ingesta**: Captura de dades de fonts diverses.
3. **UT2 Preprocessament**: Processos ETL i qualitat de dades.
3. **UT3 Emmagatzematge i Modelatge**: Disseny del magatzem de dades.
4. **UT4 Analítica**: Disseny de mètriques i anàlisis avançats. Implementació en el magatzem de dades.
5. **UT5 Visualització**: Creació d'un quadre de comandament interactiu.
6. **Presentació i Avaluació**

## Resultat i entregues
<mark>COMPLETAR</mark>

## Metodologies
- Treball en equip
- Aprenentatge basat en simulació de cas real
- Aprenentatge-investigació
- Pràctica guiada

## Avaluació

<mark>TAULA</mark>

---

:checkered_flag::checkered_flag::checkered_flag: COMENCEM! :checkered_flag::checkered_flag::checkered_flag:

---

## FASE D'ORGANITZACIÓ DEL PROJECTE I D'EXPLORACIÓ

Aquesta fase és fonamental perquè l’alumnat entenga el context, definisca els objectius i planifique el treball de manera col·laborativa i estructurada.  

Durant la sessió, el professorat explicarà i assignarà les tasques una a una, exposant l'exemple pràctic per il·lustrar el resultat esperat. Totes les tasques s'han de completar en equip, encara que el professorat realitzarà les explicacions a tota la classe i motivarà discussions grupals quan siga convenient.

### :pencil2: Creació d'equips de treball

En grups de 2 persones (3 si cal).  

### :pencil2: Elecció de cas pràctic

S'ha d'escollir una proposta per equip:
- Negoci de venta en línia
- Associació sense ànim de lucre de suport a un barri
- Ajuntament
- Club esportiu
- Magatzem logístic
- Proposta alternativa de l'alumnat

> Exemple "Forn Nyas Coca" (forn artesà amb diverses tendes).

### :pencil2: Anàlisi del cas pràctic

- Identificació de les àrees de negoci implicades.
- Discussió sobre possibles preguntes a respondre amb dades.

> Exemple "Forn Nyas Coca"  
> El "Forn Nyas Coca" és un forn artesà amb diversos punts de venda repartits per la ciutat i una producció centralitzada. Oferix pa, brioixeria, pastissos i productes de temporada. També ven a restaurants i escoles. Disposa de sistemes digitals per a la gestió de comandes, vendes, estoc i compres de matèries primeres.  
> 
> Possibles preguntes:
> - Quins productes es venen més segons el dia de la setmana?
> - Hi ha diferències de consum entre barris?
> - Quins dies es genera més malbaratament? De quins productes?
> - A quines hores del dia hi ha més clients? I menys?

### :pencil2: Identificació de fonts de dades

- Anàlisi de les fonts de dades disponibles.

> Exemple "Forn Nyas Coca"   
> | Font de dades                   | Tipus           | Dades                      |
> |---------------------------------|-----------------|----------------------------|
> | Sistema intern d'estoc i vendes | Estructurat     | vendes, productes, usuaris |
> | Fitxer CSV                      | Semiestructurat | sensors ambientals         |
> | Fitxer CSV                      | Estructurat     | aplicació per fitxar       |


:fishing_pole_and_fish: Fonts de dades proporcionades
<mark> COMPLETAR </mark>

### :pencil2: Definició d’objectius analítics

Els objectius han de ser clars, mesurables i alineats amb el cas.
- Definició de 10 objectius a aconseguir mitjançant les dades, relacionats amb problemes de negoci. 
- Definició de la prioritat dels objectius, tenint en compte la disponibilitat de dades i la viabilitat del ítem del projecte.

> Exemple "Forn Nyas Coca"  
> Millorar la presa de decisions del negoci mitjançant l’anàlisi de dades per: 
> - (1) Optimitzar la producció segons la demanda real.
> - (2) Reduir el malbaratament de productes frescos.
> - (3) Visualitzar en temps real l’estat de vendes i estoc.
> - (4) Controlar els sistemes de conservació dels aliments.
> - (5) Millorar l'atenció als clients en tenda.
> - (6) Detectar patrons de compra per zona, dia i hora.
> - (7) Analitzar l’impacte de les promocions i productes estacionals.  

### :pencil2: Organització del treball

Per tal que cada integrant aprenga les destreses requerides en cada fase de l'aprofitament de dades, es recomana que es dividisquen les tasques d'implementació i documentació del projecte per a cada fase i que s'assignen de manera alternada (una persona farà la implementació d'una fase i l'altra la documentació, mentre que a la següent fase s'intercanviaran els rols).
