создаем виртуальное окружене(сюда будут прописываться наши библиотеки и зависимости)
добавить в гитигнор
python -m venv venv  - устанавливаем виртуальное окружение
далее настраиваем интерпритатор
в pycharm снизу справа -> add new interpritatot -> add local interpritator -> select existing
появится папка venv ее добавляем в gitignore

pip - аналог npm



pip freeze - показывает что установлено в виртуальном окружении

создаем файл requirements.txt и вставляем туда содержимое консоли pip freeze 
далее pip install -r requirements.txt


pytest - управление запуска тестов
pip install pytest
import pytest
pytest название файла должно начинаться с test_
	пример:
		text_demo.py
pytest функции обязательно должны начинать с test_
	пример:
		def test_demo():
			assert 1 == 1 // утверждаю что 1 равно 1
чтобы запустить pytest нужно:
	pytest -v -s
	// -v будет писать pass
	// -s выводит содержимое print()
	
в pytest существуют пред и пос условия:
		для этого import pytest
		
		@pytest.fixture()
		def before_after():
			print("before test")
			yield // запуск теста
			print("\nafter test")
	означает что эта функция будет запускаться перед тестами и после	
	добавляем в функцию параметр фикстуры	
		def test_demo(before_after):
		
чтобы запустить тесты из одного файла то 
	pytest -v -s название файла
чтобы запустить определенный тест из одного файла 
	pytest -v -s название файла::название функции 
	
добавляем в requirements.txt:
	pip freeze > requirements.txt	
	
установка selenium:
		pip install selenium
		from selenium import webdriver
		from selenium.webdriver.common.by import By
		webdriver.Chrome()
	пример:	
	from selenium import webdriver
	import pytest

	@pytest.fixture() //пред условие
	def driver():
		browser = webdriver.Chrome() //открываем хром
		browser.maximize_window() // на весь экран
		browser.implicitly_wait(3) // если не нашел то подожди 3 секунды
		yield browser //возвращаем браузер
		browser.close()
время ожидания(супер гавнокод):
	import time
	time.sleep(3)
	чтобы не исползовать такой говнокод надо привязываться к элементам которые меняются после загрузки страницы
	например: урл или класс актив у выбраного меню
		
	

	
		
Создаем структуру автотестов:
	папка pages : 
		тут мы описываем страницы с которыми работаем
		описываем первоначальные действия типо открываем страницу и кликаем на элемент
		
		код: страница homepage.py
			from selenium.webdriver.common.by import By
			class HomePage:
				def __init__(self, browser): //параметр browser приходит из файла test_site.py
					self.browser = browser
				def open(self):
					self.browser.get('https://demoblaze.com')
				def click_galaxy_s6(self):
					galaxy_s6 = self.browser.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
					galaxy_s6.click()
		код: страница product.py
			from selenium.webdriver.common.by import By
			class ProductPage:
				def __init__(self, browser):
					self.browser = browser
				def check_title_is(self, title):
					page_title = self.browser.find_element(By.CSS_SELECTOR, 'h2')
					assert page_title.text == 'Samsung galaxy s6'
	папка test:
		тут лежат тесты
		from pages.homepage import HomePage //забираем классы со своих страниц
		from pages.product import ProductPage

		def test_open_s6(browser): 
			homepage = HomePage(browser) // тут передаем в класс параметр browser
			homepage.open() //запускаем функцию из pages.homepage
			homepage.click_galaxy_s6()
			product_page = ProductPage(browser)
			product_page.check_title_is('Samsung galaxy s6')
	файл conftest.py : 
		для конфигурации тестов - сюда переносим общие настройки типо @pytest.fixture()
		from selenium import webdriver
		import pytest

		@pytest.fixture()
		def browser():
			browser = webdriver.Chrome()
			browser.maximize_window()
			browser.implicitly_wait(3)
			yield browser
			browser.close()
			
			
	Запускаем pytest -v		