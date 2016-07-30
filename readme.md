# pokemon-bot

## Description

A pokemon go bot that will catch them all.

## Summary

A pokemon go bot written in python that will catch pokemons and farm poketstops.
Developed on linux but it may also work on windows.
No phone is needed this will run on your computer and interact with the game server.

## Installation

pip install -r requirements.txt

Add your credentials to go.cfg

```sh
vim go.cfg
```

    [pokemon]
    username     = email@address.com
    password     = password
    map_location = 'Nobelparken, Nobelgatan, Stockholm, Sverige'
    auth         = google
    geo_key      = 

### Usage

No arguments will list usage menu.

```sh

$:~/dev/pokemon-bot$ ./go.py 

 _____     _                        _____     
|  _  |___| |_ ___ _____ ___ ___   |   __|___ 
|   __| . | '_| -_|     | . |   |  |  |  | . |
|__|  |___|_,_|___|_|_|_|___|_|_|  |_____|___|

Mikael Kall [kall.micke@gmail.com]

Usage: go.py <OPTIONS> 

General Options

    pokestops   Spin pokestops
    pokemons    Hunt pokemons
    profile     View profile
    inventory   View inventory

```

### Prerequisite

python 2.7
pip2 

### Notes

Sometimes the gameserver send malformed data that the API cant handle?
Unsure what the problem is yet but just rerun the application and it will work.   

### Credits

Have used this pokemon api to create this application so I take no credits for the API.
https://github.com/rubenvereecken/pokemongo-api
