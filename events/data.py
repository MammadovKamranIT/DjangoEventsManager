from copy import deepcopy
from datetime import datetime
from typing import Any



_EVENTS: list[dict[str, Any]] =  [


            {

                "id": 1,
                "title": "ADEX 2026 – Azerbaijan International Defence Exhibition",
                "content": "International exhibition focused on defence, security, military technology, and related industries.",
                "category": "Exhibition",
                "location": "Baku Expo Center, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 2,
                "title": "SECUREX Caspian 2026",
                "content": "International exhibition covering homeland security, protection, and rescue equipment.",
                "category": "Exhibition",
                "location": "Baku Expo Center, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 3,
                "title": "Baku 2026 World Aquatics Swimming World Cup",
                "content": "International swimming competition featuring elite athletes from around the world.",
                "category": "Sports",
                "location": "Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 4,
                "title": "GastroFest 2026",
                "content": "Food festival featuring culinary experiences and food-related events.",
                "category": "Food / Festival",
                "location": "Icherisheher, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 5,
                "title": "Baku World Senior Judo Championships 2026",
                "content": "International judo competition featuring senior athletes competing for world titles.",
                "category": "Sports",
                "location": "Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 6,
                "title": "Game Summit 2026",
                "content": "International event focused on games, entertainment, and the gaming industry.",
                "category": "Conference / Festival",
                "location": "Baku Convention Center, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 7,
                "title": "OMNI AI Summit 2026",
                "content": "Technology summit focused on artificial intelligence, emerging technologies, and practical AI applications.",
                "category": "Technology / Conference",
                "location": "Baku Convention Center, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 8,
                "title": "BakuBuild 2026",
                "content": "International construction exhibition covering construction, building materials, and related industries.",
                "category": "Exhibition",
                "location": "Baku Expo Center, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 9,
                "title": "12th Baku International Book Fair",
                "content": "International book fair bringing together publishers, authors, and readers.",
                "category": "Cultural / Exhibition",
                "location": "Baku Expo Center, Baku, Azerbaijan",
                "current_status": "Upcoming"
            },
            {

                "id": 10,
                "title": "Baku International Arts Festival 2026",
                "content": "Multidisciplinary arts festival featuring concerts, ballet, theatre, film screenings, artist meetings, and masterclasses.",
                "category": "Arts / Festival",
                "location": "Baku, Azerbaijan",
                "current_status": "Upcoming"
            }


        ]



_next_id = 11



def list_events() -> list[dict[str, Any]]:

    return deepcopy(_EVENTS)



def get_event(event_id: int) -> dict[str, Any]| None:

    for event in _EVENTS:
        if event["id"] == event_id:
            return deepcopy(event)
    return None



def create_event (*, title: str, content: str, current_status: list[str], category: str,) -> dict[str, Any]:

    global _next_id
    event = {

        "id": _next_id,
        "title": title.strip(),
        "content": content.strip(),
        "current_status": current_status,
        "category":  category.strip(),



    }

    _EVENTS.append(event)
    _next_id += 1
    return deepcopy(event)



def update_event(

event_id: int,
*,
title:str,
content:str,
current_status:list[str],
category: str,)-> dict[str, Any] | None:
    for event in _EVENTS:
        if event["id"] == event_id:
            event["title"] = title.strip()
            event["content"] = content.strip()
            event["current_status"] = current_status
            event["category"] = category.strip()
            return deepcopy(event)
        return None
    return None



def delete_event(event_id: int) -> bool:
    global _EVENTS
    before = len(_EVENTS)
    _EVENTS = [n for n in _EVENTS if n['id'] != event_id]
    return before != len(_EVENTS)
