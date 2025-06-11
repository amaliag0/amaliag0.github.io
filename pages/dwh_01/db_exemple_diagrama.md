````mermaid
%%{init: {'er': { 'layoutDirection': 'LR' }}}%%
erDiagram
    DIM_PRODUCTE {
        int producte_id
        string nom
        string descripcio
        float preu
        int categoria_id
    }
    DIM_PRODUCTE_CATEGORIA {
        int categoria_id
        string nom
    }
    DIM_MATERIA {
        int materia_id
        string nom
        string descripcio
        int categoria_id
    }
    DIM_MATERIA_CATEGORIA {
        int categoria_id
        string nom
    }
    DIM_PROVEIDOR {
        int proveidor_id
        string nom
        string contacte
        int regio_id
    }
    DIM_CLIENT {
        int client_id
        string nom
        string contacte
        int regio_id
    }
    DIM_EMPLEAT {
        int empleat_id
        string nom
        int departament_id
    }
    DIM_DEPARTAMENT {
        int departament_id
        string nom
    }
    DIM_TEMPS {
        int temps_id
        date data
        time hora
    }
    DIM_REGIO {
        int regio_id
        string nom
    }
    FACT_VENDES {
        int venda_id
        int producte_id
        int client_id
        int temps_id
        int empleat_id
        int quantitat
        float total
    }
    FACT_COMPRES {
        int compra_id
        int materia_id
        int proveidor_id
        int temps_id
        int empleat_id
        int quantitat
        float total
    }
    FACT_FITXATGE_EMPLEATS {
        int fitxatge_id
        int empleat_id
        int temps_id
        string tipus_fitxatge
    }
    METRIQUES_COMPLEXES {
        int metrica_id
        int temps_id
        int producte_id
        int client_id
        float mitjana_vendes_per_client_producte
        float variacio_mensual_compres
        float percentatge_puntualitat_empleats
    }
    DIM_PRODUCTE ||--o{ FACT_VENDES : producte_id
    DIM_CLIENT ||--o{ FACT_VENDES : client_id
    DIM_TEMPS ||--o{ FACT_VENDES : temps_id
    DIM_EMPLEAT ||--o{ FACT_VENDES : empleat_id
    DIM_MATERIA ||--o{ FACT_COMPRES : materia_id
    DIM_PROVEIDOR ||--o{ FACT_COMPRES : proveidor_id
    DIM_TEMPS ||--o{ FACT_COMPRES : temps_id
    DIM_EMPLEAT ||--o{ FACT_COMPRES : empleat_id
    DIM_EMPLEAT ||--o{ FACT_FITXATGE_EMPLEATS : empleat_id
    DIM_TEMPS ||--o{ FACT_FITXATGE_EMPLEATS : temps_id
    DIM_PRODUCTE_CATEGORIA ||--o{ DIM_PRODUCTE : categoria_id
    DIM_MATERIA_CATEGORIA ||--o{ DIM_MATERIA : categoria_id
    DIM_DEPARTAMENT ||--o{ DIM_EMPLEAT : departament_id
    DIM_REGIO ||--o{ DIM_CLIENT : regio_id
    DIM_REGIO ||--o{ DIM_PROVEIDOR : regio_id
    DIM_PRODUCTE ||--o{ METRIQUES_COMPLEXES : producte_id
    DIM_CLIENT ||--o{ METRIQUES_COMPLEXES : client_id
    DIM_TEMPS ||--o{ METRIQUES_COMPLEXES : temps_id
    ```