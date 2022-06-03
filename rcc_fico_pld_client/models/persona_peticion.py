# coding: utf-8


import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_client.configuration import Configuration


class PersonaPeticion(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'apellido_paterno': 'str',
        'apellido_materno': 'str',
        'apellido_adicional': 'str',
        'primer_nombre': 'str',
        'segundo_nombre': 'str',
        'fecha_nacimiento': 'str',
        'rfc': 'str',
        'curp': 'str',
        'nacionalidad': 'str',
        'residencia': 'CatalogoResidencia',
        'estado_civil': 'CatalogoEstadoCivil',
        'sexo': 'CatalogoSexo',
        'clave_elector_ife': 'str',
        'numero_dependientes': 'int',
        'fecha_defuncion': 'str',
        'domicilio': 'DomicilioPeticion'
    }

    attribute_map = {
        'apellido_paterno': 'apellidoPaterno',
        'apellido_materno': 'apellidoMaterno',
        'apellido_adicional': 'apellidoAdicional',
        'primer_nombre': 'primerNombre',
        'segundo_nombre': 'segundoNombre',
        'fecha_nacimiento': 'fechaNacimiento',
        'rfc': 'RFC',
        'curp': 'CURP',
        'nacionalidad': 'nacionalidad',
        'residencia': 'residencia',
        'estado_civil': 'estadoCivil',
        'sexo': 'sexo',
        'clave_elector_ife': 'claveElectorIFE',
        'numero_dependientes': 'numeroDependientes',
        'fecha_defuncion': 'fechaDefuncion',
        'domicilio': 'domicilio'
    }

    def __init__(self, apellido_paterno=None, apellido_materno=None, apellido_adicional=None, primer_nombre=None, segundo_nombre=None, fecha_nacimiento=None, rfc=None, curp=None, nacionalidad=None, residencia=None, estado_civil=None, sexo=None, clave_elector_ife=None, numero_dependientes=None, fecha_defuncion=None, domicilio=None, _configuration=None):  # noqa: E501
        """PersonaPeticion - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._apellido_paterno = None
        self._apellido_materno = None
        self._apellido_adicional = None
        self._primer_nombre = None
        self._segundo_nombre = None
        self._fecha_nacimiento = None
        self._rfc = None
        self._curp = None
        self._nacionalidad = None
        self._residencia = None
        self._estado_civil = None
        self._sexo = None
        self._clave_elector_ife = None
        self._numero_dependientes = None
        self._fecha_defuncion = None
        self._domicilio = None
        self.discriminator = None

        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        if apellido_adicional is not None:
            self.apellido_adicional = apellido_adicional
        self.primer_nombre = primer_nombre
        if segundo_nombre is not None:
            self.segundo_nombre = segundo_nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        if curp is not None:
            self.curp = curp
        self.nacionalidad = nacionalidad
        if residencia is not None:
            self.residencia = residencia
        if estado_civil is not None:
            self.estado_civil = estado_civil
        if sexo is not None:
            self.sexo = sexo
        if clave_elector_ife is not None:
            self.clave_elector_ife = clave_elector_ife
        if numero_dependientes is not None:
            self.numero_dependientes = numero_dependientes
        if fecha_defuncion is not None:
            self.fecha_defuncion = fecha_defuncion
        self.domicilio = domicilio

    @property
    def apellido_paterno(self):
        """Gets the apellido_paterno of this PersonaPeticion.  # noqa: E501

        Apellido paterno de la persona. Sin abreviaturas o iniciales  # noqa: E501

        :return: The apellido_paterno of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self, apellido_paterno):
        """Sets the apellido_paterno of this PersonaPeticion.

        Apellido paterno de la persona. Sin abreviaturas o iniciales  # noqa: E501

        :param apellido_paterno: The apellido_paterno of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and apellido_paterno is None:
            raise ValueError("Invalid value for `apellido_paterno`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                apellido_paterno is not None and len(apellido_paterno) > 30):
            raise ValueError("Invalid value for `apellido_paterno`, length must be less than or equal to `30`")  # noqa: E501

        self._apellido_paterno = apellido_paterno

    @property
    def apellido_materno(self):
        """Gets the apellido_materno of this PersonaPeticion.  # noqa: E501

        Apellido materno de la persona  # noqa: E501

        :return: The apellido_materno of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._apellido_materno

    @apellido_materno.setter
    def apellido_materno(self, apellido_materno):
        """Sets the apellido_materno of this PersonaPeticion.

        Apellido materno de la persona  # noqa: E501

        :param apellido_materno: The apellido_materno of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and apellido_materno is None:
            raise ValueError("Invalid value for `apellido_materno`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                apellido_materno is not None and len(apellido_materno) > 30):
            raise ValueError("Invalid value for `apellido_materno`, length must be less than or equal to `30`")  # noqa: E501

        self._apellido_materno = apellido_materno

    @property
    def apellido_adicional(self):
        """Gets the apellido_adicional of this PersonaPeticion.  # noqa: E501

        Apellido adicional de la persona, si tuviere  # noqa: E501

        :return: The apellido_adicional of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._apellido_adicional

    @apellido_adicional.setter
    def apellido_adicional(self, apellido_adicional):
        """Sets the apellido_adicional of this PersonaPeticion.

        Apellido adicional de la persona, si tuviere  # noqa: E501

        :param apellido_adicional: The apellido_adicional of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                apellido_adicional is not None and len(apellido_adicional) > 30):
            raise ValueError("Invalid value for `apellido_adicional`, length must be less than or equal to `30`")  # noqa: E501

        self._apellido_adicional = apellido_adicional

    @property
    def primer_nombre(self):
        """Gets the primer_nombre of this PersonaPeticion.  # noqa: E501

        Primer nombre de la persona  # noqa: E501

        :return: The primer_nombre of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._primer_nombre

    @primer_nombre.setter
    def primer_nombre(self, primer_nombre):
        """Sets the primer_nombre of this PersonaPeticion.

        Primer nombre de la persona  # noqa: E501

        :param primer_nombre: The primer_nombre of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and primer_nombre is None:
            raise ValueError("Invalid value for `primer_nombre`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                primer_nombre is not None and len(primer_nombre) > 50):
            raise ValueError("Invalid value for `primer_nombre`, length must be less than or equal to `50`")  # noqa: E501

        self._primer_nombre = primer_nombre

    @property
    def segundo_nombre(self):
        """Gets the segundo_nombre of this PersonaPeticion.  # noqa: E501

        Segundo nombre de la persona  # noqa: E501

        :return: The segundo_nombre of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._segundo_nombre

    @segundo_nombre.setter
    def segundo_nombre(self, segundo_nombre):
        """Sets the segundo_nombre of this PersonaPeticion.

        Segundo nombre de la persona  # noqa: E501

        :param segundo_nombre: The segundo_nombre of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                segundo_nombre is not None and len(segundo_nombre) > 50):
            raise ValueError("Invalid value for `segundo_nombre`, length must be less than or equal to `50`")  # noqa: E501

        self._segundo_nombre = segundo_nombre

    @property
    def fecha_nacimiento(self):
        """Gets the fecha_nacimiento of this PersonaPeticion.  # noqa: E501

        Fecha de nacimiento de la persona, en el formato especificado (por defecto yyyy-MM-dd)  # noqa: E501

        :return: The fecha_nacimiento of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        """Sets the fecha_nacimiento of this PersonaPeticion.

        Fecha de nacimiento de la persona, en el formato especificado (por defecto yyyy-MM-dd)  # noqa: E501

        :param fecha_nacimiento: The fecha_nacimiento of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fecha_nacimiento is None:
            raise ValueError("Invalid value for `fecha_nacimiento`, must not be `None`")  # noqa: E501

        self._fecha_nacimiento = fecha_nacimiento

    @property
    def rfc(self):
        """Gets the rfc of this PersonaPeticion.  # noqa: E501

        RFC con homoclave de la persona  # noqa: E501

        :return: The rfc of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this PersonaPeticion.

        RFC con homoclave de la persona  # noqa: E501

        :param rfc: The rfc of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and rfc is None:
            raise ValueError("Invalid value for `rfc`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                rfc is not None and len(rfc) > 13):
            raise ValueError("Invalid value for `rfc`, length must be less than or equal to `13`")  # noqa: E501

        self._rfc = rfc

    @property
    def curp(self):
        """Gets the curp of this PersonaPeticion.  # noqa: E501

        CURP de la persona, emitida por RENAPO  # noqa: E501

        :return: The curp of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._curp

    @curp.setter
    def curp(self, curp):
        """Sets the curp of this PersonaPeticion.

        CURP de la persona, emitida por RENAPO  # noqa: E501

        :param curp: The curp of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                curp is not None and len(curp) > 18):
            raise ValueError("Invalid value for `curp`, length must be less than or equal to `18`")  # noqa: E501

        self._curp = curp

    @property
    def nacionalidad(self):
        """Gets the nacionalidad of this PersonaPeticion.  # noqa: E501

        <p>Debe contener la clave de la nacionalidad del consumidor los valores posibles son los siguientes:</p><p><table><thead><tr><th>Clave</th><th>Nacionalidad</th><th>País</th></tr></thead><tbody><tr><td>AD</td><td>Andorra</td><td>Andorra</td></tr><tr><td>AF</td><td>Afgana</td><td>Afganistán</td></tr><tr><td>AG</td><td>Antigua y Barbado</td><td>Antigua y Barbado</td></tr><tr><td>AI</td><td>Anguila</td><td>Anguila</td></tr><tr><td>AN</td><td>Albania</td><td>Albania</td></tr><tr><td>AO</td><td>Angola</td><td>Angola</td></tr><tr><td>AS</td><td>Ascensión</td><td>Ascensión</td></tr><tr><td>AT</td><td>Argentina</td><td>Argentina</td></tr><tr><td>AU</td><td>Australiana</td><td>Australia</td></tr><tr><td>AW</td><td>Árabe</td><td>Arabia</td></tr><tr><td>AX</td><td>Azores</td><td>Azores</td></tr><tr><td>BB</td><td>Barbados</td><td>Barbados</td></tr><tr><td>BD</td><td>Bangladesh</td><td>Bangladesh</td></tr><tr><td>BE</td><td>Belga</td><td>Bélgica</td></tr><tr><td>BF</td><td>Burkina</td><td>Burkina</td></tr><tr><td>BG</td><td>Búlgara</td><td>Bulgaria</td></tr><tr><td>BH</td><td>Bahrein</td><td>Bahrein</td></tr><tr><td>BI</td><td>Burundi</td><td>Burundi</td></tr><tr><td>BJ</td><td>Benin</td><td>Benin</td></tr><tr><td>BK</td><td>Birmania</td><td>Birmania</td></tr><tr><td>BM</td><td>Bután</td><td>Bután</td></tr><tr><td>BN</td><td>Brunei</td><td>Brunei</td></tr><tr><td>BO</td><td>Boliviana</td><td>Bolivia</td></tr><tr><td>BR</td><td>Brasileño</td><td>Brasil</td></tr><tr><td>BS</td><td>Bahamas</td><td>Bahamas</td></tr><tr><td>BU</td><td>Bermudas</td><td>Bermudas</td></tr><tr><td>BW</td><td>Botswana</td><td>Botswana</td></tr><tr><td>BX</td><td>Bosnia Herzegovina</td><td>Bosnia Herzegovina</td></tr><tr><td>BZ</td><td>Belice</td><td>Belice</td></tr><tr><td>CB</td><td>Colombiana</td><td>Colombia</td></tr><tr><td>CC</td><td>Córcega</td><td>Córcega</td></tr><tr><td>CD</td><td>Chad</td><td>Chad</td></tr><tr><td>CF</td><td>Rep. Central Africana</td><td>Rep. Central Africana</td></tr><tr><td>CG</td><td>Congo</td><td>Congo</td></tr><tr><td>CH</td><td>Liechtenstein</td><td>Liechtenstein</td></tr><tr><td>CI</td><td>Islas Caimán</td><td>Islas Caimán</td></tr><tr><td>CJ</td><td>Comoros</td><td>Comoros</td></tr><tr><td>CL</td><td>Chilena</td><td>Chile</td></tr><tr><td>CM</td><td>Camerunés</td><td>Camerún</td></tr><tr><td>CN</td><td>Canadiense</td><td>Canadá</td></tr><tr><td>CP</td><td>China</td><td>China (Pekín)</td></tr><tr><td>CS</td><td>República Checa Eslovaca</td><td>República Checa Eslovaca</td></tr><tr><td>CU</td><td>Cariacou</td><td>Cariacou</td></tr><tr><td>CV</td><td>Cabo Verde</td><td>Cabo Verde</td></tr><tr><td>CY</td><td>Chipre</td><td>Chipre</td></tr><tr><td>DF</td><td>Austriaca</td><td>Austria</td></tr><tr><td>DJ</td><td>Djibouti</td><td>Djibouti</td></tr><tr><td>DK</td><td>Danés</td><td>Dinamarca</td></tr><tr><td>DM</td><td>Dominicana</td><td>Dominicana</td></tr><tr><td>DO</td><td>Dominicana</td><td>República Dominicana</td></tr><tr><td>DW</td><td>Alemana</td><td>Alemania</td></tr><tr><td>DZ</td><td>Argelia</td><td>Argelia</td></tr><tr><td>EC</td><td>Ecuatoriana</td><td>Ecuador</td></tr><tr><td>EG</td><td>Egipcia</td><td>Egipto</td></tr><tr><td>EM</td><td>Timor Oriental</td><td>Timor Oriental</td></tr><tr><td>ES</td><td>Española</td><td>España</td></tr><tr><td>ET</td><td>Etiopia</td><td>Etiopia</td></tr><tr><td>FA</td><td>Islas Falkland (Malvinas)</td><td>Islas Falkland (Malvinas)</td></tr><tr><td>FE</td><td>Islas Faroe</td><td>Islas Faroe</td></tr><tr><td>FI</td><td>Finlandia</td><td>Finlandia</td></tr><tr><td>FJ</td><td>Fiji</td><td>Fiji</td></tr><tr><td>FP</td><td>Polinesia</td><td>Polinesia</td></tr><tr><td>FR</td><td>Francesa</td><td>Francia</td></tr><tr><td>GB</td><td>Gabón</td><td>Gabón</td></tr><tr><td>GD</td><td>Granada</td><td>Granada</td></tr><tr><td>GE</td><td>Groenlandia</td><td>Groenlandia</td></tr><tr><td>GF</td><td>Guayana Francesa</td><td>Guayana Francesa</td></tr><tr><td>GH</td><td>Ghana</td><td>Ghana</td></tr><tr><td>GI</td><td>Gibraltar</td><td>Gibraltar</td></tr><tr><td>GM</td><td>Gambia</td><td>Gambia</td></tr><tr><td>GN</td><td>Guinea</td><td>Guinea</td></tr><tr><td>GP</td><td>Guadalupe</td><td>Guadalupe</td></tr><tr><td>GQ</td><td>Guinea Ecuatorial</td><td>Guinea Ecuatorial</td></tr><tr><td>GR</td><td>Griega</td><td>Grecia</td></tr><tr><td>GT</td><td>Guatemalteca</td><td>Guatemala</td></tr><tr><td>GW</td><td>Guinea Bissau</td><td>Guinea Bissau</td></tr><tr><td>GX</td><td>República De Georgia</td><td>República De Georgia</td></tr><tr><td>GY</td><td>Guyana</td><td>Guyana</td></tr><tr><td>HA</td><td>Haitiana</td><td>Haití</td></tr><tr><td>HK</td><td>Hong Kong</td><td>Hong Kong</td></tr><tr><td>HN</td><td>Hondureña</td><td>Honduras</td></tr><tr><td>HR</td><td>Cubano</td><td>Cuba</td></tr><tr><td>HU</td><td>Húngara</td><td>Húngara</td></tr><tr><td>HX</td><td>Croata</td><td>Croacia</td></tr><tr><td>IB</td><td>India</td><td>India</td></tr><tr><td>IC</td><td>Costa De Marfil</td><td>Costa De Marfil</td></tr><tr><td>IE</td><td>Irlandesa</td><td>Irlandesa</td></tr><tr><td>IF</td><td>Indonesia</td><td>Indonesia</td></tr><tr><td>IG</td><td>Israelí</td><td>Israelí</td></tr><tr><td>IQ</td><td>Iraquí</td><td>Iraquí</td></tr><tr><td>IR</td><td>Iraní</td><td>Iraní</td></tr><tr><td>IS</td><td>Islandia</td><td>Islandia</td></tr><tr><td>IT</td><td>Italiano</td><td>Italiano</td></tr><tr><td>JM</td><td>Jamaicano</td><td>Jamaicano</td></tr><tr><td>JO</td><td>Jordano</td><td>Jordano</td></tr><tr><td>JP</td><td>Japonesa</td><td>Japonesa</td></tr><tr><td>KA</td><td>Kampuchea</td><td>Kampuchea</td></tr><tr><td>KE</td><td>Kenya</td><td>Kenya</td></tr><tr><td>KI</td><td>Kiribati</td><td>Kiribati</td></tr><tr><td>KN</td><td>San Cristóbal De Neváis</td><td>San Cristóbal De Neváis</td></tr><tr><td>KR</td><td>Corea Del Sur</td><td>Corea Del Sur</td></tr><tr><td>KW</td><td>Kuwait</td><td>Kuwait</td></tr><tr><td>KX</td><td>Corea Del Norte</td><td>Corea Del Norte</td></tr><tr><td>LB</td><td>Libanes</td><td>Libanes</td></tr><tr><td>LC</td><td>Santa Lucia</td><td>Santa Lucia</td></tr><tr><td>LE</td><td>Islas De Sotavento</td><td>Islas De Sotavento</td></tr><tr><td>LK</td><td>Sri Lanka</td><td>Sri Lanka</td></tr><tr><td>LO</td><td>Laos</td><td>Laos</td></tr><tr><td>LR</td><td>Liberia</td><td>Liberia</td></tr><tr><td>LS</td><td>Lesotho</td><td>Lesotho</td></tr><tr><td>LT</td><td>Lituania</td><td>Lituania</td></tr><tr><td>LU</td><td>Luxemburgo</td><td>Luxemburgo</td></tr><tr><td>LV</td><td>Libia</td><td>Libia</td></tr><tr><td>LX</td><td>Letonia</td><td>Letonia</td></tr><tr><td>MC</td><td>Mongolia</td><td>Mongolia</td></tr><tr><td>MD</td><td>Madeira</td><td>Madeira</td></tr><tr><td>MG</td><td>Madagascar</td><td>Madagascar</td></tr><tr><td>MH</td><td>Macedonia</td><td>Macedonia</td></tr><tr><td>MJ</td><td>Macao</td><td>Macao</td></tr><tr><td>MK</td><td>Montserrat</td><td>Montserrat</td></tr><tr><td>ML</td><td>Mali</td><td>Mali</td></tr><tr><td>MM</td><td>Montenegro</td><td>Montenegro</td></tr><tr><td>MP</td><td>Sao Tome y Principado</td><td>Sao Tome y Principado</td></tr><tr><td>MQ</td><td>Martinico</td><td>Martinico</td></tr><tr><td>MR</td><td>Mauritania</td><td>Mauritania</td></tr><tr><td>MT</td><td>Malta</td><td>Malta</td></tr><tr><td>MU</td><td>Mauricio</td><td>Mauricio</td></tr><tr><td>MV</td><td>Maldivas</td><td>Maldivas</td></tr><tr><td>MW</td><td>Malawi</td><td>Malawi</td></tr><tr><td>MX</td><td>Mexicana</td><td>México</td></tr><tr><td>MY</td><td>Malasia</td><td>Malasia</td></tr><tr><td>MZ</td><td>Mozambique</td><td>Mozambique</td></tr><tr><td>NA</td><td>Nauru</td><td>Nauru</td></tr><tr><td>ND</td><td>No Definido</td><td>No Definido</td></tr><tr><td>NI</td><td>Nicaragua</td><td>Nicaragua</td></tr><tr><td>NL</td><td>Holandesa</td><td>Holanda</td></tr><tr><td>NN</td><td>Antillas Holandesas</td><td>Antillas Holandesas</td></tr><tr><td>NO</td><td>Noruega</td><td>Noruega</td></tr><tr><td>NP</td><td>Nepal</td><td>Nepal</td></tr><tr><td>NR</td><td>Nigeriano</td><td>Nigeria</td></tr><tr><td>NW</td><td>Nueva Caledonia</td><td>Nueva Caledonia</td></tr><tr><td>NZ</td><td>Nueva Zelandia</td><td>Nueva Zelandia</td></tr><tr><td>OA</td><td>Katar</td><td>Katar</td></tr><tr><td>OM</td><td>Omán</td><td>Omán</td></tr><tr><td>PG</td><td>Papúa Nueva Guinea</td><td>Papúa Nueva Guinea</td></tr><tr><td>PH</td><td>Filipinas</td><td>Filipinas</td></tr><tr><td>PK</td><td>Pakistán</td><td>Pakistán</td></tr><tr><td>PL</td><td>Polaco</td><td>Polonia</td></tr><tr><td>PM</td><td>Panameño</td><td>Panamá</td></tr><tr><td>PS</td><td>Islas Pitcairn</td><td>Islas Pitcairn</td></tr><tr><td>PT</td><td>Portugués</td><td>Portugal</td></tr><tr><td>PU</td><td>Peruana</td><td>Perú</td></tr><tr><td>PY</td><td>Paraguayo</td><td>Paraguay</td></tr><tr><td>RC</td><td>Marroquí</td><td>Marruecos</td></tr><tr><td>RE</td><td>Islas Reunión</td><td>Islas Reunión</td></tr><tr><td>RO</td><td>Rumana</td><td>Rumania</td></tr><tr><td>RU</td><td>Rusa</td><td>Rusia</td></tr><tr><td>RW</td><td>Ruanda</td><td>Ruanda</td></tr><tr><td>SA</td><td>Saudí Árabe</td><td>Arabia Saudita</td></tr><tr><td>SB</td><td>Sudan</td><td>Sudan</td></tr><tr><td>SE</td><td>Sueco</td><td>Suecia</td></tr><tr><td>SF</td><td>San Vencen y Las Granadas</td><td>San Vencen y Las Granadas</td></tr><tr><td>SH</td><td>Santa Helena</td><td>Santa Helena</td></tr><tr><td>SI</td><td>Islas Salmon</td><td>Islas Salmon</td></tr><tr><td>SN</td><td>Senegal</td><td>Senegal</td></tr><tr><td>SO</td><td>Somalia</td><td>Somalia</td></tr><tr><td>SP</td><td>San Pierre y Miquelón</td><td>San Pierre y Miquelón</td></tr><tr><td>SR</td><td>Surinam</td><td>Surinam</td></tr><tr><td>SS</td><td>San Kitts</td><td>San Kitts</td></tr><tr><td>ST</td><td>Islas Santa Cruz</td><td>Islas Santa Cruz</td></tr><tr><td>SU</td><td>Estonia</td><td>Estonia</td></tr><tr><td>SV</td><td>Salvadoreña</td><td>El Salvador</td></tr><tr><td>SW</td><td>Suiza</td><td>Suiza</td></tr><tr><td>SX</td><td>Serbia</td><td>Serbia</td></tr><tr><td>SY</td><td>Siria</td><td>Siria</td></tr><tr><td>SZ</td><td>Swazilandia</td><td>Swazilandia</td></tr><tr><td>TA</td><td>Tonga</td><td>Tonga</td></tr><tr><td>TC</td><td>Turcos e Islas Caicos</td><td>Turcos e Islas Caicos</td></tr><tr><td>TD</td><td>Tristán De Cunha</td><td>Tristán De Cunha</td></tr><tr><td>TG</td><td>Togo</td><td>Togo</td></tr><tr><td>TH</td><td>Tailandia</td><td>Tailandia</td></tr><tr><td>TR</td><td>Turca</td><td>Turquía </td></tr><tr><td>TT</td><td>Trinidad y Tobago</td><td>Trinidad y Tobago</td></tr><tr><td>TU</td><td>Túnez</td><td>Túnez</td></tr><tr><td>TV</td><td>Tuvala</td><td>Tuvala</td></tr><tr><td>TW</td><td>Taiwán</td><td>Taiwán</td></tr><tr><td>TZ</td><td>Tanzania</td><td>Tanzania</td></tr><tr><td>UA</td><td>Ucraniano</td><td>Ucrania</td></tr><tr><td>UG</td><td>Uganda</td><td>Uganda</td></tr><tr><td>UK</td><td>Reino Unido</td><td>Reino Unido</td></tr><tr><td>UM</td><td>Árabe</td><td>Emiratos Árabes Unidos</td></tr><tr><td>US</td><td>Estadounidense</td><td>Estados Unidos</td></tr><tr><td>UY</td><td>Uruguayo</td><td>Uruguay</td></tr><tr><td>VC</td><td>Ciudad Del Vaticano</td><td>Ciudad Del Vaticano</td></tr><tr><td>VE</td><td>Venezolana</td><td>Venezuela</td></tr><tr><td>VG</td><td>Islas Vírgenes Inglesas</td><td>Islas Vírgenes Inglesas</td></tr><tr><td>VN</td><td>Vietnami</td><td>Vietnam</td></tr><tr><td>VU</td><td>Vanuatu</td><td>Vanuatu</td></tr><tr><td>WS</td><td>Samoa Oeste</td><td>Samoa Oeste</td></tr><tr><td>WT</td><td>Gales / Isla Futura</td><td>Gales / Isla Futura</td></tr><tr><td>XN</td><td>Eslovenia</td><td>Eslovenia</td></tr><tr><td>YE</td><td>Yemen (Del Sur)</td><td>Yemen (Del Sur)</td></tr><tr><td>YS</td><td>Yemen (Del Norte)</td><td>Yemen (Del Norte)</td></tr><tr><td>ZA</td><td>Sudafricana</td><td>África Del Sur</td></tr><tr><td>ZM</td><td>Zambia</td><td>Zambia</td></tr><tr><td>ZR</td><td>Zaire</td><td>Zaire</td></tr><tr><td>ZW</td><td>Zimbabwe</td><td>Zimbabwe</td></tr></tbody></table></p  # noqa: E501

        :return: The nacionalidad of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        """Sets the nacionalidad of this PersonaPeticion.

        <p>Debe contener la clave de la nacionalidad del consumidor los valores posibles son los siguientes:</p><p><table><thead><tr><th>Clave</th><th>Nacionalidad</th><th>País</th></tr></thead><tbody><tr><td>AD</td><td>Andorra</td><td>Andorra</td></tr><tr><td>AF</td><td>Afgana</td><td>Afganistán</td></tr><tr><td>AG</td><td>Antigua y Barbado</td><td>Antigua y Barbado</td></tr><tr><td>AI</td><td>Anguila</td><td>Anguila</td></tr><tr><td>AN</td><td>Albania</td><td>Albania</td></tr><tr><td>AO</td><td>Angola</td><td>Angola</td></tr><tr><td>AS</td><td>Ascensión</td><td>Ascensión</td></tr><tr><td>AT</td><td>Argentina</td><td>Argentina</td></tr><tr><td>AU</td><td>Australiana</td><td>Australia</td></tr><tr><td>AW</td><td>Árabe</td><td>Arabia</td></tr><tr><td>AX</td><td>Azores</td><td>Azores</td></tr><tr><td>BB</td><td>Barbados</td><td>Barbados</td></tr><tr><td>BD</td><td>Bangladesh</td><td>Bangladesh</td></tr><tr><td>BE</td><td>Belga</td><td>Bélgica</td></tr><tr><td>BF</td><td>Burkina</td><td>Burkina</td></tr><tr><td>BG</td><td>Búlgara</td><td>Bulgaria</td></tr><tr><td>BH</td><td>Bahrein</td><td>Bahrein</td></tr><tr><td>BI</td><td>Burundi</td><td>Burundi</td></tr><tr><td>BJ</td><td>Benin</td><td>Benin</td></tr><tr><td>BK</td><td>Birmania</td><td>Birmania</td></tr><tr><td>BM</td><td>Bután</td><td>Bután</td></tr><tr><td>BN</td><td>Brunei</td><td>Brunei</td></tr><tr><td>BO</td><td>Boliviana</td><td>Bolivia</td></tr><tr><td>BR</td><td>Brasileño</td><td>Brasil</td></tr><tr><td>BS</td><td>Bahamas</td><td>Bahamas</td></tr><tr><td>BU</td><td>Bermudas</td><td>Bermudas</td></tr><tr><td>BW</td><td>Botswana</td><td>Botswana</td></tr><tr><td>BX</td><td>Bosnia Herzegovina</td><td>Bosnia Herzegovina</td></tr><tr><td>BZ</td><td>Belice</td><td>Belice</td></tr><tr><td>CB</td><td>Colombiana</td><td>Colombia</td></tr><tr><td>CC</td><td>Córcega</td><td>Córcega</td></tr><tr><td>CD</td><td>Chad</td><td>Chad</td></tr><tr><td>CF</td><td>Rep. Central Africana</td><td>Rep. Central Africana</td></tr><tr><td>CG</td><td>Congo</td><td>Congo</td></tr><tr><td>CH</td><td>Liechtenstein</td><td>Liechtenstein</td></tr><tr><td>CI</td><td>Islas Caimán</td><td>Islas Caimán</td></tr><tr><td>CJ</td><td>Comoros</td><td>Comoros</td></tr><tr><td>CL</td><td>Chilena</td><td>Chile</td></tr><tr><td>CM</td><td>Camerunés</td><td>Camerún</td></tr><tr><td>CN</td><td>Canadiense</td><td>Canadá</td></tr><tr><td>CP</td><td>China</td><td>China (Pekín)</td></tr><tr><td>CS</td><td>República Checa Eslovaca</td><td>República Checa Eslovaca</td></tr><tr><td>CU</td><td>Cariacou</td><td>Cariacou</td></tr><tr><td>CV</td><td>Cabo Verde</td><td>Cabo Verde</td></tr><tr><td>CY</td><td>Chipre</td><td>Chipre</td></tr><tr><td>DF</td><td>Austriaca</td><td>Austria</td></tr><tr><td>DJ</td><td>Djibouti</td><td>Djibouti</td></tr><tr><td>DK</td><td>Danés</td><td>Dinamarca</td></tr><tr><td>DM</td><td>Dominicana</td><td>Dominicana</td></tr><tr><td>DO</td><td>Dominicana</td><td>República Dominicana</td></tr><tr><td>DW</td><td>Alemana</td><td>Alemania</td></tr><tr><td>DZ</td><td>Argelia</td><td>Argelia</td></tr><tr><td>EC</td><td>Ecuatoriana</td><td>Ecuador</td></tr><tr><td>EG</td><td>Egipcia</td><td>Egipto</td></tr><tr><td>EM</td><td>Timor Oriental</td><td>Timor Oriental</td></tr><tr><td>ES</td><td>Española</td><td>España</td></tr><tr><td>ET</td><td>Etiopia</td><td>Etiopia</td></tr><tr><td>FA</td><td>Islas Falkland (Malvinas)</td><td>Islas Falkland (Malvinas)</td></tr><tr><td>FE</td><td>Islas Faroe</td><td>Islas Faroe</td></tr><tr><td>FI</td><td>Finlandia</td><td>Finlandia</td></tr><tr><td>FJ</td><td>Fiji</td><td>Fiji</td></tr><tr><td>FP</td><td>Polinesia</td><td>Polinesia</td></tr><tr><td>FR</td><td>Francesa</td><td>Francia</td></tr><tr><td>GB</td><td>Gabón</td><td>Gabón</td></tr><tr><td>GD</td><td>Granada</td><td>Granada</td></tr><tr><td>GE</td><td>Groenlandia</td><td>Groenlandia</td></tr><tr><td>GF</td><td>Guayana Francesa</td><td>Guayana Francesa</td></tr><tr><td>GH</td><td>Ghana</td><td>Ghana</td></tr><tr><td>GI</td><td>Gibraltar</td><td>Gibraltar</td></tr><tr><td>GM</td><td>Gambia</td><td>Gambia</td></tr><tr><td>GN</td><td>Guinea</td><td>Guinea</td></tr><tr><td>GP</td><td>Guadalupe</td><td>Guadalupe</td></tr><tr><td>GQ</td><td>Guinea Ecuatorial</td><td>Guinea Ecuatorial</td></tr><tr><td>GR</td><td>Griega</td><td>Grecia</td></tr><tr><td>GT</td><td>Guatemalteca</td><td>Guatemala</td></tr><tr><td>GW</td><td>Guinea Bissau</td><td>Guinea Bissau</td></tr><tr><td>GX</td><td>República De Georgia</td><td>República De Georgia</td></tr><tr><td>GY</td><td>Guyana</td><td>Guyana</td></tr><tr><td>HA</td><td>Haitiana</td><td>Haití</td></tr><tr><td>HK</td><td>Hong Kong</td><td>Hong Kong</td></tr><tr><td>HN</td><td>Hondureña</td><td>Honduras</td></tr><tr><td>HR</td><td>Cubano</td><td>Cuba</td></tr><tr><td>HU</td><td>Húngara</td><td>Húngara</td></tr><tr><td>HX</td><td>Croata</td><td>Croacia</td></tr><tr><td>IB</td><td>India</td><td>India</td></tr><tr><td>IC</td><td>Costa De Marfil</td><td>Costa De Marfil</td></tr><tr><td>IE</td><td>Irlandesa</td><td>Irlandesa</td></tr><tr><td>IF</td><td>Indonesia</td><td>Indonesia</td></tr><tr><td>IG</td><td>Israelí</td><td>Israelí</td></tr><tr><td>IQ</td><td>Iraquí</td><td>Iraquí</td></tr><tr><td>IR</td><td>Iraní</td><td>Iraní</td></tr><tr><td>IS</td><td>Islandia</td><td>Islandia</td></tr><tr><td>IT</td><td>Italiano</td><td>Italiano</td></tr><tr><td>JM</td><td>Jamaicano</td><td>Jamaicano</td></tr><tr><td>JO</td><td>Jordano</td><td>Jordano</td></tr><tr><td>JP</td><td>Japonesa</td><td>Japonesa</td></tr><tr><td>KA</td><td>Kampuchea</td><td>Kampuchea</td></tr><tr><td>KE</td><td>Kenya</td><td>Kenya</td></tr><tr><td>KI</td><td>Kiribati</td><td>Kiribati</td></tr><tr><td>KN</td><td>San Cristóbal De Neváis</td><td>San Cristóbal De Neváis</td></tr><tr><td>KR</td><td>Corea Del Sur</td><td>Corea Del Sur</td></tr><tr><td>KW</td><td>Kuwait</td><td>Kuwait</td></tr><tr><td>KX</td><td>Corea Del Norte</td><td>Corea Del Norte</td></tr><tr><td>LB</td><td>Libanes</td><td>Libanes</td></tr><tr><td>LC</td><td>Santa Lucia</td><td>Santa Lucia</td></tr><tr><td>LE</td><td>Islas De Sotavento</td><td>Islas De Sotavento</td></tr><tr><td>LK</td><td>Sri Lanka</td><td>Sri Lanka</td></tr><tr><td>LO</td><td>Laos</td><td>Laos</td></tr><tr><td>LR</td><td>Liberia</td><td>Liberia</td></tr><tr><td>LS</td><td>Lesotho</td><td>Lesotho</td></tr><tr><td>LT</td><td>Lituania</td><td>Lituania</td></tr><tr><td>LU</td><td>Luxemburgo</td><td>Luxemburgo</td></tr><tr><td>LV</td><td>Libia</td><td>Libia</td></tr><tr><td>LX</td><td>Letonia</td><td>Letonia</td></tr><tr><td>MC</td><td>Mongolia</td><td>Mongolia</td></tr><tr><td>MD</td><td>Madeira</td><td>Madeira</td></tr><tr><td>MG</td><td>Madagascar</td><td>Madagascar</td></tr><tr><td>MH</td><td>Macedonia</td><td>Macedonia</td></tr><tr><td>MJ</td><td>Macao</td><td>Macao</td></tr><tr><td>MK</td><td>Montserrat</td><td>Montserrat</td></tr><tr><td>ML</td><td>Mali</td><td>Mali</td></tr><tr><td>MM</td><td>Montenegro</td><td>Montenegro</td></tr><tr><td>MP</td><td>Sao Tome y Principado</td><td>Sao Tome y Principado</td></tr><tr><td>MQ</td><td>Martinico</td><td>Martinico</td></tr><tr><td>MR</td><td>Mauritania</td><td>Mauritania</td></tr><tr><td>MT</td><td>Malta</td><td>Malta</td></tr><tr><td>MU</td><td>Mauricio</td><td>Mauricio</td></tr><tr><td>MV</td><td>Maldivas</td><td>Maldivas</td></tr><tr><td>MW</td><td>Malawi</td><td>Malawi</td></tr><tr><td>MX</td><td>Mexicana</td><td>México</td></tr><tr><td>MY</td><td>Malasia</td><td>Malasia</td></tr><tr><td>MZ</td><td>Mozambique</td><td>Mozambique</td></tr><tr><td>NA</td><td>Nauru</td><td>Nauru</td></tr><tr><td>ND</td><td>No Definido</td><td>No Definido</td></tr><tr><td>NI</td><td>Nicaragua</td><td>Nicaragua</td></tr><tr><td>NL</td><td>Holandesa</td><td>Holanda</td></tr><tr><td>NN</td><td>Antillas Holandesas</td><td>Antillas Holandesas</td></tr><tr><td>NO</td><td>Noruega</td><td>Noruega</td></tr><tr><td>NP</td><td>Nepal</td><td>Nepal</td></tr><tr><td>NR</td><td>Nigeriano</td><td>Nigeria</td></tr><tr><td>NW</td><td>Nueva Caledonia</td><td>Nueva Caledonia</td></tr><tr><td>NZ</td><td>Nueva Zelandia</td><td>Nueva Zelandia</td></tr><tr><td>OA</td><td>Katar</td><td>Katar</td></tr><tr><td>OM</td><td>Omán</td><td>Omán</td></tr><tr><td>PG</td><td>Papúa Nueva Guinea</td><td>Papúa Nueva Guinea</td></tr><tr><td>PH</td><td>Filipinas</td><td>Filipinas</td></tr><tr><td>PK</td><td>Pakistán</td><td>Pakistán</td></tr><tr><td>PL</td><td>Polaco</td><td>Polonia</td></tr><tr><td>PM</td><td>Panameño</td><td>Panamá</td></tr><tr><td>PS</td><td>Islas Pitcairn</td><td>Islas Pitcairn</td></tr><tr><td>PT</td><td>Portugués</td><td>Portugal</td></tr><tr><td>PU</td><td>Peruana</td><td>Perú</td></tr><tr><td>PY</td><td>Paraguayo</td><td>Paraguay</td></tr><tr><td>RC</td><td>Marroquí</td><td>Marruecos</td></tr><tr><td>RE</td><td>Islas Reunión</td><td>Islas Reunión</td></tr><tr><td>RO</td><td>Rumana</td><td>Rumania</td></tr><tr><td>RU</td><td>Rusa</td><td>Rusia</td></tr><tr><td>RW</td><td>Ruanda</td><td>Ruanda</td></tr><tr><td>SA</td><td>Saudí Árabe</td><td>Arabia Saudita</td></tr><tr><td>SB</td><td>Sudan</td><td>Sudan</td></tr><tr><td>SE</td><td>Sueco</td><td>Suecia</td></tr><tr><td>SF</td><td>San Vencen y Las Granadas</td><td>San Vencen y Las Granadas</td></tr><tr><td>SH</td><td>Santa Helena</td><td>Santa Helena</td></tr><tr><td>SI</td><td>Islas Salmon</td><td>Islas Salmon</td></tr><tr><td>SN</td><td>Senegal</td><td>Senegal</td></tr><tr><td>SO</td><td>Somalia</td><td>Somalia</td></tr><tr><td>SP</td><td>San Pierre y Miquelón</td><td>San Pierre y Miquelón</td></tr><tr><td>SR</td><td>Surinam</td><td>Surinam</td></tr><tr><td>SS</td><td>San Kitts</td><td>San Kitts</td></tr><tr><td>ST</td><td>Islas Santa Cruz</td><td>Islas Santa Cruz</td></tr><tr><td>SU</td><td>Estonia</td><td>Estonia</td></tr><tr><td>SV</td><td>Salvadoreña</td><td>El Salvador</td></tr><tr><td>SW</td><td>Suiza</td><td>Suiza</td></tr><tr><td>SX</td><td>Serbia</td><td>Serbia</td></tr><tr><td>SY</td><td>Siria</td><td>Siria</td></tr><tr><td>SZ</td><td>Swazilandia</td><td>Swazilandia</td></tr><tr><td>TA</td><td>Tonga</td><td>Tonga</td></tr><tr><td>TC</td><td>Turcos e Islas Caicos</td><td>Turcos e Islas Caicos</td></tr><tr><td>TD</td><td>Tristán De Cunha</td><td>Tristán De Cunha</td></tr><tr><td>TG</td><td>Togo</td><td>Togo</td></tr><tr><td>TH</td><td>Tailandia</td><td>Tailandia</td></tr><tr><td>TR</td><td>Turca</td><td>Turquía </td></tr><tr><td>TT</td><td>Trinidad y Tobago</td><td>Trinidad y Tobago</td></tr><tr><td>TU</td><td>Túnez</td><td>Túnez</td></tr><tr><td>TV</td><td>Tuvala</td><td>Tuvala</td></tr><tr><td>TW</td><td>Taiwán</td><td>Taiwán</td></tr><tr><td>TZ</td><td>Tanzania</td><td>Tanzania</td></tr><tr><td>UA</td><td>Ucraniano</td><td>Ucrania</td></tr><tr><td>UG</td><td>Uganda</td><td>Uganda</td></tr><tr><td>UK</td><td>Reino Unido</td><td>Reino Unido</td></tr><tr><td>UM</td><td>Árabe</td><td>Emiratos Árabes Unidos</td></tr><tr><td>US</td><td>Estadounidense</td><td>Estados Unidos</td></tr><tr><td>UY</td><td>Uruguayo</td><td>Uruguay</td></tr><tr><td>VC</td><td>Ciudad Del Vaticano</td><td>Ciudad Del Vaticano</td></tr><tr><td>VE</td><td>Venezolana</td><td>Venezuela</td></tr><tr><td>VG</td><td>Islas Vírgenes Inglesas</td><td>Islas Vírgenes Inglesas</td></tr><tr><td>VN</td><td>Vietnami</td><td>Vietnam</td></tr><tr><td>VU</td><td>Vanuatu</td><td>Vanuatu</td></tr><tr><td>WS</td><td>Samoa Oeste</td><td>Samoa Oeste</td></tr><tr><td>WT</td><td>Gales / Isla Futura</td><td>Gales / Isla Futura</td></tr><tr><td>XN</td><td>Eslovenia</td><td>Eslovenia</td></tr><tr><td>YE</td><td>Yemen (Del Sur)</td><td>Yemen (Del Sur)</td></tr><tr><td>YS</td><td>Yemen (Del Norte)</td><td>Yemen (Del Norte)</td></tr><tr><td>ZA</td><td>Sudafricana</td><td>África Del Sur</td></tr><tr><td>ZM</td><td>Zambia</td><td>Zambia</td></tr><tr><td>ZR</td><td>Zaire</td><td>Zaire</td></tr><tr><td>ZW</td><td>Zimbabwe</td><td>Zimbabwe</td></tr></tbody></table></p  # noqa: E501

        :param nacionalidad: The nacionalidad of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and nacionalidad is None:
            raise ValueError("Invalid value for `nacionalidad`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                nacionalidad is not None and len(nacionalidad) > 2):
            raise ValueError("Invalid value for `nacionalidad`, length must be less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                nacionalidad is not None and len(nacionalidad) < 2):
            raise ValueError("Invalid value for `nacionalidad`, length must be greater than or equal to `2`")  # noqa: E501

        self._nacionalidad = nacionalidad

    @property
    def residencia(self):
        """Gets the residencia of this PersonaPeticion.  # noqa: E501


        :return: The residencia of this PersonaPeticion.  # noqa: E501
        :rtype: CatalogoResidencia
        """
        return self._residencia

    @residencia.setter
    def residencia(self, residencia):
        """Sets the residencia of this PersonaPeticion.


        :param residencia: The residencia of this PersonaPeticion.  # noqa: E501
        :type: CatalogoResidencia
        """

        self._residencia = residencia

    @property
    def estado_civil(self):
        """Gets the estado_civil of this PersonaPeticion.  # noqa: E501


        :return: The estado_civil of this PersonaPeticion.  # noqa: E501
        :rtype: CatalogoEstadoCivil
        """
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        """Sets the estado_civil of this PersonaPeticion.


        :param estado_civil: The estado_civil of this PersonaPeticion.  # noqa: E501
        :type: CatalogoEstadoCivil
        """

        self._estado_civil = estado_civil

    @property
    def sexo(self):
        """Gets the sexo of this PersonaPeticion.  # noqa: E501


        :return: The sexo of this PersonaPeticion.  # noqa: E501
        :rtype: CatalogoSexo
        """
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """Sets the sexo of this PersonaPeticion.


        :param sexo: The sexo of this PersonaPeticion.  # noqa: E501
        :type: CatalogoSexo
        """

        self._sexo = sexo

    @property
    def clave_elector_ife(self):
        """Gets the clave_elector_ife of this PersonaPeticion.  # noqa: E501

        La clave de elector que se encuentra en el IFE/INE.  # noqa: E501

        :return: The clave_elector_ife of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._clave_elector_ife

    @clave_elector_ife.setter
    def clave_elector_ife(self, clave_elector_ife):
        """Sets the clave_elector_ife of this PersonaPeticion.

        La clave de elector que se encuentra en el IFE/INE.  # noqa: E501

        :param clave_elector_ife: The clave_elector_ife of this PersonaPeticion.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                clave_elector_ife is not None and len(clave_elector_ife) > 20):
            raise ValueError("Invalid value for `clave_elector_ife`, length must be less than or equal to `20`")  # noqa: E501

        self._clave_elector_ife = clave_elector_ife

    @property
    def numero_dependientes(self):
        """Gets the numero_dependientes of this PersonaPeticion.  # noqa: E501

        Número de personas que dependen de la persona.  # noqa: E501

        :return: The numero_dependientes of this PersonaPeticion.  # noqa: E501
        :rtype: int
        """
        return self._numero_dependientes

    @numero_dependientes.setter
    def numero_dependientes(self, numero_dependientes):
        """Sets the numero_dependientes of this PersonaPeticion.

        Número de personas que dependen de la persona.  # noqa: E501

        :param numero_dependientes: The numero_dependientes of this PersonaPeticion.  # noqa: E501
        :type: int
        """

        self._numero_dependientes = numero_dependientes

    @property
    def fecha_defuncion(self):
        """Gets the fecha_defuncion of this PersonaPeticion.  # noqa: E501

        Fecha de nacimiento de la persona, en el formato especificado (por defecto yyyy-MM-dd)  # noqa: E501

        :return: The fecha_defuncion of this PersonaPeticion.  # noqa: E501
        :rtype: str
        """
        return self._fecha_defuncion

    @fecha_defuncion.setter
    def fecha_defuncion(self, fecha_defuncion):
        """Sets the fecha_defuncion of this PersonaPeticion.

        Fecha de nacimiento de la persona, en el formato especificado (por defecto yyyy-MM-dd)  # noqa: E501

        :param fecha_defuncion: The fecha_defuncion of this PersonaPeticion.  # noqa: E501
        :type: str
        """

        self._fecha_defuncion = fecha_defuncion

    @property
    def domicilio(self):
        """Gets the domicilio of this PersonaPeticion.  # noqa: E501


        :return: The domicilio of this PersonaPeticion.  # noqa: E501
        :rtype: DomicilioPeticion
        """
        return self._domicilio

    @domicilio.setter
    def domicilio(self, domicilio):
        """Sets the domicilio of this PersonaPeticion.


        :param domicilio: The domicilio of this PersonaPeticion.  # noqa: E501
        :type: DomicilioPeticion
        """
        if self._configuration.client_side_validation and domicilio is None:
            raise ValueError("Invalid value for `domicilio`, must not be `None`")  # noqa: E501

        self._domicilio = domicilio

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PersonaPeticion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PersonaPeticion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonaPeticion):
            return True

        return self.to_dict() != other.to_dict()
