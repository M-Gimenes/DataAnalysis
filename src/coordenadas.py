from geopy.geocoders import Nominatim

# Inicializar o geocodificador do Nominatim
geolocator = Nominatim(user_agent="my_geocoder")

# Função para obter as coordenadas a partir de um CEP
def get_coordinates_from_cep(cep):
    # Construir a consulta de endereço com o CEP
    address_query = f"{cep}, Brasil"
    
    # Tentar obter as coordenadas do endereço
    try:
        location = geolocator.geocode(address_query)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Erro ao obter coordenadas para o CEP {cep}: {e}")
    
    return None, None