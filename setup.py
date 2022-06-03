# coding: utf-8



from setuptools import setup, find_packages  # noqa: H301

NAME = "rcc-fico-pld-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23",
    "pyOpenSSL>=22.0.0",
    "cryptography>=37.0.2",
    "configparser>=5.2.0"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Reporte de Crédito Consolidado, FICO® Score y PLD ",
    author_email="api@circulodecredito.com.mx",
    url="",
    keywords=["Swagger", "Reporte de Crédito Consolidado, FICO® Score y PLD "],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;p&gt;Esta API reporta: el historial crediticio; el cumplimiento de pago de los compromisos que la persona ha adquirido con entidades financieras, no financieras e instituciones comerciales que dan crédito o participan en actividades afines al crédito; y filtra contra listas de cumplimiento para Prevención de Lavado de Dinero. En esta versión se retornan los campos del Crédito Asociado a Nomina (CAN) en el nodo de créditos.&lt;br/&gt;&lt;img src&#x3D;&#39;https://developer.circulodecredito.com.mx/sites/default/files/2020-10/circulo_de_credito-apihub.png&#39; height&#x3D;&#39;40&#39; width&#x3D;&#39;220&#39;/&gt;&lt;/p&gt;&lt;br/&gt;  # noqa: E501
    """
)
