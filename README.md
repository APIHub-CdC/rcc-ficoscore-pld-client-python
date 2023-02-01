# rcc-ficoscore-pld-client-python 

<p>Reporta el historial crediticio; el cumplimiento de pago de los compromisos que la persona ha adquirido con entidades financieras, no financieras e instituciones comerciales que dan crédito o participan en actividades afines al crédito; y filtra contra listas de cumplimiento para Prevención de Lavado de Dinero..<br/><img src='https://developer.circulodecredito.com.mx/sites/default/files/2020-10/circulo_de_credito-apihub.png' height='40' width='220'/></p><br/>


## Requisitos

Python 3.4+

## Instalación

### Setuptools

Instalacion via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` instala el paquete para todos los usuarios)


*Nota:* En caso de tener problemas en la instalacion del cryptography en mac con procesador M1, esta seria una solucion para este problema:
```
pip3 uninstall cryptography
pip3 uninstall cffi
LDFLAGS="-L$(brew --prefix openssl@1.1)/lib" CFLAGS="-I$(brew --prefix openssl@1.1)/include" pip3 install cryptography
```


Then import the package:
```python
import rcc_fico_pld_client
```

## Guía de inicio

## Guía de inicio

### Paso 1. Generar llave y certificado
Antes de lanzar la prueba se deberá tener un keystore para la llave privada y el certificado asociado a ésta.
Para generar el keystore se ejecutan las instrucciones que se encuentran en ***/createKeystore.sh*** ó con los siguientes comandos:

**Opcional**: Si desea cifrar su contenedor, coloque una contraseña en una variable de ambiente.

```shell
export KEY_PASSWORD=your_super_secure_password
```

**Opcional**: Si desea cifrar su keystore, coloque una contraseña en una variable de ambiente.

```shell
export KEYSTORE_PASSWORD=your_super_secure_keystore_password
```

- Definición de los nombres de archivos y alias.

```shell
export PRIVATE_KEY_FILE=pri_key.pem
export CERTIFICATE_FILE=certificate.pem
export SUBJECT=/C=MX/ST=MX/L=MX/O=CDC/CN=CDC
export PKCS12_FILE=keypair.p12
export KEYSTORE_FILE=keystore.jks
export ALIAS=cdc
```
- Generar llave y certificado.

```shell
# Genera la llave privada.
openssl ecparam -name secp384r1 -genkey -out ${PRIVATE_KEY_FILE}

# Genera el certificado público
openssl req -new -x509 -days 365 \
  -key ${PRIVATE_KEY_FILE} \
  -out ${CERTIFICATE_FILE} \
  -subj "${SUBJECT}"

```

- Generar contenedor PKCS12 a partir de la llave privada y el certificado

```shell
# Genera el archivo pkcs12 a partir de la llave privada y el certificado.
# Deberá empaquetar su llave privada y el certificado.

openssl pkcs12 -name ${ALIAS} \
  -export -out ${PKCS12_FILE} \
  -inkey ${PRIVATE_KEY_FILE} \
  -in ${CERTIFICATE_FILE} \
  -password pass:${KEY_PASSWORD}

```

- Generar un keystore dummy y eliminar su contenido.

```sh
#Genera un Keystore con un par de llaves dummy.
keytool -genkey -alias dummy -keyalg RSA \
    -keysize 2048 -keystore ${KEYSTORE_FILE} \
    -dname "CN=dummy, OU=, O=, L=, S=, C=" \
    -storepass ${KEYSTORE_PASSWORD} -keypass ${KEY_PASSWORD}
#Elimina el par de llaves dummy.
keytool -delete -alias dummy \
    -keystore ${KEYSTORE_FILE} \
    -storepass ${KEYSTORE_PASSWORD}
```

- Importar el contenedor PKCS12 al keystore

```sh
#Importamos el contenedor PKCS12
keytool -importkeystore -srckeystore ${PKCS12_FILE} \
  -srcstoretype PKCS12 \
  -srcstorepass ${KEY_PASSWORD} \
  -destkeystore ${KEYSTORE_FILE} \
  -deststoretype JKS -storepass ${KEYSTORE_PASSWORD} \
  -alias ${ALIAS}
#Lista el contenido del Kesystore para verificar que
keytool -list -keystore ${KEYSTORE_FILE} \
  -storepass ${KEYSTORE_PASSWORD}
```

### Paso 2. Carga del certificado dentro del portal de desarrolladores
 1. Iniciar sesión.
 2. Dar clic en la sección "**Mis aplicaciones**".
 3. Seleccionar la aplicación.
 4. Ir a la pestaña de "**Certificados para @tuApp**".
    <p align="center">
      <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/applications.png">
    </p>
 5. Al abrirse la ventana emergente, seleccionar el certificado previamente creado y dar clic en el botón "**Cargar**":
    <p align="center">
      <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/upload_cert.png" width="268">
    </p>
### Paso 3. Descarga del certificado de Círculo de Crédito dentro del portal de desarrolladores
 1. Iniciar sesión.
 2. Dar clic en la sección "**Mis aplicaciones**".
 3. Seleccionar la aplicación.
 4. Ir a la pestaña de "**Certificados para @tuApp**".
    <p align="center">
        <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/applications.png">
    </p>
 5. Al abrirse la ventana emergente, dar clic al botón "**Descargar**":
    <p align="center">
        <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/download_cert.png" width="268">
    </p>




### Paso 4. Modificar archivo de configuraciones

Los siguientes datos a modificar se encuentran en ***config.ini***

Para hacer uso del certificado que se descargó y el keystore que se creó se deberán modificar las rutas que se encuentran e

Es importante modificar el archivo config.ini que se encargará de inicializar la url. Modificar la URL ***('host')***, como se muestra en el siguiente fragmento de código:

```ini
[CERTIFICATEINFO]
key_password = your_key_password
pathKeypair = /your_path/keypair.p12
pathCertificateCdc = /your_path/cdc_cert.pem


[API_CONFIG]
host = https://services.circulodecredito.com.mx
username = YOUR_USERNAME_CIRCULO
password = YOUR_PASSSWORD_CIRCULO
x_api_key = YOUT_XAPIKEY
```

De igual manera, en el archivo **testRCC.py**, se deberá modificar el siguiente fragmento de código con los datos correspondientes:

```python
 
    def test_reporte(self):
        body = PersonaPeticion(
            apellido_paterno="APELLIDO_PATERNO",
            apellido_materno="APELLIDO_MATERNO",
            apellido_adicional=None,
            primer_nombre="PRIMER_NOMBRE",
            segundo_nombre=None,
            fecha_nacimiento="YYYY-MM-DD",
            rfc="RFC",
            curp=None,
            nacionalidad="mx",
            residencia=None,
            estado_civil=None,
            sexo=None,
            clave_elector_ife=None,
            numero_dependientes=None,
            fecha_defuncion=None,
            domicilio=DomicilioPeticion( 
                direccion="DIRECCION",
                colonia_poblacion="COLONIA", 
                delegacion_municipio="MUNICIPIO", 
                ciudad= "CIUDAD", 
                estado="ESTADO", 
                cp="CODIGO_POSTAL", 
                fecha_residencia="YYYY-MM-DD", 
                numero_telefono=None, 
                tipo_domicilio=None, 
                tipo_asentamiento=None)
        )
        try:
   
            api_response=self.api.get_reporte( x_api_key=self.x_api_key, username=self.username, password=self.password, request=body)
            print(api_response)
        except ApiException as e:
            print("Exception when calling TestRCC->test_reporte: %s\n" % e)

```

### Paso 3. Ejecutar la prueba unitaria

Teniendo los pasos anteriores ya solo falta ejecutar la prueba unitaria, con el siguiente comando:

```shell
python3 testRCC.py
```
 

---
[CONDICIONES DE USO, REPRODUCCIÓN Y DISTRIBUCIÓN](https://github.com/APIHub-CdC/licencias-cdc)

[1]: https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos