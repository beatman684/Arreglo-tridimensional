#Calcular Temperaturas promedio
temperaturas = [
    [   # Loja
        [   # Semana
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 11},
            {"dia": "Viernes", "temp": 13},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 19}
        ]
    ],
    [   # Cuenca
        [   # Semana
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 14},
            {"dia": "Viernes", "temp": 11},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 21}
        ]
    ],
    [   # Machala
        [   # Semana
            {"dia": "Lunes", "temp": 19},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 16}
        ]
    ]
]


for ciudad_index, ciudad in enumerate(temperaturas, start=1):
    for semana_index, semana in enumerate(ciudad, start=1):
        suma_temp = sum(dia['temp'] for dia in semana)
        media = suma_temp / 7 #se divide por los dias de la semana
        media = round(media, 2)
    print('La temperatura promedio de la semana es de ' + str(media))