# :sparkles: Unitat de Treball 2. Transformació de dades

## Objectius de la UT
<mark> ACTUALITZAR AMB ELEMENTS CURRICULARS</mark>
- Comprendre la importància de la transformació de dades dins del procés ETL.
- Aplicar tècniques de neteja, normalització i enriquiment de dades.
- Conèixer els principis de la gestió de dades i la governança de dades.
- Garantir la qualitat i la protecció de les dades durant la transformació.

## 1. ETL: Extracció, Transformació i Càrrega (continuació)

Continuant amb el procés ETL, el següent pas una vegada realitzada l'extracció de dades és la transformació.

### Transformació

La **transformació** és la fase intermèdia del procés ETL, on les dades en brut es convertixen en dades preparades per a ser carregades en el magatzem de dades, en funció de l'objectiu de l'aprofitament de dades. La transformació consistix a filtrar, netejar i donar un format concret a les dades, abans d'emmagatzemar-les.   

A cavall entre l'extracció i la transformació està la revisió i verificació de les dades, moment en el qual es decidixen les operacions que s'hauran d'executar sobre les dades, incloent el rebuig de dades que no cumplisquen els requisits de qualitat establerts.  

Són freqüents les següents operacions sobre les dades:

- Conversió de tipus de dades (ex. de text a data).
- Neteja de valors nuls, incorrectes o duplicats.
- Filtrat i selecció de columnes rellevants.
- Normalització de formats (majúscules, codificacions, unitats).
- Agregacions de dades.
- Enriquiment amb dades externes o derivades.

> Exemples: convertir “sí/no” en valors booleans, unificar codis postals, eliminar duplicats.  

---

## 2. Qualitat de dades: un dels fonaments de la transformació

La **qualitat de les dades** és un element clau per garantir que les decisions basades en dades siguen fiables. Forma part dels procediments de gestió de dades (_data management_ i _data governance_) i és un dels pilars que regixen les operacions que es realitzaran durant la transformació en el procés ETL.    

### Dimensions de la qualitat de dades:  

Les dimensions de la qualitat de dades són característiques de les dades que es poden avaluar de manera individual, per millorar aspectes concrets d'aquestes. És habitual que les organitzacions mesuren la qualitat de les seues dades segons aquestes dimensions, i aquestes mesures, juntament amb altres factors, definixen els usos per als quals les dades són adequades. 

> Per exemple, si una font de dades guarda les lectures de sensors IoT una vegada al dia, aquestes dades no seran adequades per realitzar prediccions horàries, però sí que ho poden ser per realitzar prediccions diàries o mensuals.  

La següent taula mostra les dimensions més habituals, si bé cada sistema o entorn pot definir-ne d'altres:

| Dimensió       | Descripció                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Completesa    | Les dades estan completes, sense camps buits innecessaris.                    |
| Exactitud      | Les dades reflectixen la realitat de manera precisa.                      |
| Consistència   | No hi ha contradiccions entre les dades de diferents fonts o camps.                     |
| Validesa       | Les dades seguixen els formats, tipus i rangs esperats. |
| Homogeneïtat   | Les dades són uniformes i consistents al llarg del temps, amb característiques similars pel que fa a formats i estructures, dins un mateix objecte de dades. |
| Actualització  | Les dades estan al dia i reflectixen l’estat temporal requerit.                      |
| Unicitat       | No hi ha duplicats innecessaris.                                           |

---

## 3. Protecció de dades: un altre fonament de la transformació

La governança de dades establix les normes i responsabilitats que garantixen que les dades estiguen protegides, seguisquen les regulacions establertes i puguen ser útils. Pel que fa a la protecció de dades, aquesta es regix pels següents principis clau:

- Classificació de dades: habitualment en públiques, internes, confidencials, molt confidencials.
- Protecció de dades personals: compliment del RGPD i d'altres regulacions nacionals o locals pel que fa a l'ús de dades.
- Accés controlat: qui pot veure o modificar cada dada.
- Traçabilitat: registre de qui ha accedit o modificat les dades.

Durant la transformació de dades, aquestes passen d’un estat en brut a un estat estructurat i preparat per a anàlisis posteriors. És en aquest moment quan:

- Es poden identificar dades personals o sensibles.
- Es poden combinar fonts que revelen informació nova o més detallada.

I, per tant, la fase de transformació és **clau per garantir la privacitat i la seguretat** de les dades, ja que és quan es poden aplicar mesures de protecció abans que les dades siguen visibles o accessibles per altres sistemes o usuaris.

### 3. 1. Tipus de dades a protegir

A la Unió Europea, segons el RGPD ([Reglament General de Protecció de Dades](https://eur-lex.europa.eu/ES/legal-content/summary/general-data-protection-regulation-gdpr.html)), cal prestar especial atenció a:

- **Dades personals**: nom, DNI, correu electrònic, telèfon, IP...
- **Dades sensibles**: salut, orientació sexual, creences religioses, dades biomètriques...
- **Dades identificadores indirectes**: combinacions que poden identificar una persona (ex. codi postal + data de naixement).

No obstant això, és necessari conéixer l'origen de les dades, ja que poden ser aplicables altres regulacions no europees en funció del seu contingut; per exemple, si contenen informació sobre ciutadans estatunidencs. A més, els estats també definixen regulacions específiques pel que fa al tractament de dades, algunes de les quals poden ser més restrictives que el RGPD (com és el cas a Alemanya).  

D'altra banda, no només les dades personals són considerades sensibles, sinó que, en funció de l'activitat duta a terme per l'organització per a la qual s'implementa el projecte, altres dades poden necessitar d'una protecció específica també. Per tant, durant el desenvolupament del projecte d'aprofitament de dades, **és necessari coordinar-se amb els departaments legals i de governança de dades de l'entitat**, així com amb les persones responsables de les dades en qüestió, per tal d'assegurar la legalitat i la correcció en els procediments.

### 3.2. Accions de protecció

1. Anonimització

    - Elimina qualsevol possibilitat d’identificar una persona.

2. Pseudonimització

    - Substituïx dades identificatives per valors ficticis, però manté la possibilitat de revertir-ho amb una clau.

3. Encriptació

    - Protegeix les dades mitjançant codificació.
    - Pot aplicar-se a camps concrets (ex. targetes de crèdit) o a tot el conjunt de dades.
    - Pot ser:
        - En repòs: mentre les dades estan emmagatzemades.
        - En trànsit: mentre es mouen entre sistemes.

4. Filtrat i exclusió

    - Durant la transformació, es poden eliminar o excloure camps que no siguen necessaris per a l’anàlisi.

5. Control d’accés i traçabilitat

    - Registrar qui transforma què, quan i com.
    - Assignar permisos per a accedir només a les dades necessàries.
    - Mantindre un registre d’auditoria per garantir la responsabilitat.

La taula següent resumix les tècniques de protecció de dades més habituals, amb consells sobre quan aplicar-les i exemples pràctics:  

| **Tècnica de Protecció**           | **Descripció**                                                                 | **Quan aplicar-la**                                                                 | **Exemple pràctic**                                                                 |
|-----------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Anonimització                     | Elimina qualsevol possibilitat d’identificar una persona.                        | Quan no es necessita cap dada personal per a l’anàlisi.                             | Substituir noms per codis aleatoris, eliminar camps com correu electrònic o telèfon. |
| Pseudonimització                  | Substitueix dades identificatives per valors ficticis, però reversibles.         | Quan es necessita fer seguiment sense exposar la identitat real.                   | Encriptar el DNI, assignar un identificador únic a cada usuari.                      |
| Encriptació                       | Protegeix les dades mitjançant codificació.                                      | Quan es vol protegir dades sensibles durant l’emmagatzematge o el trànsit.         | Encriptar el camp de targetes de crèdit o la data de compra.                         |
| Filtrat i exclusió                | Elimina o exclou camps que no són necessaris per a l’anàlisi.                    | Quan hi ha camps que no són rellevants per a l’anàlisi.                             | Eliminar el codi postal si no és rellevant per a l’anàlisi.                          |
| Control d'accés i traçabilitat   | Registra qui transforma què, quan i com. Assigna permisos d’accés.              | Sempre, per garantir la responsabilitat i la seguretat.                             | Mantindre un registre d’auditoria per a garantir la responsabilitat.                 |

### 3. 3. Tècniques d'anonimització de dades 

#### Supressió
Eliminació directa de dades identificatives (noms, DNI, correus electrònics).  

Aplicació tècnica:  
- Elimina columnes o camps sencers.
- Pot aplicar-se a dades sensibles o no essencials per a l’anàlisi.
- Les dades poden substituir-se per un valor que faça referència a l'acció realitzada.

```plaintext
Nom: [eliminat], Telèfon: [eliminat]
```

#### Tokenització irreversible
Substitució de dades sensibles per un token aleatori sense significat.

Aplicació tècnica:
- El token no té cap relació matemàtica amb el valor original.
- No es guarda cap taula de correspondència segura.

```plaintext
DNI: 12345678A → Token: XZ9K2P
```

### 3. 4. Tècniques de pseudonimització de dades

#### Pseudonimització
Substitució de dades identificatives per valors ficticis o codis. Pot ser reversible si es guarda una taula de correspondència segura.

Aplicació tècnica:
- Assignació d’un identificador únic (hash, UUID).

```plaintext
Nom: “Miquel Garcia” → ID_Usuari: “U12345”
```

#### Tokenització reversible
Substitució de dades sensibles per un token aleatori sense significat.

Aplicació tècnica:
- El token no té cap relació matemàtica amb el valor original.
- Es guarda una taula de correspondència segura.

```plaintext
DNI: 12345678A → Token: XZ9K2P
```

#### Generalització
Substitució de valors específics per categories més àmplies.

Aplicació tècnica:
- Agrupar valors en rangs o nivells d’abstracció.

```plaintext
Edat: 34 → Edat: 30-40  
Codi postal: 46001 → Província: València
```

#### Pertorbacions (_Noise Addition_)
Afegir soroll aleatori a les dades per dificultar la identificació. Preserva tendències generals però oculta valors exactes.

Aplicació tècnica:
- Suma de valors aleatoris controlats a dades numèriques.
 
```plaintext
Ingressos: 32.000 € → 32.000 € ± ε
```

#### K-anonimat
Garantix que cada registre siga indistinguible d’almenys k-1 altres.

Aplicació tècnica:
- Requereix generalització i supressió fins que cada combinació de valors siga compartida per almenys k registres.

```plaintext
Si k=3, almenys 3 persones han de compartir la mateixa combinació d’edat, sexe i codi postal.
```

### 3. 5. Encriptació de dades

L'encriptació es pot realitzar al conjunt de dades complet o de manera selectiva (a camps concrets amb dades sensibles). Consistix en la codificació de camps sensibles per a protegir-los durant el seu processament.

Aplicació tècnica:
- Algoritmes com AES, RSA.
- Pot ser simètrica (una clau) o asimètrica (clau pública/privada).

```plaintext
Targeta de crèdit → Encriptada amb AES-256
```

Aquesta taula compara les tècniques d’encriptació més habituals en processos ETL:

| **Tècnica de Protecció**                | **Tipus**                    | **Ús Principal**                                                                 | **Motiu d'Ús**                                                                                   | **Exemple Pràctic**                                                  |
|----------------------------------------|------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| AES (Advanced Encryption Standard)     | Simètrica                   | Encriptació de camps sensibles com DNI, correus electrònics, targetes de crèdit | Ràpid, segur i compatible amb la majoria d’eines ETL                                            | Encriptació de camps com DNI, correus electrònics, targetes de crèdit |
| RSA                                    | Asimètrica                  | Transmissió segura de claus o dades entre sistemes ETL distribuïts              | Ideal per a protegir dades en trànsit entre nodes o serveis                                     | Transmissió segura de claus entre nodes ETL                          |
| Encriptació basada en TLS/SSL          | Protocol de seguretat       | Protecció de connexions entre components ETL                                     | Evita que les dades siguen interceptades durant la transmissió                                  | Protecció de connexions JDBC amb bases de dades                      |
| Encriptació a nivell de camp           | Simètrica o asimètrica      | Encriptació selectiva de columnes específiques                                  | Permet protegir només les dades crítiques sense afectar el rendiment global                     | Encriptació selectiva de columnes com telèfon, adreça                |
| Hashing (amb salts)                    | Funció unidireccional       | Protecció de contrasenyes o identificadors únics                                | Útil per a dades que no cal desxifrar, com contrasenyes                                          | Protecció de contrasenyes amb SHA-256 + salt                         |
| Tokenització                           | Substitució de dades        | Protecció de dades personals en entorns on no es pot aplicar encriptació directa| Compatible amb sistemes que no poden operar amb dades encriptades                              | Substitució de dades personals per tokens aleatoris                  |

---

## 4. Bones pràctiques

- Aplicar el principi de **minimització de dades**: només ingerir, transformar i conservar les dades estrictament necessàries.
- Documentar totes les transformacions aplicades les dades, especialment a dades sensibles.
- Validar que les dades sensibles no permeten la identificació, una vegada la tècnica de protecció estiga aplicada.
- Establir polítiques clares de retenció i eliminació de dades.

> Exemple pràctic
> 
> Suposem que tenim un conjunt de dades de clients amb els següents camps:
> 
> | Nom complet | Correu electrònic | Codi postal | Producte comprat | Dades pagament |
> |-------------|-------------------|-------------|------------------|-------------|
> 
> Durant la transformació, podem aplicar:
> 
> - Pseudonimització del nom i correu.
> - Filtrat del codi postal si no és rellevant.
> - Encriptació de les dades de pagament.
> - Documentació de totes les accions aplicades.

---

## Conclusions

- La transformació no és només una qüestió tècnica, sinó també ètica i legal.
- La qualitat i la protecció de les dades són responsabilitat de tot l’equip.
- Una bona transformació prepara les dades per a ser útils, segures i reutilitzables.

---