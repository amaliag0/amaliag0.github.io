# Forn Nyas Coca
Exemple de model de base de dades.  

La base de dades està pensada per a un forn tradicional de pa i dolços anomenat "Nyas Coca", que compra matèries primes per elaborar els seus productes, i ven a clients particulars i també a negocis i escoles.

El diagrama inclou:

- alguns atributs típics per a cada taula
- les claus mínimes necessàries
- les relacions entre les taules

---

## Descripció de la informació inclosa en el model

### Base de dades
`forn_nyas_coca`

### Taules de dimensions

- `dim_producte`: taula amb la llista de productes que estan disponibles a la venda.
- `dim_producte_categoria`: taula amb la llista de categories que poden tindre els productes de venda.
- `dim_materia`: taula amb la llista de matèries primes que són necessàries per elaborar els productes.
- `dim_materia_categoria`: taula amb la llista de tipus de metèries primes, principalment necessari per saber com s'han d'emmagatzemar.
- `dim_proveidor`: taula amb la llista de proveidors que proporcionen les matèries primes.
- `dim_client`: taula amb la llista de clients que compren a l'engròs.
- `dim_empleat`: taula amb la llista d'empleats del forn.
- `dim_departament`: taula amb la llista de departaments als quals poden pertànyer els empleats, en funció de si elaboren productes, únicament venen productes, realitzen tasques comercials, tasques de gestió o altre tipus de tasques.
- `dim_temps`: taula amb els atributs necessaris per representar dates i temps.
- `dim_regio`: taula amb la informació de les regions a Espanya, utilitzada per la taula dim_client i la taula dim_proveidor.

### Taules de fets

- `fact_vendes`: taula amb el registre de les vendes de productes. Es relaciona principalment amb dim_producte, dim_client, dim_temps, dim_empleat.
- `fact_compres`: taula amb el registre de les compres de matèries primes. Es relaciona principalment amb dim_materia, dim_temps, dim_empleat.
- `fact_fitxatge_empleats`: taula amb el registre dels fitxatges d'entrada i eixida laborals dels empleats. Es relaciona amb dim_empleat, dim_temps.
- Taula amb mètriques

---

## Model seguint l'esquema _snowflake_

En el fitxer [db_exemple_diagrama.md](./db_exemple_diagrama.md).