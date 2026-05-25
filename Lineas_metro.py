#Programa creado por Mex Lozano Rafael Emilio
#Esta programa contiene las líneas y sus estaciones del metro de la CDMX

#Se crea cada línea del metro como una variable para que puedan ser usadas por el verificador 

linea_1 = [
    "Pantitlán L1","Zaragoza","Gómez Farías","Boulevard Puerto Aéreo", "Balbuena", "Moctezuma", "San Lázaro L1", "Candelaria L1","Merced","Pino Suárez L1", "Isabel La Católica","Salto del Agua L1", "Balderas L1", "Cuauhtémoc", "Insurgentes", "Sevilla", "Chapultepec", "Juanacatlán", "Tacubaya L1", "Observatorio" 
    ]

linea_2 = [
    'Cuatro Caminos', 'Panteones', 'Tacuba L2', 'Cuitláhuac', 'Popotla', 'Colegio Militar', 'Normal',  'San Cosme', 'Revolución', 'Hidalgo L2', 'Bellas Artes L2', 'Allende', 'Zócalo/Tenochtitlán', 'Pino Suárez L2', 'San Antonio Abad', 'Chabacano L2','Viaducto', 'Xola', 'Villa de Cortés', 'Nativitas', 'Portales', 'Ermita L2', 'General Anaya', 'Tasqueña'
]

linea_3 = [
    'Indios Verdes', 'Deportivo 18 de marzo L3', 'Potrero', 'La Raza L3', 'Tlatelolco', 'Guerrero', 'Hidalgo L3', 'Juárez', 'Balderas L3', 'Niños Héroes/Poder Judicial CDMX', 'Hospital General', 'Centro Médico L3', 'Etiopía/Plaza de la Transparencia', 'Eugenia', 'División del Norte', 'Zapata L3', 'Coyoacán', 'Viveros/Derechos Humanos', 'M. A. de Quevedo', 'Copilco', 'Universidad'   
]

linea_4 = [
    'Martín Carrera L4', 'Talismán', 'Bondojito', 'Consulado L4', 'Canal del Norte', 'Morelos L4', 'Candelaria L4', 'Fray Servando', 'Jamaica L4', 'Santa Anita L4'
]

linea_5 = [
    'Pantitlán L5', 'Hangares', 'Terminal Aérea', 'Oceanía L5', 'Aragón', 'Eduardo Molina', 'Consulado L5', 'Valle Gómez', 'Misterios', 'La Raza L5', 'Autobuses del Norte', 'Instituto del Petróleo L5', 'Politécnico'
]

linea_6 = [
    'El Rosario L6','Tezozómoc', 'Azcapotzalco', 'Ferrería', 'Norte 45', 'Vallejo', 'Instituto del Petróleo L6', 'Lindavista', 'Deportivo 18 de marzo L6', 'La Villa-Basílica', 'Martín Carrera L6'
]

linea_7 =[
    'El Rosario L7', 'Aquiles Serdán', 'Camarones', 'Refinería', 'Tacuba L7', 'San Joaquín', 'Polanco', 'Auditorio', 'Constituyentes', 'Tacubaya L7', 'San Pedro de los Pinos', 'San Antonio', 'Mixcoac L7', 'Barranca del Muerto'
]

linea_8 = [
    'Garibaldi / Lagunilla L8', 'Bellas Artes L8', 'San Juan de Letrán', 'Salto del Agua L8', 'Doctores', 'Obrera', 'Chabacano L8', 'La Viga', 'Santa Anita L8', 'Coyuya' , 'Iztacalco', 'Apatlaco', 'Aculco', 'Escuadrón 201' 'Atlalilco L8', 'Iztapalapa', 'Cerro de la Estrella', 'UAM-I', 'Constitución de 1917'
]

linea_9 = [
    'Tacubaya L9', 'Patriotismo', 'Chilpancingo', 'Centro Médico L9', 'Lázaro Cárdenas', 'Chabacano L9', 'Jamaica L9', 'Mixiuhca', 'Velódromo', 'Ciudad Deportiva', 'Puebla', 'Pantitlán L9'
]

linea_A = [
    'Pantitlán LA', 'Agrícola Oriental', 'Canal de San Juan', 'Tepalcates', 'Guelatao', 'Peñón Viejo', 'Acatitla', 'Santa Marta', 'Los Reyes', 'La Paz'
]

linea_B = [
    'Ciudad Azteca', 'Plaza Aragón', 'Olímpica', 'Ecatepec', 'Múzquiz', 'Río de los Remedios', 'Impulsora', 'Nezahualcóyotl', 'Villa de Aragón', 'Bosque de Aragón', 'Deportivo Oceanía', 'Oceanía LB', 'Romero Rubio', 'R. Flores Magón', 'San Lázaro LB', 'Morelos LB', 'Tepito', 'Lagunilla', 'Garibaldi/Lagunilla LB', 'Guerrero', 'Buenavista'
]

linea_12 = [
    'Mixcoac L12', 'Insurgentes Sur', 'Hospital 20 de noviembre', 'Zapata', 'Parque de los Venados', 'Eje Central', 'Ermita L12', 'Mexicaltzingo', 'Atlalilco L12', 'Culhuacán', 'San Andrés Tomatlán', 'Lomas Estrella', 'Calle 11', 'Periférico Oriente', 'Tezonco', 'Olivos', 'Nopalera', 'Zapotitlán' 'Tlaltenco', 'Tláhuac'
]

#Se crea una función llamada "verificador_estaciones" con dos argumentos, uno que será la ruta que cree el usuario y el segundo la lista de todas las líneas y estaciones que puse.
def verificador_estaciones(ruta_creada, lista_estaciones):
    return ruta_creada in lista_estaciones
    

