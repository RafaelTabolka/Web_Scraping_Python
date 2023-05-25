import requests
from bs4 import BeautifulSoup

#Utiliza o Header do Internet Explorer, obtido ao entrar em inspecionar página
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

#Url da única página acessável do internet explorer
url = "https://support.microsoft.com/pt-br/microsoft-edge/este-site-funciona-melhor-no-microsoft-edge-160fa918-d581-4932-9e4e-1075c4713595?ui=pt-br&rs=pt-br&ad=br"

#Método get da biblioteca "requests" para pegar a url da página junto do header
page = requests.get(url,headers=header)

#Método da biblioteca BeautifulSoup para pegar o conteúdo html parser da página
soup = BeautifulSoup(page.content, "html.parser")

#Variável criada contendo qual o nome da class das tags html que queremos
atributos = {'class':'m-skip-to-main'}

#Método utilizado para encontrar todas as tags 'a' com o atributo passado da linha 17 contidos na página
respostas = soup.find_all('a',attrs=atributos)[0]

#Três retornos possíveis: 1: Tudo o que foi encontrado, 2: String que tem dentro de "href", 3: Text existente na tag encontrada
print(respostas) #1
print(respostas['href']) #2
print(respostas.text) #3