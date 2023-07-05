import requests

API_KEY = '148d4ca9d8ad4614a711190fa33b1524'  # Замените на свой API-ключ Spoonacular

def search_recipe(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={API_KEY}&fillIngredients=True'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Получаем первый рецепт из результатов поиска
        if 'results' in data and len(data['results']) > 0:
            for i in range(0, len(data['results'])):
                recipe_id = data['results'][i]['id']
                recipe_title = data['results'][i]['title']
                recipe_url = f'https://spoonacular.com/recipes/{recipe_title.replace(" ", "-")}-{recipe_id}'

                print(f'Найден рецепт "{recipe_title}": {recipe_url}')
        else:
            print('Рецепт не найден.')

    except requests.exceptions.HTTPError as err:
        print(f'Ошибка при выполнении запроса: {err}')

    except requests.exceptions.RequestException as err:
        print(f'Ошибка при выполнении запроса: {err}')

# Пример использования
user_query = input('Введите запрос для поиска рецепта: ')
search_recipe(user_query)
