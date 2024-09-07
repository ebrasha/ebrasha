from bs4 import BeautifulSoup
import os

# Load the SVG file
with open('icons.svg', 'r', encoding='utf-8') as file:
    svg_content = file.read()

# Parse the SVG content using BeautifulSoup
soup = BeautifulSoup(svg_content, 'xml')

# Find all individual <svg> elements inside the main SVG
svgs = soup.find_all('svg')

# Directory to save individual icons
output_dir = 'separated_icons'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save each icon as an individual SVG file
for i, svg_tag in enumerate(svgs):
    icon_id = f'icon_{i+1}'
    icon_svg = str(svg_tag)
    with open(f'{output_dir}/{icon_id}.svg', 'w', encoding='utf-8') as icon_file:
        icon_file.write(icon_svg)

print(f'Successfully saved {len(svgs)} icons to the {output_dir} directory.')
