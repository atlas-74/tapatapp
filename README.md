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

### **End-point 1: Llista d'usuaris**
- **Descripció**: Aquest endpoint retorna un missatge de benvinguda amb el text `"Hello World"`.
- **HOST**: `localhost:5000`
- **End-point (URL)**: `/lista`
- **Method**: `GET`
- **Tipus de petició (headers)**: No es requereixen headers específics.
- **Paràmetres que necessita la petició**: Cap.
- **Resposta**:
  - **Codi d'estat**: `200 OK`
  - **Cos de la resposta**: 
    ```plaintext
    "Hello World"
    ```

---

### **End-point 2: Prova de petició POST**
- **Descripció**: Aquest endpoint rep una petició POST amb un paràmetre `username` i el retorna com a resposta.
- **HOST**: `localhost:5000`
- **End-point (URL)**: `/provapost`
- **Method**: `POST`
- **Tipus de petició (headers)**: 
  - `Content-Type: application/x-www-form-urlencoded`
- **Paràmetres que necessita la petició**: 
  - `username` (exemple: `"usuari1"`)
- **Resposta**:
  - **Codi d'estat**: `200 OK`
  - **Cos de la resposta**: 
    ```json
    {
      "username": "usuari1"
    }
    ```

---

### **End-point 3: Obtenir usuari per username**
- **Descripció**: Aquest endpoint rep un `username` a través d'una petició GET i retorna la informació de l'usuari associat amb aquest nom d'usuari, si es troba. Si no es troba l'usuari, retorna un missatge d'error.
- **HOST**: `localhost:5000`
- **End-point (URL)**: `/user/<username>`
- **Method**: `GET`
- **Tipus de petició (headers)**: No es requereixen headers específics.
- **Paràmetres que necessita la petició**: 
  - `username` (exemple: `"usuari1"`)
- **Resposta**:
  - **Codi d'estat**: `200 OK` si l'usuari es troba.
  - **Cos de la resposta**: 
    ```json
    {
      "id": 1,
      "username": "usuari1",
      "password": "12345",
      "email": "prova@gmail.com"
    }
    ```
  - **Codi d'estat**: `404 Not Found` si no es troba l'usuari.
  - **Cos de la resposta**:
    ```json
    {
      "message": "User not found"
    }
    ```
