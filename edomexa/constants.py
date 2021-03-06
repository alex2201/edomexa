def create_navbar_options(current_path: str):
    NAVBAR_OPTIONS = (
        ['NOSOTRXS', '/nosotros', False],
        ['LUGARES EXTRAORDINARIOS', '/section/lugares-extraordinarios', False],
        ['ORGULLO EDOMEXA', '/section/orgullo-edomexa', False],
        ['EVENTOS', '/section/eventos', False],
        ['POSTULAR', '/postular', False],
    )

    for option in NAVBAR_OPTIONS:
        if option[1] == current_path:
            option[2] = True
            break

    return NAVBAR_OPTIONS


EMAIL_LIST = ('edomexa23@gmail.com', 'alejandrocastillo0088@gmail.com')


HOMEPAGE_SECTIONS = {
    'lugares-extraordinarios': (
        1,
        'LUGARES<br>EXTRAORDINARIOS',
        'El Estado de México es una de las entidades de la república que ofrece una gran cantidad de atractivos turísticos. Es rico en bellezas naturales, sitios arqueológicos y lugares históricos. Cuenta con ocho corredores turísticos que te harán maravillarte con la grandeza de su territorio.',
        'edomexa/resources/ico_lugares.png',
        'lugares-extraordinarios',
    ),
    'orgullo-edomexa': (
        3,
        'ORGULLO<br>EDOMEXA',
        'Si vives en el Estado de México o quieres recorrer los lugares turisticos de esta entidad. no te puedes perder de la increlble gastronomía, así como el talento local o las grandiosas artesanias que te ofrece cada lugar al que vayas.',
        'edomexa/resources/ico_orgullo.png',
        'orgullo-edomexa',
    ),
    'eventos': (
        4,
        'EVENTOS<br>-',
        'Encuentra los meiores eventos en Estado de México esta semana y descubre todas las actividades en tu zona Consulta nuestras recomendaciones de eventos y actividades de ocio, y no te quedes sin plan este fin de semana en Estado de México.',
        'edomexa/resources/ico_eventos.png',
        'eventos',
    ),
}

TIPO_LUGAR = (
    ('NEGOCIO', 'Negocio'),
    ('TURISMO', 'Turístico'),
    ('MUSEO/RECREATIVO', 'Museo/Recreativo'),
    ('EVENTO', 'Evento'),
)

MUNICIPIOS = (
    ('001', 'Acambay de Ruíz Castañeda'),
    ('002', 'Acolman'),
    ('003', 'Aculco'),
    ('004', 'Almoloya de Alquisiras'),
    ('005', 'Almoloya de Juárez'),
    ('006', 'Almoloya del Río'),
    ('007', 'Amanalco'),
    ('008', 'Amatepec'),
    ('009', 'Amecameca'),
    ('010', 'Apaxco'),
    ('011', 'Atenco'),
    ('012', 'Atizapán'),
    ('013', 'Atizapán de Zaragoza'),
    ('014', 'Atlacomulco'),
    ('015', 'Atlautla'),
    ('016', 'Axapusco'),
    ('017', 'Ayapango'),
    ('018', 'Calimaya'),
    ('019', 'Capulhuac'),
    ('020', 'Coacalco de Berriozábal'),
    ('021', 'Coatepec Harinas'),
    ('022', 'Cocotitlán'),
    ('023', 'Coyotepec'),
    ('024', 'Cuautitlán'),
    ('025', 'Chalco'),
    ('026', 'Chapa de Mota'),
    ('027', 'Chapultepec'),
    ('028', 'Chiautla'),
    ('029', 'Chicoloapan'),
    ('030', 'Chiconcuac'),
    ('031', 'Chimalhuacán'),
    ('032', 'Donato Guerra'),
    ('033', 'Ecatepec de Morelos'),
    ('034', 'Ecatzingo'),
    ('035', 'Huehuetoca'),
    ('036', 'Hueypoxtla'),
    ('037', 'Huixquilucan'),
    ('038', 'Isidro Fabela'),
    ('039', 'Ixtapaluca'),
    ('040', 'Ixtapan de la Sal'),
    ('041', 'Ixtapan del Oro'),
    ('042', 'Ixtlahuaca'),
    ('043', 'Xalatlaco'),
    ('044', 'Jaltenco'),
    ('045', 'Jilotepec'),
    ('046', 'Jilotzingo'),
    ('047', 'Jiquipilco'),
    ('048', 'Jocotitlán'),
    ('049', 'Joquicingo'),
    ('050', 'Juchitepec'),
    ('051', 'Lerma'),
    ('052', 'Malinalco'),
    ('053', 'Melchor Ocampo'),
    ('054', 'Metepec'),
    ('055', 'Mexicaltzingo'),
    ('056', 'Morelos'),
    ('057', 'Naucalpan de Juárez'),
    ('058', 'Nezahualcóyotl'),
    ('059', 'Nextlalpan'),
    ('060', 'Nicolás Romero'),
    ('061', 'Nopaltepec'),
    ('062', 'Ocoyoacac'),
    ('063', 'Ocuilan'),
    ('064', 'El Oro'),
    ('065', 'Otumba'),
    ('066', 'Otzoloapan'),
    ('067', 'Otzolotepec'),
    ('068', 'Ozumba'),
    ('069', 'Papalotla'),
    ('070', 'La Paz'),
    ('071', 'Polotitlán'),
    ('072', 'Rayón'),
    ('073', 'San Antonio la Isla'),
    ('074', 'San Felipe del Progreso'),
    ('075', 'San Martín de las Pirámides'),
    ('076', 'San Mateo Atenco'),
    ('077', 'San Simón de Guerrero'),
    ('078', 'Santo Tomás'),
    ('079', 'Soyaniquilpan de Juárez'),
    ('080', 'Sultepec'),
    ('081', 'Tecámac'),
    ('082', 'Tejupilco'),
    ('083', 'Temamatla'),
    ('084', 'Temascalapa'),
    ('085', 'Temascalcingo'),
    ('086', 'Temascaltepec'),
    ('087', 'Temoaya'),
    ('088', 'Tenancingo'),
    ('089', 'Tenango del Aire'),
    ('090', 'Tenango del Valle'),
    ('091', 'Teoloyucan'),
    ('092', 'Teotihuacán'),
    ('093', 'Tepetlaoxtoc'),
    ('094', 'Tepetlixpa'),
    ('095', 'Tepotzotlán'),
    ('096', 'Tequixquiac'),
    ('097', 'Texcaltitlán'),
    ('098', 'Texcalyacac'),
    ('099', 'Texcoco'),
    ('100', 'Tezoyuca'),
    ('101', 'Tianguistenco'),
    ('102', 'Timilpan'),
    ('103', 'Tlalmanalco'),
    ('104', 'Tlalnepantla de Baz'),
    ('105', 'Tlatlaya'),
    ('106', 'Toluca'),
    ('107', 'Tonatico'),
    ('108', 'Tultepec'),
    ('109', 'Tultitlán'),
    ('110', 'Valle de Bravo'),
    ('111', 'Villa de Allende'),
    ('112', 'Villa del Carbón'),
    ('113', 'Villa Guerrero'),
    ('114', 'Villa Victoria'),
    ('115', 'Xonacatlán'),
    ('116', 'Zacazonapan'),
    ('117', 'Zacualpan'),
    ('118', 'Zinacantepec'),
    ('119', 'Zumpahuacán'),
    ('120', 'Zumpango'),
    ('121', 'Cuautitlán Izcalli'),
    ('122', 'Valle de Chalco Solidaridad'),
    ('123', 'Luvianos'),
    ('124', 'San José del Rincón'),
    ('125', 'Tonanitla'),
)
