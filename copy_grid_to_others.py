import re

with open('temp-combo-grid.txt', 'r') as f:
    grid_content = f.read()

for file_name in ['cadeira-dobravel.html', 'mesa-dobravel.html']:
    with open(file_name, 'r') as f:
        content = f.read()
    
    # Replace everything from <div class="grid grid-cols-1 md:grid-cols-3 gap-8"> up to the closing </div>
    # of the "O COMBO PERFEITO" section.
    pattern = r'<div class="grid grid-cols-1 md:grid-cols-3 gap-8">.*?(?=    </section>)'
    
    new_content = re.sub(pattern, grid_content + '\n', content, flags=re.DOTALL)
    
    with open(file_name, 'w') as f:
        f.write(new_content)

