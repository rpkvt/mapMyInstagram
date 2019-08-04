
import instaloader
import simplekml
import itertools

# Get instance
L = instaloader.Instaloader(download_geotags=True)

# Optionally, login or load session
USER = 'instagram user name'
PROFILE = USER
PASSWORD = 'instagram password'
L.login(USER, PASSWORD)        # (login)

profile = instaloader.Profile.from_username(L.context, PROFILE)

count = 0;
locations = []
urls = []
for post in profile.get_saved_posts():
    if post.location is not None:
        print(post.location.name)
        #print(post.url)
        locations.append(post.location)
        urls.append(post.url)


kml=simplekml.Kml()

for (place,link) in zip(locations,urls):
    pnt = kml.newpoint(name=place.name, coords=[(place.lng,place.lat)])
    pnt.description = '<img src="' + link +'" alt="picture" width="400" height="300" align="left" />'

kml.save('locations.kml')
