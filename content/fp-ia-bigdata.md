# Unitat de Treball: Disseny d'un magatzem de dades (DWH)

<table>
    <tr>
        <th>Títol</th>
        <td>Disseny d'un magatzem de dades (DWH)</td>
    </tr>
    <tr>
        <th>Àmbit</th>
        <td>Curs d'especialització FPS d'IA i Big Data > Sistemes de Big Data (5074)</td>
    </tr>
    <tr>
        <th>Temporització</th>
        <td>X sessions</td>
    </tr>
    <tr>
        <th>Descripció</th>
        <td>La gestió de sistemes d'informació digital i de les dades que contenen és una habilitat fonamental en qualsevol àmbit en l'actualitat. Una aplicació habitual n'és la integració de dades de diferents fonts d'informació en un únic sistema de manera estructurada, segons un ús concret. L'objectiu d'aquest projecte és que l'alumnat s'introduïsca en aquest camp, dissenyant un magatzem de dades (DWH) que després implementarà de manera pràctica en una altra fase del projecte.</td>
    </tr>
    <tr>
        <th>Repte</th>
        <td>L'entitat per a la qual treballes vol fer ús de dades que es generen en diferents aplicacions, per analitzar-les de manera conjunta i crear taulers de control amb mètriques i gràfics. Eres l'arquitecte/a de dades de l'entitat i has de dissenyar el DWH que integrarà les dades. El disseny s'ha d'adaptar a l'activitat de l'entitat i a l'ús concret que es definisca al projecte, en l'acord amb la gestió de l'equip (professorat).</td>
    </tr>
    <tr>
        <th>Producte</th>
        <td>Documentació del DWH, incloent:
            <li>les tecnologies emprades en el DWH </li>
            <li>les ferramentes d'integració de dades emprades </li>
            <li>el diagrama de l'extracció i integració de les dades </li>
            <li>almenys un disseny lògic d'un model de dades que siga coherent amb l'activitat de l'entitat i l'ús concret definit </li> </td>
    </tr>
    <tr>
        <th>Resultats d'Aprenentatge</th>
        <td><b>RA1</b>. Aplica tècniques d'anàlisis de dades que integren, processen i analitzen la informació, adaptant i implementant sistemes que les utilitzen. <br> <b>RA3</b>. Gestiona i emmagatzema dades facilitant la recerca de respostes en conjunts grans de dades.</td>
    </tr>
    <tr>
        <th>Continguts</th>
        <td>Tècniques i procediments d'extracció i d'integració de dades (ETL, ELT). <br> Sistemes de gestió de emmagatzematge de dades. Ferramentes d'importació, integració i transformació de dades. <br> Programació. Modelat i arquitectura de dades. <br> Documentació tècnica. </td>
    </tr>
    <tr>
        <th>Criteris d'Avaluació</th>
        <td>RA1-b. S'han extret informació a partir de volums grans de dades. <br> RA1-c. S'han combinat diferents fonts i tipus de dades <br> RA1-d. S'ha construït un conjunt de dades complexes que s'han relacionat entre si. <br> RA1-e. S'han establert objectius i prioritats, s'ha organitzat i seqüenciat el temps de realització del projecte. <br> RA1-f. S'han seleccionat i integrat sistemes d'informació que cumplixen amb les necessitats del projecte. <br> RA1-g. S'han determinat els criteris de cost i qualitat necessaris per a la implementació eficaç i eficient del sistema de Big Data.<br> RA3-a S'han extret i emmagatzemat dades de diverses fonts, per ser processats en diferents escenaris. <br> RA3-b S'ha definit l'objectiu per aprofitar les dades. <br> RA3-c S'ha comprovat que la revolució digital exigix poder emmagatzemar i processar grans volums de dades de diferent tipus, així com descobrir el seu valor. <br> RA3-d S'han desenvolupat sistemes de gestió, emmagatzematge i processament de grans volums de dades de manera eficient i segura, tenint en compte la normativa existent.</td>
    </tr>
</table>

<br>   

Continguts
1. Introducció
2. Context
3. Elements curriculars
4. Descripció
5. Metodologia
6. Planificació
7. Avaluació

## 1. Introducció
L'objectiu d'aquest projecte és que l'alumnat dissenye un magatzem de dades que després implementarà de manera pràctica (en una altra fase del projecte). El magatzem de dades es dissenyarà en un context concret que s'acordarà amb el professorat a priori. En el disseny s'hauran d'incloure fonts d'informació diverses que s'integraran en el magatzem, mètodes d'integració, etapes de la integració i processament de dades en el magatzem, i almenys un disseny lògic de la integració d'un conjunt de dades que es relacionaran entre si amb un ús concret. 

## 2. Context
La Unitat de Treball "Disseny d'un magatzem de dades" s'emmarca en el mòdul "Sistemes de Big Data" dins el "Curs d'especialització de Formació Professional Superior d'Intel·ligència Artificial i Big Data". Aquesta UT es desenvolupa en el context educatiu particular definit a continuació.

### Ubicació i entorn socioeconòmic i cultural
L'IES Jaume II el Just està ubicat en la localitat de Tavernes de la Valldigna, el major nucli urbà de la Valldigna amb quasi 18.000 habitants, aproximadament.  

El seu entorn es caracteritza per una combinació d’activitat agrícola, un sector turístic important a causa de la proximitat a la costa, i una certa presència industrial en el sector de la construcció, del metall, l’agroalimentari i la fusta (mobles).  

Des del punt de vista sociocultural, Tavernes compta amb una població diversa, on conviuen famílies autòctones i una creixent presència de persones d’origen immigrant, principalment provinents de països com Romania, el Marroc i països d’Amèrica llatina.

Pel que fa a la llengua, Tavernes es troba dins d’una zona de predomini lingüístic valencià, com és la Valldigna, per la qual cosa la major part de la població és bilingüe en valencià i castellà. En l’àmbit educatiu, això suposa una especial atenció a la promoció del valencià com a llengua vehicular, a la vegada que es fomenta el multilingüisme amb l’aprenentatge de llengües estrangeres, preferentment l’anglés.

### Oferta d'ensenyaments
El centre impartix els estudis corresponents a l'Educació Secundària Obligatòria (ESO) i els de Batxillerat, en les modalitats de General, Humanitats i Ciències Socials, i Ciència i Tecnologia, en torn diürn i nocturn.

Pel que respecta a les ensenyances de Formació Professional, el centre impartix 5 cicles formatius de les família Informàtica i Comunicacions i 2 cursos
d’especialització:
- Cicle Formatiu de Grau Bàsic Informàtica d’Oficina
- Cicle formatiu de Grau Mitjà Sistemes Microinformàtics i xarxes
- Cicle Formatiu de Grau Superior Administració de Sistemes Informàtics en Xarxa
- Cicle Formatiu de Grau Superior Desenvolupament d’Aplicacions Multiplataforma
- Cicle Formatiu de Grau Superior Desenvolupament d’Aplicacions Web
- **Curs d’especialització en Inteligència Artificial i Big Data**
- Curs d’especialització en Ciberseguretat en Entorns de les Tecnologies de la Informació

Per altra banda, de la familia professional Agrària també s’impartixen 2 cicles formatius.

### Descripció del centre educatiu: instal·lacions i recursos
L'IES Jaume II el Just és un centre públic amb més 50 anys d’història. Va ser inaugurat l'any 1967, i compta amb una comunitat educativa composta per entre 900 i 1100 alumnes i un claustre d'aproximadament 130 docents.

Pel que fa a les instaŀlacions, l'institut disposa d'un pavelló específicament dedicat a l’ensenyament dels cicles formatius d'informàtica, equipat amb les aules i els recursos tecnològics necessaris per a la formació en aquest àmbit. També disposa d'espais específics per als cicles de la família agrícola.

El Jaume II el Just oferix altres espais que complementen l'activitat acadèmica i esportiva, com ara un pavelló esportiu, un saló d'actes on es desenvolupen diferents esdeveniments educatius i culturals, i una cafeteria. No obstant això, actualment la cafeteria roman tancada a l'espera del procés de licitació per a la seua gestió.  

Aquestes instaŀlacions i recursos garantixen un entorn d’aprenentatge òptim per a l’alumnat, promovent tant la formació acadèmica com el desenvolupament de competències tècniques, personals i socials necessàries per a la seua inserció en el món laboral o en educacions postobligatòries.

### Perfil de l'alumnat 
L'alumnat del centre prové predominantment de Tavernes i de diverses localitats pròximes. Presenta una gran diversitat de perfils acadèmics i personals degut a l’ample espectre d’opcions acadèmiques de les qual disposa: estudiants d'ESO, Batxillerat i Cicles Formatius de Grau Bàsic, Mitjà i Superior, amb interessos professionals i acadèmics molt diferents, per a les quals el centre oferix programes d'atenció a la diversitat i suport educatiu, definits al seu Pla d’Atenció a la Diversitat i Inclusió Educativa.

Pel que fa als Cicles Formatius, el centre compta amb alumnat interessat en la Formació Professional en àmbits com la informàtica i l’agricultura. L’alumnat d’aquests ensenyaments sol tindre un perfil més pràctic i orientat cap a la inserció laboral o la continuïtat en estudis superiors especialitzats. A més, dins de l'àmbit de la informàtica, el centre oferix dos cursos d'especialització dirigits a l’alumnat que vol aprofundir en aspectes concrets del sector tecnològic que estan molt d’actualitat, com són la Ciberseguretat i la Inteŀligència Artificial.

### Perfil professional
La competència general d'aquest curs d'especialització consistix a programar i aplicar sistemes "intel·ligents" per optimitzar la gestió de la informació i l'ús de les dades, garantint el seu accés de manera segura i seguint els criteris d'accessibilitat, usabilitat i qualitat que exigixen els estàndards establers, així com els principis ètics i legals rellevants.  

Les persones que obtenen el certificat de superació del curs poden exercir la seua activitat laboral en els àmbits de la programació, la infrastructura i la consultoria, especialment a:
- Desenvolupament de programari d'IA i Big Data
- Gestió de sistemes d'informació
- Anàlisi de dades

### La Unitat de Treball dins el Pla d'estudis

## 3. Elements curriculars
Mòdul Sistemes de Big Data (5074).  

### Resultats d'Aprenentatge
<b>RA1</b>. Aplica tècniques d'anàlisis de dades que integren, processen i analitzen la informació, adaptant i implementant sistemes que les utilitzen. 
<br> 
<b>RA3</b>. Gestiona i emmagatzema dades facilitant la recerca de respostes en conjunts grans de dades.  

### Continguts
Tècniques i procediments d'extracció i d'integració de dades (ETL, ELT). <br> Sistemes de gestió de emmagatzematge de dades. Ferramentes d'importació, integració i transformació de dades. <br> Programació. Modelat i arquitectura de dades. <br> Documentació tècnica.  

### Criteris d'Avaluació

## 4. Descripció
### Objectius

### Coneixements previs

### Desenvolupament 

### Entrega
Documentació del DWH, incloent:
    <li>les tecnologies emprades en el DWH 
    <li>les ferramentes d'integració de dades emprades
    <li>el diagrama de l'extracció i integració de les dades
    <li>almenys un disseny lògic d'un model de dades que siga coherent amb l'activitat de l'entitat i l'ús concret definit

### Recursos
MS Visio

## 5. Metodologia

## 6. Planificació

## 7. Avaluació
### Instruments d'avaluació
L'entrega seria en un format de documentació, no definida de moment.

### Mètodes d'avaluació

