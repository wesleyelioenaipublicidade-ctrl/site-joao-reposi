import re

with open('banqueta-mosaico.html', 'r') as f:
    content = f.read()

# Fix mesa link
content = content.replace(
    'href="https://wa.me/5514991267349?text=Ol%C3%A1!%20Vim%20pelo%20site%2C%20quero%20comprar%20a%20unidade%20da%20banqueta%20mosaico"',
    'href="https://wa.me/5514991267349?text=Ol%C3%A1!%20Vim%20pelo%20site%2C%20quero%20comprar%20a%20unidade%20da%20mesa%20dobr%C3%A1vel"',
    1 # We only want to replace the FIRST occurrence AFTER the first product (so the second occurrence overall, wait, let's just do it with regex)
)

