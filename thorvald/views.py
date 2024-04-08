from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import Fighter
from .serializers import FighterSerializer
from nanoid import generate
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class FighterViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer

@api_view(["GET"])
def get_enemies(request):
    enemies = [
        {
           "id": generate(size=10),
            "name": "Guard",
            "strength": 1,
            "fullHP": 10,
            "maxHP": 10,
            "armor": 0,
            "avatar": "https://64.media.tumblr.com/28146c7955b7025d394d43467f64fb52/tumblr_p0p3ljjsir1tibuboo1_1280.jpg",
            "XP": 5,
            "level": 1,
            "isDead": False,
        },
        {
            "id": generate(size=10),
            "name": "Archer",
            "strength": 2,
            "fullHP": 20,
            "maxHP": 20,
            "armor": 1,
            "avatar": "https://i.pinimg.com/originals/69/5a/0c/695a0cdeea901966afdbbf931f848f7d.jpg",
            "XP": 10,
            "level": 1,
            "isDead": False,
        },
        {
            "id": generate(size=10),
            "name": "Warrior",
            "strength": 3,
            "fullHP": 30,
            "maxHP": 30,
            "armor": 3,
            "avatar": "https://wallpapersmug.com/large/ad2083/fantasy-warrior-art.jpg",
            "XP": 15,
            "level": 1,
            "isDead": False,
        },
        {
           "id": generate(size=10),
            "name": "Knight",
            "strength": 4,
            "fullHP": 50,
            "maxHP": 50,
            "armor": 5,
            "avatar": "https://steamuserimages-a.akamaihd.net/ugc/911296644864742654/0F8D9C3A40ABB6D62C3EFA6750F1AFD2372A251F/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
            "XP": 20,
            "level": 1,
            "isDead": False,
        },
        {
            "id": generate(size=10),
            "name": "Guardsman",
            "strength": 5,
            "fullHP": 70,
            "maxHP": 70,
            "armor": 8,
            "avatar": "https://i.pinimg.com/originals/63/fb/65/63fb656fcb22a817cefa67fa2ee27ad1.jpg",
            "XP": 30,
            "level": 1,
            "isDead": False,
        },
        {
           "id": generate(size=10),
            "name": "Final",
            "strength": 10,
            "fullHP": 10,
            "maxHP": 10,
            "armor": 10,
            "avatar": "",
            "XP": 10,
            "level": 1,
            "isDead": False,
        },
    ]

    return Response(enemies)


@api_view(["GET"])
def get_thorvald(request):
    thorvald = {
        "id": "thorvald",
        "name": "Thorvald",
        "strength": 5,
        "fullHP": 100,
        "maxHP": 100,
        "armor": 0,
        "avatar": "https://i.pinimg.com/originals/31/46/1b/31461b321a171a627646a836b259d937.png",
        "XP": 0,
        "level": 1,
        "isDead": False,
        "levelsScore": 10,
    }

    return Response(thorvald)