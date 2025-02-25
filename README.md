# tapatapp
# Descripció
[Descripció del Projecte TapatApp](descTapatApp.md)

## Texte
[Requeriments Tecnics del Projecte TapatApp](RequerimentsTecnics.md)\
[HTTP Request](HttpRequestResponse.md)

## DIAGRAMES
[Diagrama de Classes (Mermaid)](/charts/DiagramaClassesTapat.mermaid)\
[Diagrama de Fluxe (Mermaid)](charts/DiagramaFluxeSoftware.mermaid)

# Definició dels EndPoints del WebService

### **End-point 1: Es troba usuari**
- **Descripció**: Aquest endpoint retorna un missatge de benvinguda amb el text `"Hello World"`.
- **HOST**: `localhost:5000`
- **End-point (URL)**: `/tapatapp/getuser`
- **Method**: `GET`
- **Tipus de petició: application/json.**
- **Paràmetres: username(string).**
- **Resposta**:
  - **Codi d'estat**: `200 OK`
  - **Cos de la resposta**: 
    ```plaintext
    "Hello World"
    ```

---

#### **End-point 2: No es troba usuari**
- **Descripció**: Aquest endpoint retorna un missatge indicant que no s'ha trobat `"No s'ha trobat l'usuari"`.
- **HOST**: `localhost:5000`
- **End-point (URL)**: `/tapatapp/getuser`
- **Method**: `GET`
- **Tipus de petició: application/json.**
- **Paràmetres: username(string).**
- **Resposta**:
  - **Codi d'estat**: `404`
  - **Cos de la resposta**: 
    ```plaintext
    "No s'ha trobat l'usuari"
    ```

---

#### **End-point 3: No s'ha rebut l'informació requerida**
- **Descripció**: Aquest endpoint retorna un missatge l'error `"Error. Cerca o tipus de dada incorrecta"`.
- **HOST**: `localhost:5000`
- **End-point (URL)**: `/tapatapp/getuser`
- **Method**: `GET`
- **Tipus de petició: application/json.**
- **Paràmetres: username(string).**
- **Resposta**:
  - **Codi d'estat**: `400`
  - **Cos de la resposta**: 
    ```plaintext
    "Error. Cerca o tipus de dada incorrecta"
    ```
---    
# Imatges

## Wireframe
![Imatge Wireframe](/img/wireframeCaptura.PNG)

---

# Descripciones de Vista

## Vista de Login:
- **Descripció:** Pantalla de Login on l'usuari es validarà.
- **Info. Entrada:** Username o email, Password.
- **Info. Vista:** None.

---

## Vista de Login OK?:
- **Descripció:** Verificació de les credencials de l'usuari. Si són correctes, l'usuari accedeix al Lobby.
- **Info. Entrada:** Username o email, Password.
- **Info. Vista:** Lobby o Missatge d'error si les credencials són incorrectes.

---

## Vista de Lobby:
- **Descripció:** Pantalla principal des d'on l'usuari pot accedir a diferents seccions de l'aplicació.
- **Info. Entrada:** Cap.
- **Info. Vista:** Accions per accedir a altres seccions.

---

## Vista de Infant:
- **Descripció:** Pantalla on es mostra i gestiona el perfil d'un nen registrat en l'aplicació.
- **Info. Entrada:** Cap.
- **Info. Vista:** Informació del nen i opcions de gestió.

---

## Vista de Estat Tap:
- **Descripció:** Pantalla per gestionar si l'infant té el tap posat o no.
- **Info. Entrada:** Cap.
- **Info. Vista:** Informació sobre l'estat del tap.

---

## Vista de Progrés Tap:
- **Descripció:** Pantalla per controlar el temps restant del pegat oftàlmic.
- **Info. Entrada:** Cap.
- **Info. Vista:** Temps restant del pegat.

---

## Vista de Tancar Sessió:
- **Descripció:** Opció per tancar la sessió de l'usuari i tornar a la pantalla de Login.
- **Info. Entrada:** Cap.
- **Info. Vista:** Pantalla de Login.

---
