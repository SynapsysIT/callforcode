import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon


class MapGenerator:
    def generate_map(self):

        # Coordonnées GPS (exemple: Paris)
        latitude = 51.5074  # Londres
        longitude = -0.1278


        # Rayon autour des coordonnées GPS (en degrés, 1 km approx.)
        radius = 0.5

        # Créer la requête Overpass pour récupérer des points d'eau (lacs, rivières, étangs)
        overpass_url = "http://overpass-api.de/api/interpreter"
        overpass_query = f"""
                            [out:json];
                            (
                            node["highway"](around:{radius},{latitude},{longitude});
                            way["highway"](around:{radius},{latitude},{longitude});
                            node["building"](around:{radius},{latitude},{longitude});
                            way["building"](around:{radius},{latitude},{longitude});
                            );
                            out body;
                        """
        response = requests.get(overpass_url, params={'data': overpass_query})

       # Vérifiez si la requête a réussi
        if response.status_code == 200:
            print("Données récupérées avec succès")
            # Afficher la taille des données récupérées pour vérifier
            data = response.json()
            print(f"Nombre d'éléments récupérés : {len(data['elements'])}")
        else:
            print(f"Erreur de récupération des données: {response.status_code}")

        # Convertir les données JSON récupérées en GeoDataFrame
        data = response.json()

        # Initialisation des listes pour chaque type de géométrie
        points = []
        lines = []
        polygons = []

        # Traiter les nœuds (points)
        for element in data['elements']:
            if 'lat' in element and 'lon' in element:
                points.append(Point(element['lon'], element['lat']))

        # Traiter les ways (lignes ou polygones)
        for element in data['elements']:
            if 'nodes' in element:
                if len(element['nodes']) == 2:  # Ligne
                    coords = [(node['lon'], node['lat']) for node in element['nodes']]
                    lines.append(LineString(coords))
                elif len(element['nodes']) > 2:  # Polygone
                    coords = [(node['lon'], node['lat']) for node in element['nodes']]
                    polygons.append(Polygon(coords))

        # Créer un GeoDataFrame
        all_geometry = points + lines + polygons
        gdf = gpd.GeoDataFrame(geometry=all_geometry)

        # Affichage de la carte avec toutes les géométries
        fig, ax = plt.subplots(figsize=(10, 10))
        gdf.plot(ax=ax, color='blue', markersize=5)
        ax.set_title("Carte avec toutes les données géographiques autour de Paris")
        plt.show()

        # Sauvegarder la carte en PNG si nécessaire
        fig.savefig("toutes_donnees_paris.png", dpi=300)
