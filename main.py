import requests
from bs4 import BeautifulSoup
import functions_framework

@functions_framework.http
def scrap(request):
  params = request.args
  if params['category'] == 'all':
    return scrap_all()
  else:
    return { 'result': scrap_category(params['category']) }

def scrap_category(category):
  if category == 'Pymes':
    url = 'https://4n68r2aa.apicdn.sanity.io/v2023-08-21/data/query/production?query=*%0A%09++%09%5B%0A%09%09%09%09%28_type+%3D%3D+%22blogArticle%22%29%0A++++++++%0A++++++++%26%26+%28%0A%09%09%09%09%09blogCategory-%3Eslug.current+%3D%3D+%22pymes%22%0A%09%09%09%09%29%0A%09%09++%5D+%0A%09%09%09%7C+order%28date+desc%2C+_createdAt+desc%29%0A%09%09%09%7B%0A++++++_type%2C%0A++++++_id%2C%0A++++++slug%2C%0A++++++title%2C%0A%09%09%09excerpt%2C%0A++++++featuredImage%2C%0A++++++_createdAt%2C%0A++++++_updatedAt%2C%0A++++++date%2C%0A++++++author-%3E%2C%0A++++++blogCategory-%3E%2C%0A++++++resourceCategory-%3E%2C%0A++++%7D%5B9...1000%5D&returnQuery=false&perspective=published'
  elif category == 'Xepelin':
    url = 'https://4n68r2aa.apicdn.sanity.io/v2023-08-21/data/query/production?query=*%0A%09++%09%5B%0A%09%09%09%09%28_type+%3D%3D+%22blogArticle%22%29%0A++++++++%0A++++++++%26%26+%28%0A%09%09%09%09%09blogCategory-%3Eslug.current+%3D%3D+%22noticias%22%0A%09%09%09%09%29%0A%09%09++%5D+%0A%09%09%09%7C+order%28date+desc%2C+_createdAt+desc%29%0A%09%09%09%7B%0A++++++_type%2C%0A++++++_id%2C%0A++++++slug%2C%0A++++++title%2C%0A%09%09%09excerpt%2C%0A++++++featuredImage%2C%0A++++++_createdAt%2C%0A++++++_updatedAt%2C%0A++++++date%2C%0A++++++author-%3E%2C%0A++++++blogCategory-%3E%2C%0A++++++resourceCategory-%3E%2C%0A++++%7D%5B0...1000%5D&returnQuery=false&perspective=published'
  elif category == 'Corporativos':
    url = 'https://4n68r2aa.apicdn.sanity.io/v2023-08-21/data/query/production?query=*%0A%09++%09%5B%0A%09%09%09%09%28_type+%3D%3D+%22blogArticle%22%29%0A++++++++%0A++++++++%26%26+%28%0A%09%09%09%09%09blogCategory-%3Eslug.current+%3D%3D+%22corporativos%22%0A%09%09%09%09%29%0A%09%09++%5D+%0A%09%09%09%7C+order%28date+desc%2C+_createdAt+desc%29%0A%09%09%09%7B%0A++++++_type%2C%0A++++++_id%2C%0A++++++slug%2C%0A++++++title%2C%0A%09%09%09excerpt%2C%0A++++++featuredImage%2C%0A++++++_createdAt%2C%0A++++++_updatedAt%2C%0A++++++date%2C%0A++++++author-%3E%2C%0A++++++blogCategory-%3E%2C%0A++++++resourceCategory-%3E%2C%0A++++%7D%5B0...1000%5D&returnQuery=false&perspective=published'
  elif category == 'Educacion Financiera':
    url = 'https://4n68r2aa.apicdn.sanity.io/v2023-08-21/data/query/production?query=*%0A%09++%09%5B%0A%09%09%09%09%28_type+%3D%3D+%22blogArticle%22%29%0A++++++++%0A++++++++%26%26+%28%0A%09%09%09%09%09blogCategory-%3Eslug.current+%3D%3D+%22educacion-financiera%22%0A%09%09%09%09%29%0A%09%09++%5D+%0A%09%09%09%7C+order%28date+desc%2C+_createdAt+desc%29%0A%09%09%09%7B%0A++++++_type%2C%0A++++++_id%2C%0A++++++slug%2C%0A++++++title%2C%0A%09%09%09excerpt%2C%0A++++++featuredImage%2C%0A++++++_createdAt%2C%0A++++++_updatedAt%2C%0A++++++date%2C%0A++++++author-%3E%2C%0A++++++blogCategory-%3E%2C%0A++++++resourceCategory-%3E%2C%0A++++%7D%5B0...1000%5D&returnQuery=false&perspective=published'
  elif category == 'Emprendedores':
    url = 'https://4n68r2aa.apicdn.sanity.io/v2023-08-21/data/query/production?query=*%0A%09++%09%5B%0A%09%09%09%09%28_type+%3D%3D+%22blogArticle%22%29%0A++++++++%0A++++++++%26%26+%28%0A%09%09%09%09%09blogCategory-%3Eslug.current+%3D%3D+%22emprendedores%22%0A%09%09%09%09%29%0A%09%09++%5D+%0A%09%09%09%7C+order%28date+desc%2C+_createdAt+desc%29%0A%09%09%09%7B%0A++++++_type%2C%0A++++++_id%2C%0A++++++slug%2C%0A++++++title%2C%0A%09%09%09excerpt%2C%0A++++++featuredImage%2C%0A++++++_createdAt%2C%0A++++++_updatedAt%2C%0A++++++date%2C%0A++++++author-%3E%2C%0A++++++blogCategory-%3E%2C%0A++++++resourceCategory-%3E%2C%0A++++%7D%5B0...1000%5D&returnQuery=false&perspective=published'
  elif category == 'Casos de exito':
    url = 'https://4n68r2aa.apicdn.sanity.io/v2023-08-21/data/query/production?query=*%0A%09++%09%5B%0A%09%09%09%09%28_type+%3D%3D+%22blogArticle%22%29%0A++++++++%0A++++++++%26%26+%28%0A%09%09%09%09%09blogCategory-%3Eslug.current+%3D%3D+%22empresarios-exitosos%22%0A%09%09%09%09%29%0A%09%09++%5D+%0A%09%09%09%7C+order%28date+desc%2C+_createdAt+desc%29%0A%09%09%09%7B%0A++++++_type%2C%0A++++++_id%2C%0A++++++slug%2C%0A++++++title%2C%0A%09%09%09excerpt%2C%0A++++++featuredImage%2C%0A++++++_createdAt%2C%0A++++++_updatedAt%2C%0A++++++date%2C%0A++++++author-%3E%2C%0A++++++blogCategory-%3E%2C%0A++++++resourceCategory-%3E%2C%0A++++%7D%5B0...1000%5D&returnQuery=false&perspective=published'

  return_array = []
  raw_response = requests.get(url)
  raw_response.encoding = 'utf-8'
  response = raw_response.json()['result']
  for blog in response:
    slug = blog['slug']['current']
    category_slug = blog['blogCategory']['slug']['current']
    blog_request_url = f'https://xepelin.com/blog/{category_slug}/{slug}'
    blog_response = requests.get(blog_request_url, headers={"User-Agent": "curl/7.61.0"})
    soup = BeautifulSoup(blog_response.text, features="html.parser")
    lecture_time = soup.select('div[class*="Text_body__snVk8"]')[0].text.split()[0]
    return_array.append({
      'title': blog['title'],
      'category': category_slug,
      'author': blog['author']['name'],
      'lecture_time': lecture_time,
      'published_date': blog['date']
      })
  return return_array

def scrap_all():
  pymes = scrap('Pymes')
  xepelin = scrap('Xepelin')
  corporatives = scrap('Corporativos')
  financial_education = scrap('Educacion Financiera')
  enterpreneurs = scrap('Emprendedores')
  success_cases = scrap('Casos de exito')

  return { 'result': pymes + xepelin + corporatives + financial_education + enterpreneurs + success_cases }
