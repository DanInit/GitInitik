from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.img_shiny = self.get_shiny()
        self.hp = randint(200, 400)
        self.power = randint(30,60)

        def attack(self, enemy):
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    # Метод для получения имени покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"

    def get_shiny(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_shiny'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return (f"\nИмя твоего покеомона: {self.name}",
                f"\nЗдоровье покемона: {self.hp}",
                f"\nСила покемона: {self.power}")

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    #Метод класса для получения картинки покемона
    def show_shiny(self):
        return self.img_shiny

    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):
    def magic(self, enemy):
        super_power = randint(40, 70)
        self.hp += super_power
        result = super().attack(enemy)
        return result+f"\nМаг исцелил себя на {super_power}"

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power = super_power
        return result+f"\nБоец применил супер атаку силой {super_power}"



