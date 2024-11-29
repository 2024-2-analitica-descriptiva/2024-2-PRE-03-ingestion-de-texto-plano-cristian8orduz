"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd
    data = open("files/input/clusters_report.txt", "r").readlines()
    data = [z.replace('\n', '')for z in data]
    data = [line.strip() for line in data if isinstance(line, str) and line.strip()]
    

    header = data[0:2]
    header = ' '.join(header).split()
    cleaned_data = ' '.join(header).split()

    # Now, group the words into the desired format
    result = [
        cleaned_data[0],  # 'Cluster'
        ' '.join(cleaned_data[1:3]+cleaned_data[6:8]),  # 'Cantidad de palabras clave'
        ' '.join(cleaned_data[3:5]+ cleaned_data[6:8]),  # 'Porcentaje de palabras clave'
        ' '.join(cleaned_data[5:8])    # 'Principales palabras clave'
    ]
    result = [z.lower().replace(' ', '_') for z in result]

    data_lines = data[2:]
    data_lines.pop(0)
    

    data_lines =  [z.split() for z in data_lines]
    data_lines = [item for sublist in data_lines for item in sublist]
    data_lines = [int(z) if z.isdigit() else z for z in data_lines]


    inner_data = []
    text = []
    final_data = []
    previous_number = None  # Variable para verificar si el número ya fue agregado
    for item in range(len(data_lines)):
        type_data = type(data_lines[item])

        # Check if it's the first element
        if item == 0:
            inner_data.append(data_lines[item])
            continue

        # Check if both the current and previous item are integers
        elif isinstance(data_lines[item], int) and isinstance(data_lines[item - 1], int):
            inner_data.append(data_lines[item])

        # Check if both previous and current items are integers and the next item is a string
        elif isinstance(data_lines[item - 1], int) and isinstance(data_lines[item], int):
            if item + 1 < len(data_lines) and isinstance(data_lines[item + 1], str):
                inner_data.append(data_lines[item])

        # If the current item is a string and the next item is a "%"
        elif isinstance(data_lines[item], str) and item + 1 < len(data_lines) and data_lines[item + 1] == "%":
            inner_data.append(float(data_lines[item].replace(',', '.')))

        # Skip "%" symbols
        elif data_lines[item] == "%":
            continue

        # Check if both previous and current items are strings and the next item is a string
        elif isinstance(data_lines[item], str) and isinstance(data_lines[item - 1], str) and item + 1 < len(data_lines) and isinstance(data_lines[item + 1], str):
            text.append(data_lines[item])
        elif isinstance(data_lines[item], str) and isinstance(data_lines[item - 1], str) and item + 1 < len(data_lines) and isinstance(data_lines[item + 1], int):
          text.append(data_lines[item])


        # If an integer is surrounded by a string on both sides, create a phrase
        elif isinstance(data_lines[item], int) and isinstance(data_lines[item - 1], str) and item + 1 < len(data_lines) and isinstance(data_lines[item + 1], int):
            # Combine the text and store the result
            frase = " ".join(text)
            inner_data.append(frase)  
            final_data.append(inner_data)
            inner_data = []
            text = []
            inner_data.append(data_lines[item])

        # Handle the last element
        elif item == len(data_lines) - 1:
            text.append(data_lines[item])
            frase = " ".join(text)
            inner_data.append(frase)  
            final_data.append(inner_data)
    
    
    df = pd.DataFrame(final_data, columns=result)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: x[:-1] if x.endswith('.') else x)

    return df
    


  


    

if __name__ == '__main__': 
    print(pregunta_01())