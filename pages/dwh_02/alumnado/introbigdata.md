# :sparkles: Introducció al _Big Data_ i a l'aprofitament de dades

## 1. Què és el _Big Data_?

El ***Big Data*** fa referència al tractament de conjunts de dades que tenen grans volums, o que s'han de processar a gran velocitat, o que tenen gran complexitat. Durant els inicis de l'era del _Big Data_, les eines tradicionals de gestió de dades no eren suficients per gestionar aquestes dades de manera eficient, i es van desenvolupar eines específiques que resolien les problemàtiques principals de la gestió d'aquestos conjunts de dades. Però en el camp de les dades, l'objectiu no és emmagatzemar-les en si, sinó més bé extraure'n valor per prendre decisions més informades, automatitzar processos o descobrir patrons ocults, entre altres. És a dir, l'objectiu és l'**aprofitament de les dades**. A més, la majoria de les tècniques i destreses necessàries en l'àmbit de les dades són independents de si estem tractant amb [_Big_, _Medium_ o _Small Data_](https://medium.com/@thibaut_gourdel/data-sizes-matter-small-medium-big-6303ed48ea26), i és habitual començar els projectes a una escala menor i augmentar-ne el volum i la complexitat amb el temps.  

### Les V del _Big Data_

Si bé totes aquestes característiques no són exclussives del _Big Data_, ajuden a entendre la complexitat que implica la seua gestió:

- **Varietat**: Diversitat de fonts i tipus (dades estructurades, semiestructurades i no estructurades).
- **Volum**: Quantitat massiva de dades generades per sensors, xarxes socials, dispositius mòbils, etc.
- **Velocitat**: Ritme amb què es generen i processen les dades, incloent dades en _temps real_.
- **Veracitat**: Qualitat i fiabilitat de les dades.
- **Valor**: Capacitat d’extraure coneixement útil de les dades per a la presa de decisions.
- **Viabilitat**: Capacitat de l'entitat per gestionar les dades i extraure'n valor.
- **Visualització**: Representació de les dades en forma gràfica o amb mètriques/indicadors per facilitar-ne la interpretació.

### La importància de l'aprofitament de les dades

Per exemple, per a...

- Detectar patrons de comportament dels clients.
- Optimitzar processos industrials.
- Predir fallades en maquinària.
- Personalitzar serveis.
- Prendre decisions basades en dades reals i no en intuïcions.

És a dir, que saber fer ús de les dades que es generen en una activitat (comercial o no) és una competència essencial en qualsevol àmbit professional en l'actualitat, tenint en compte que tota activitat genera dades i que la gran majoria d'aquestes dades són digitals o poden digitalitzar-se.

---

## 2. Arquitectures _Big Data_

<mark> REVISAR</mark>

Per gestionar _Big Data_ s’utilitzen arquitectures específiques que permeten escalar el processament i adaptar-se a diferents tipus de dades i necessitats.

### Arquitectura Lambda

- Combina dues capes:
  - **Batch layer**: Processa grans volums de dades històriques.
  - **Speed layer**: Processa dades en temps real.
- És robusta i flexible, però complexa de mantindre.

### Arquitectura Kappa

- Només té una capa de processament en temps real.
- És més senzilla i adequada quan no es necessita anàlisi històrica.
- Ideal per a fluxos continus de dades, com sensors o xarxes socials.

Ambdues arquitectures es basen en el principi de **processament distribuït**, és a dir, dividir el treball entre múltiples nodes o servidors.  

<mark>[!]</mark> Aquestos conceptes no es treballaran en el projecte principal del mòdul.

> Per ampliar coneixements sobre problemàtiques encara actuals respecte a ferramentes i plataformes de gestió de dades: ["The Problem is Medium Data"](https://highscalability.com/the-big-problem-is-medium-data/)

---

## 3. Components d’un sistema d'aprofitament dades

Un sistema d'aprofitament de dades complet inclou els següents blocs:

1. **Ingesta de dades**: Captura des de múltiples fonts (APIs, arxius, bases de dades, sensors...). <mark>_Aquestes destreses es treballaran en la Unitat de Treball 1_</mark>.
2. **Prepocessament**: Revisió, neteja i validació de les dades. <mark>_Aquestes destreses es treballaran en la Unitat de Treball 1 i 2_</mark>.
3. **Emmagatzematge**: Integració de les dades en bases de dades relacionals o altres sistemes, creant Magatzems de dades (_Data Warehouse_) o Llacs de dades (_Data Lake_). <mark>_Aquestes destreses es treballaran en la Unitat de Treball 3_</mark>.
4. **Modelat**: Creació de models de dades que les integren, agrupen i relacionen, en formats diferents en funció de l'objectiu analític i/o de visualització (OLAP, esquema estrella...).  <mark>_Aquestes destreses es treballaran en la Unitat de Treball 3_</mark>.
5. **Analítica**: Ampliació del model amb dades derivades, en preparació de les representacions gràfiques o del càlcul d'indicadors de progrés. <mark>_Aquestes destreses es treballaran en la Unitat de Treball 4_</mark>.
6. **Visualització**: Quadres de comandament (_dashboards_), informes d'intel·ligència de negoci (BI) i alertes que permeten visualitzar, interpretar i monitoritzar les dades i els indicadors definits. <mark>_Aquestes destreses es treballaran en la Unitat de Treball 5_</mark>.

Aquests components es connecten entre si formant un **flux de dades** que va des de les fonts fins a la presa de decisions, una vegada s'han interpretat les dades. Tots aquestos conceptes s'estudiaran amb profunditat en les Unitats de Treball referides.  

<mark> REVISAR ESTIL</mark>

```mermaid
flowchart LR
    subgraph "`Extracció (E)`"
        A1["`F1: Base de dades`"]
        A2["`F2: API`"]
        A3["`F3: Arxiu`"]
        A1 --> B["`(1) Ingesta de dades`"]
        A2 --> B
        A3 --> B
    end

    subgraph "`Transformació (T)`"
        B --> C["`(2) Preprocessament de dades`"]
    end

    subgraph "`Càrrega (L)`"
        C --> D["`(3) Emmagatzematge de dades`"]
    end

    D --> E["`(4) Modelat de dades`"]  

    E --> F["`(5) Analítica de dades`"]
    
    F --> G["`(6) Visualització de dades`"]

    style A1 fill:#FFD1DC,stroke:#000,stroke-width:1px
    style A2 fill:#FFD1DC,stroke:#333,stroke-width:1px
    style A3 fill:#FFD1DC,stroke:#333,stroke-width:1px
    style B fill:#FFD1DC,stroke:#333,stroke-width:1px
    style C fill:#DA70D6,stroke:#333,stroke-width:1px
    style D fill:#F1FAEE,stroke:#333,stroke-width:1px
    style E fill:#D8F3DC,stroke:#333,stroke-width:1px
    style F fill:#ffb,stroke:#fff,stroke-width:1px
    style G fill:#ffb,stroke:#fff,stroke-width:1px

```

---
## 4. Rols associats al món professional 

<mark>Intro + relació amb projecte</mark>

#### Arquitectura de dades

#### Enginyeria de dades

#### Anàlisi de dades

#### Ciència de dades

#### Intel·ligència de Negoci (BI)

#### Gestió de Dades i Governança de Dades

#### Altres
CPO


---
