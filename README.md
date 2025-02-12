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

# Descripcions de Vista
**Vista de Login:**

- **Descripció:** Pantalla de Login on l'usuari es validarà.
- **Info. Entrada:** Username o email, Password.
- **Info. Vista:** None.
-----
**Vista de Login OK?:**

- **Descripció:** Verificació de les credencials de l'usuari. Si són correctes, l'usuari accedeix al Lobby.
- **Info. Entrada:** Username o email, Password.
- **Info. Vista:** Lobby o Missatge d'error si les credencials són incorrectes.
-----
**Vista de Lobby:**

- **Descripció:** Pantalla principal des d'on l'usuari pot accedir a diferents seccions de l'aplicació.
- **Info. Entrada:** None.
- **Info. Vista:** Accions per accedir a altres seccions.
-----
**Vista de Error de Login:**

- **Descripció:** Missatge d'error per a les credencials incorrectes, amb opció de tornar-ho a intentar.
- **Info. Entrada:** None.
- **Info. Vista:** Missatge d'error i formulari de Login.
-----
**Vista de Registre:**

- **Descripció:** Formulari de Registre d'Usuari.
- **Info. Entrada:** username, password, email, telèfon, adreça.
- **Info. Vista:** None.
-----
**Vista de Registre OK?:**

- **Descripció:** Verificació del registre de l'usuari. Si és reeixit, s'accedeix al Lobby.
- **Info. Entrada:** username, password, mail, telèfon, adreça.
- **Info. Vista:** Lobby o Missatge d'error si el registre no és correcte.
-----
**Vista de Error de Registre:**

- **Descripció:** Missatge indicant que hi ha hagut un problema amb el registre de l'usuari.
- **Info. Entrada:** None.
- **Info. Vista:** Missatge d'error.
-----
**Vista de Perfil Nen:**

- **Descripció:** Pantalla on es mostra i gestiona el perfil d'un nen registrat en l'aplicació.
- **Info. Entrada:** None.
- **Info. Vista:** Informació del nen i opcions de gestió.
-----
**Vista de Perfil Tutor:**

- **Descripció:** Vista per gestionar la informació del tutor o cuidador.
- **Info. Entrada:** None.
- **Info. Vista:** Informació del tutor o cuidador.
-----
**Vista de Tractaments:**

- **Descripció:** Secció on s'administren els tractaments mèdics de l'usuari.
- **Info. Entrada:** None.
- **Info. Vista:** Llista de tractaments mèdics de l'usuari.
-----
**Vista de Temps de Pegat:**

- **Descripció:** Pantalla per controlar el temps restant del pegat oftàlmic.
- **Info. Entrada:** None.
- **Info. Vista:** Temps restant del pegat.
-----
**Vista de Configuració:**

- **Descripció:** Opcions per personalitzar l'aplicació, canviar preferències i gestionar comptes.
- **Info. Entrada:** None.
- **Info. Vista:** Opcions de configuració i preferències.
-----
**Vista de Tancar Sessió:**

- **Descripció:** Opció per tancar la sessió de l'usuari i tornar a la pantalla de Login.
- **Info. Entrada:** None.
- **Info. Vista:** Pantalla de Login.
-----
**Vista de Vaig oblidar la meva Contrasenya:**

- **Descripció:** Pantalla on els usuaris poden recuperar la seva contrasenya ingressant el seu email.
- **Info. Entrada:** E-mail.
- **Info. Vista:** Instruccions per recuperar la contrasenya.
-----
**Vista de Recepta Mèdica:**

- **Descripció:** Secció dins de Tractaments on s'emmagatzemen i consulten receptes mèdiques.
- **Info. Entrada:** None.
- **Info. Vista:** Llista de receptes mèdiques.
-----
**Vista de Perfil Doctors:**

- **Descripció:** Llistat dels metges associats al tractament de l'usuari.
- **Info. Entrada:** None.
- **Info. Vista:** Llista de metges.
-----
**Vista de Procediments:**

- **Descripció:** Registre dels procediments mèdics realitzats o programats.
- **Info. Entrada:** None.
- **Info. Vista:** Llista de procediments mèdics.
-----
**Vista de Temps Restant Pegat:**

- **Descripció:** Vista que mostra el temps restant abans de retirar o canviar el pegat oftàlmic.
- **Info. Entrada:** None.
- **Info. Vista:** Temps restant per retirar o canviar el pegat.
-----
