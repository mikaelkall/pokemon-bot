#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pokemon Go bot.

Note to create this application I have used the API code from 
https://github.com/rubenvereecken/pokemongo-api so I will not take any credits for the API code.

"""

from ConfigParser import SafeConfigParser
import datetime
import time
import sys
import os
import random

try:
    sys.path.insert(1, os.path.join(sys.path[0], '../pogo'))
    from custom_exceptions import GeneralPogoException
    from api import PokeAuthSession
    from location import Location
    from pokedex import pokedex
    from inventory import items
except:
    sys.path.insert(1, os.path.join(sys.path[0], 'pogo'))
    from custom_exceptions import GeneralPogoException
    from api import PokeAuthSession
    from location import Location
    from pokedex import pokedex
    from inventory import items


class Polib:

    def __init__(self):
        """Load settings into this class namespace"""
        config = self.__load_settings()
        for key, value in dict(config.items('pokemon')).iteritems():
            setattr(self, str(key), str(value))


    def __load_settings(self):
        config = SafeConfigParser()
        path = os.path.dirname(os.path.abspath(__file__))
        filename = "%s/../go.cfg" % path
        if os.path.isfile(filename) == False:
            self.puts('error',"Can't find config: %s" % (filename))
            sys.exit(1)

        config.read(filename)
        return config


    def __puts(self, tp, msg):
        """Output messages in fancy colors."""

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        if tp == "info":
            print("%s%s|%s| %s" % ('\033[93m', "➜ ".decode('utf-8'), st , msg))
        elif tp == "warning":
            print("%s%s|%s| %s" % ('\033[93m', "➜ ".decode('utf-8'), st , msg))
        elif tp == "error":
            print("%s%s|%s| %s" % ('\033[91m', "✖ ".decode('utf-8'), st , msg))
        elif tp == "success":
            print("%s%s|%s| %s" % ('\033[92m', "✔ ".decode('utf-8'), st , msg))


    def __api_connect(self):

	api_user = str(self.username).strip()
	api_pass = str(self.password).strip()
	api_auth = str(self.auth).strip()
	api_geo  = str(self.geo_key).strip()
	api_map  = str(self.map_location).strip()

        # Check service
        if self.auth not in ['ptc', 'google']:
            self.__puts('error',"Invalid auth service %s" % ( self.auth ))
            sys.exit(-1)

	# Create PokoAuthObject
        poko_session = PokeAuthSession(
            api_user,
            api_pass,
            api_auth,
            geo_key=api_geo
        )

        if self.map_location:
            session = poko_session.authenticate(locationLookup=api_map)
        else:
            session = poko_session.authenticate()

        if session:
	    return session
        else:
            self.__puts('error','Session not created successfully')
	    sys.exit(-1)


    def __sortCloseForts(self, session):
        try:
            self.__puts('info', "Sorting Nearest Forts:")
            cells = session.getMapObjects()
            latitude, longitude, _ = session.getCoordinates()
            ordered_forts = []
            for cell in cells.map_cells:
                for fort in cell.forts:
                    dist = Location.getDistance(
                        latitude,
                        longitude,
                        fort.latitude,
                        fort.longitude
                    )
                    if fort.type == 1:
                        ordered_forts.append({'distance': dist, 'fort': fort})

            ordered_forts = sorted(ordered_forts, key=lambda k: k['distance'])
            return [instance['fort'] for instance in ordered_forts]
        except:
	    self.__puts('info','Malformed response since service is unstable? Try again..')     

    def __walkAndSpin(self, session, fort):
        if fort:
            details = session.getFortDetails(fort)
	    self.__puts('info', "Spinning the Fort \"%s\":" % details.name )

            session.walkTo(fort.latitude, fort.longitude, step=3.2)
            fortResponse = session.getFortSearch(fort)
	    self.__puts('info', fortResponse )


    def __walkAndSpinMany(self, session, forts):
        try:
            for fort in forts:
                self.__walkAndSpin(session, fort)
        except:
            self.__puts('info','Malformed response since service is unstable? Try again..')


    # Grab the nearest pokemon details
    def __findBestPokemon(self, session):
        # Get Map details and print pokemon
        self.__puts('info', "Finding Nearby Pokemon.")
        cells = session.getMapObjects()
        closest = float("Inf")
        best = -1
        pokemonBest = None
        latitude, longitude, _ = session.getCoordinates()
        self.__puts('info', "Current pos: %f, %f" % (latitude, longitude))
        for cell in cells.map_cells:
            # Heap in pokemon protos where we have long + lat
            pokemons = [p for p in cell.wild_pokemons] + [p for p in cell.catchable_pokemons]
            for pokemon in pokemons:
                # Normalize the ID from different protos
                pokemonId = getattr(pokemon, "pokemon_id", None)
                if not pokemonId:
                    pokemonId = pokemon.pokemon_data.pokemon_id

                # Find distance to pokemon
                dist = Location.getDistance(
                    latitude,
                    longitude,
                    pokemon.latitude,
                    pokemon.longitude
                )

                # Log the pokemon found
                self.__puts('info',"%s, %f meters away" % (
                    pokedex[pokemonId],
                    dist
                ))

                rarity = pokedex.getRarityById(pokemonId)
                # Greedy for rarest
                if rarity > best:
                    pokemonBest = pokemon
                    best = rarity
                    closest = dist
                # Greedy for closest of same rarity
                elif rarity == best and dist < closest:
                    pokemonBest = pokemon
                    closest = dist
        return pokemonBest


    # Catch a pokemon at a given point
    def __walkAndCatch(self, session, pokemon):
        if pokemon:
            self.__puts('info',"Catching %s:" % pokedex[pokemon.pokemon_data.pokemon_id])
            session.walkTo(pokemon.latitude, pokemon.longitude, step=3.2)
            self.__puts('info', self.__encounterAndCatch(session, pokemon))


    def __encounterAndCatch(self, session, pokemon, thresholdP=0.5, limit=5, delay=2):
        # Start encounter
        encounter = session.encounterPokemon(pokemon)

        # Grab needed data from proto
        chances = encounter.capture_probability.capture_probability
        balls = encounter.capture_probability.pokeball_type
        bag = session.checkInventory().bag

        # Have we used a razz berry yet?
        berried = False

        # Make sure we aren't oer limit
        count = 0

        # Attempt catch
        while True:
            bestBall = items.UNKNOWN
            altBall = items.UNKNOWN

            # Check for balls and see if we pass
            # wanted threshold
            for i in range(len(balls)):
                if balls[i] in bag and bag[balls[i]] > 0:
                    altBall = balls[i]
                    if chances[i] > thresholdP:
                        bestBall = balls[i]
                        break

            # If we can't determine a ball, try a berry
            # or use a lower class ball
            if bestBall == items.UNKNOWN:
                if not berried and items.RAZZ_BERRY in bag and bag[items.RAZZ_BERRY]:
                    self.__puts('info', "Using a RAZZ_BERRY")
                    session.useItemCapture(items.RAZZ_BERRY, pokemon)
                    berried = True
                    time.sleep(delay)
                    continue

                # if no alt ball, there are no balls
                elif altBall == items.UNKNOWN:
                    raise GeneralPogoException("Out of usable balls")
                else:
                    bestBall = altBall

            # Try to catch it!!
            self.__puts('info', "Using a %s" % items[bestBall])
            attempt = session.catchPokemon(pokemon, bestBall)
            time.sleep(delay)

            # Success or run away
            if attempt.status == 1:
                return attempt

            # CATCH_FLEE is bad news
            if attempt.status == 3:
                self.__puts('info', "Possible soft ban.")
                return attempt

            # Only try up to x attempts
            count += 1
            if count >= limit:
                self.__puts('info', "Over catch limit")
                return None


    # Find the fort closest to user
    def __findClosestFort(self, session):
        # Find nearest fort (pokestop)
        self.__puts('info', "Finding Nearest Fort:")
        return self.__sortCloseForts(session)[0]


    # Understand this function before you run it.
    # Otherwise you may flush pokemon you wanted.
    def __cleanPokemon(self, session, thresholdCP=50):
        self.__puts('info', "Cleaning out Pokemon...")
        party = session.checkInventory().party
        evolables = [pokedex.PIDGEY, pokedex.RATTATA, pokedex.ZUBAT]
        toEvolve = {evolve: [] for evolve in evolables}
        for pokemon in party:
            # If low cp, throw away
            if pokemon.cp < thresholdCP:
                # It makes more sense to evolve some,
                # than throw away
                if pokemon.pokemon_id in evolables:
                    toEvolve[pokemon.pokemon_id].append(pokemon)
                    continue

                # Get rid of low CP, low evolve value
                self.__puts('info', "Releasing %s" % pokedex[pokemon.pokemon_id])
                session.releasePokemon(pokemon)

        # Evolve those we want
        for evolve in evolables:
            candies = session.checkInventory().candies[evolve]
            pokemons = toEvolve[evolve]
            # release for optimal candies
            while candies // pokedex.evolves[evolve] < len(pokemons):
                pokemon = pokemons.pop()
                self.__puts('info', "Releasing %s" % pokedex[pokemon.pokemon_id])
                session.releasePokemon(pokemon)
                time.sleep(1)
                candies += 1

            # evolve remainder
            for pokemon in pokemons:
                self.__puts('info', "Evolving %s" % pokedex[pokemon.pokemon_id])
                self.__puts('info', session.evolvePokemon(pokemon))
                time.sleep(1)
                session.releasePokemon(pokemon)
                time.sleep(1)


    def __cleanInventory(self, session):
        self.__puts('info', "Cleaning out Inventory...")
        bag = session.checkInventory().bag

        # Clear out all of a crtain type
        tossable = [items.POTION, items.SUPER_POTION, items.REVIVE]
        for toss in tossable:
            if toss in bag and bag[toss]:
                session.recycleItem(toss, bag[toss])

        # Limit a certain type
        limited = {
            items.POKE_BALL: 50,
            items.GREAT_BALL: 100,
            items.ULTRA_BALL: 150,
            items.RAZZ_BERRY: 25
        }
        for limit in limited:
            if limit in bag and bag[limit] > limited[limit]:
                session.recycleItem(limit, bag[limit] - limited[limit])


    # Basic bot
    def __simpleBot(self, session):
    # Trying not to flood the servers
        cooldown = 1

        # Run the bot
        while True:
            forts = self.__sortCloseForts(session)
            #self.__cleanPokemon(session, thresholdCP=300)
            #self.__cleanInventory(session)
            try:
                for fort in forts:
                    pokemon = self.__findBestPokemon(session)
                    self.__walkAndCatch(session, pokemon)
                    self.__walkAndSpin(session, fort)
                    cooldown = 1
                    time.sleep(1)

            # Catch problems and reauthenticate
            except GeneralPogoException as e:
                self.__puts('error',"GeneralPogoException raised: %s" % e)
                session = poko_session.reauthenticate(session)
                time.sleep(cooldown)
                cooldown *= 2

            except Exception as e:
                self.__puts('error',"Exception raised: %s" % e)
                session = poko_session.reauthenticate(session)
                time.sleep(cooldown)
                cooldown *= 2

    # Basic bot
    def __simpleBot2(self):

        api_user = str(self.username).strip()
        api_pass = str(self.password).strip()
        api_auth = str(self.auth).strip()
        api_geo  = str(self.geo_key).strip()
        api_map  = str(self.map_location).strip()

        # Check service
        if self.auth not in ['ptc', 'google']:
            self.__puts('error',"Invalid auth service %s" % ( self.auth ))
            sys.exit(-1)

        # Create PokoAuthObject
        poko_session = PokeAuthSession(
            api_user,
            api_pass,
            api_auth,
            geo_key=api_geo
        )

        if self.map_location:
            session = poko_session.authenticate(locationLookup=api_map)
        else:
            session = poko_session.authenticate()

        if session:
            # Trying not to flood the servers
            cooldown = 1

            # Run the bot
            while True:
                forts = self.__sortCloseForts(session)
                #self.__cleanPokemon(session, thresholdCP=300)
                #self.__cleanInventory(session)
                try:
                    for fort in forts:
                        pokemon = self.__findBestPokemon(session)
                        self.__walkAndCatch(session, pokemon)
                        self.__walkAndSpin(session, fort)
                        cooldown = 1
                        time.sleep(1)

                # Catch problems and reauthenticate
                except GeneralPogoException as e:
                    self.__puts('error',"GeneralPogoException raised: %s" % e)
                    session = poko_session.reauthenticate(session)
                    time.sleep(cooldown)
                    cooldown *= 2

                except Exception as e:
                    self.__puts('error',"Exception raised: %s" % e)
                    session = poko_session.reauthenticate(session)
                    time.sleep(cooldown)
                    cooldown *= 2


    def pokestops(self):

        if self.map_location:
	    self.__puts('info', "Walks and spin all poketstop close to your location.")
	    session = self.__api_connect()
            forts = self.__sortCloseForts(session)
            try:
                self.__walkAndSpinMany(session, forts)
            except:
		self.__puts('info','Malformed response since service is unstable? Try again..')

     
    def pokemons(self):
        try:
            self.__puts('info', "Walks and catch all pokemons close to your location.")
            session = self.__api_connect()
	    self.__simpleBot2()
        except:
            self.__puts('info','Malformed response since service is unstable? Try again..')
		

    def get_inventory(self):
        try:
            self.__puts('info', "Get Inventory.")
	    session = self.__api_connect()
            print(session.getInventory())
	except:
	    self.__puts('info','Malformed response since service is unstable? Try again..')


    def get_profile(self):
	try:
	    self.__puts("info","Get Profile.")
            session = self.__api_connect()
            print session.getProfile()
	except:
	    self.__puts('info','Malformed response since service is unstable? Try again..')

