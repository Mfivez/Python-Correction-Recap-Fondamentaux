from chanson import Chanson
from podcast import Podcast
from publicite import Publicite
from playlist import Playlist
from genre import Genre

c1 = Chanson("Shape of You", "Ed Sheeran", 4, Genre.POP)
c2 = Chanson("Bohemian Rhapsody", "Queen", 6, Genre.ROCK)
c3 = Chanson("Take Five", "Dave Brubeck", 5, Genre.JAZZ)

p1 = Podcast("Tech Talk", "Alice", 30)
p2 = Podcast("Histoire du jazz", "Marc", 45)

pub1 = Publicite("Nike", 1)
pub2 = Publicite("Coca-Cola", 2)

playlist = Playlist("Ma playlist préférée")

playlist.ajouter_piste(c1)
playlist.ajouter_piste(pub1)
playlist.ajouter_piste(c2)
playlist.ajouter_piste(p1)
playlist.ajouter_piste(c3)
playlist.ajouter_piste(pub2)
playlist.ajouter_piste(p2)

playlist.afficher_pistes()

playlist.lire_playlist()

print(f"\nDurée totale : {playlist.duree_totale()} minutes")

playlist_rock = playlist.filtrer_par_genre(Genre.ROCK)
playlist_rock.afficher_pistes()

print(f"\nDurée totale playlist ROCK : {playlist_rock.duree_totale()} minutes")