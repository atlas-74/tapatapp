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
