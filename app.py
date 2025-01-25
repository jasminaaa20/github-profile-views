from flask import Flask, Response
import requests
import re

app = Flask(__name__)

@app.route('/profile-views.svg')
def profile_views_badge():
    # Fetch profile views
    url = "https://komarev.com/ghpvc/?username=jasminaaa20&style=flat-square"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extract view count
        match = re.search(r'>(\d+)</text>', response.text)
        if match:
            view_count = match.group(1)
            
            # Read the SVG template
            with open('profile-views-badge.svg', 'r') as file:
                svg_template = file.read()
            
            # Replace placeholder with actual views
            svg_content = svg_template.replace('{{VIEWS}}', view_count)
            
            return Response(svg_content, mimetype='image/svg+xml')
    
    # Fallback SVG if fetching fails
    return Response(
        '<svg xmlns="http://www.w3.org/2000/svg" width="110" height="20">' + 
        '<text x="50%" y="50%" text-anchor="middle">Error</text></svg>', 
        mimetype='image/svg+xml'
    )

if __name__ == '__main__':
    app.run(debug=True)