<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import os
import sentiment_analysis as sa
<<<<<<< Updated upstream


=======
import webbrowser
import threading

is_open = False
>>>>>>> Stashed changes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

<<<<<<< Updated upstream
# Configuración para cargar archivos
app.config['UPLOAD_FOLDER'] = 'static/images'  # Carpeta donde se guardarán las imágenes
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limitar tamaño máximo a 16 MB

# Nombres de archivo para almacenar los DataFrames
users_file = '../Datasets/users.csv'
hotels_file = '../Datasets/hotels.csv'
comments_file = '../Datasets/comments.csv'

# Inicialización global de los DataFrames
users_df = None
hotels_df = None
comments_df = None

# Cargar DataFrames desde disco
def load_dataframes():
=======
# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'static/images'  # Folder to store images
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

# Filenames for storing DataFrames
users_file = 'src/Datasets/users.csv'
hotels_file = 'src/Datasets/hotels.csv'
comments_file = 'src/Datasets/comments.csv'

# Load DataFrames from disk
def load_dataframes():
    """
    Loads the users, hotels, and comments DataFrames from disk.
    If the files don't exist, it initializes default DataFrames.
    """
>>>>>>> Stashed changes
    global users_df, hotels_df, comments_df

    if os.path.exists(users_file):
        users_df = pd.read_csv(users_file)
    else:
<<<<<<< Updated upstream
        # Crear DataFrame con usuario por defecto 'admin'
        users_df = pd.DataFrame([{'name': 'admin', 'username': 'admin', 'password': 'admin'}])
        # Guardar el DataFrame en el archivo para que se mantenga registrado
=======
        # Create a default DataFrame with an 'admin' user
        users_df = pd.DataFrame([{'name': 'admin', 'username': 'admin', 'password': 'admin'}])
        # Save the DataFrame to file to maintain persistence
>>>>>>> Stashed changes
        users_df.to_csv(users_file, index=False)

    if os.path.exists(hotels_file):
        hotels_df = pd.read_csv(hotels_file)
    else:
<<<<<<< Updated upstream
        hotels_df = pd.DataFrame(columns=['name', 'address', 'image', 'rating', 'description','totalscore','cantcomment'])
=======
        hotels_df = pd.DataFrame(columns=['name', 'address', 'image', 'rating', 'description', 'totalscore', 'cantcomment'])
>>>>>>> Stashed changes

    if os.path.exists(comments_file):
        comments_df = pd.read_csv(comments_file)
    else:
<<<<<<< Updated upstream
        comments_df = pd.DataFrame(columns=['username', 'hotel_name', 'hotel_address' ,'comment', 'sentiment', 'score','rating'])

    return users_df, hotels_df, comments_df

# Guardar DataFrames en disco
def save_dataframes():
=======
        comments_df = pd.DataFrame(columns=['username', 'hotel_name', 'hotel_address', 'comment', 'sentiment', 'score', 'rating'])

    return users_df, hotels_df, comments_df

# Save DataFrames to disk
def save_dataframes():
    """
    Saves the current state of the users, hotels, and comments DataFrames to disk.
    """
>>>>>>> Stashed changes
    global users_df, hotels_df, comments_df
    users_df.to_csv(users_file, index=False)
    hotels_df.to_csv(hotels_file, index=False)
    comments_df.to_csv(comments_file, index=False)

<<<<<<< Updated upstream
# Cargar los DataFrames al inicio
users_df, hotels_df, comments_df = load_dataframes()


# Simulación de un modelo transformer (esto debería ser reemplazado por un modelo real)
def mock_sentiment_analysis(comment):
    clean=sa.CleanText()
    lower_comment=str(comment).lower() if isinstance(comment, str) else str(comment)
    process_comment=sa.remove_numbers(sa.remove_punct(clean(sa.remove_emoji(lower_comment))[0][0]))
=======
# Load the DataFrames at the start
users_df, hotels_df, comments_df = load_dataframes()

# Mock function simulating a transformer model for sentiment analysis
def mock_sentiment_analysis(comment):
    """
    Simulates sentiment analysis on a comment using a mock transformer model.
    
    Args:
        comment (str): The comment to analyze.
    
    Returns:
        tuple: The sentiment, score, and processed comment score.
    """
    clean = sa.CleanText()
    lower_comment = str(comment).lower() if isinstance(comment, str) else str(comment)
    process_comment = sa.remove_numbers(sa.remove_punct(clean(sa.remove_emoji(lower_comment))[0][0]))
>>>>>>> Stashed changes
    return sa.sentiment_analysis(process_comment)

@app.route('/')
def home():
<<<<<<< Updated upstream
=======
    """
    Renders the login page as the home route.
    """
>>>>>>> Stashed changes
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
<<<<<<< Updated upstream
=======
    """
    Handles user login functionality. Verifies the user's credentials 
    and redirects based on user type (admin or regular user).
    """
>>>>>>> Stashed changes
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

<<<<<<< Updated upstream
        # Verificar si el usuario existe en el DataFrame
=======
        # Check if the user exists in the DataFrame
>>>>>>> Stashed changes
        user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]

        if not user.empty:
            session['username'] = username

<<<<<<< Updated upstream
            # Verificar si el usuario es administrador
            if username == "admin":  # Cambia "admin" por el nombre del usuario administrador real
=======
            # Check if the user is an admin
            if username == "admin":  # Change "admin" to the real admin username
>>>>>>> Stashed changes
                session['is_admin'] = True
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('hotels'))
        else:
<<<<<<< Updated upstream
            return "Invalid credentials", 401  # Respuesta adecuada si las credenciales son inválidas

    return render_template('login.html')  # Para solicitudes GET, renderiza el formulario de inicio de sesión


@app.route('/register', methods=['GET', 'POST'])
def register():
=======
            return "Invalid credentials", 401  # Response for invalid credentials

    return render_template('login.html')  # Render login form for GET requests

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration functionality. 
    Adds a new user to the users DataFrame and saves it.
    """
>>>>>>> Stashed changes
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

<<<<<<< Updated upstream
        # Verificar si el usuario ya existe
        existing_user = users_df[users_df['username'] == username]

        if not existing_user.empty:
            return "Username already exists", 400  # Respuesta adecuada si el usuario ya existe

        # Si el usuario no existe, agregarlo al DataFrame
        new_user_data = {
            "name": name,
            "username": username,
            "password": password  # Asegúrate de manejar las contraseñas de forma segura en producción
        }

        users_df.loc[len(users_df)] = new_user_data
        save_dataframes()  # Guardar después de agregar un nuevo usuario

        return redirect(url_for('login'))  # Redirigir a la página de inicio de sesión

    return render_template('register.html')  # Para solicitudes GET, renderiza el formulario de registro

@app.route('/hotels')
def hotels():
=======
        # Check if the user already exists
        existing_user = users_df[users_df['username'] == username]

        if not existing_user.empty:
            return "Username already exists", 400  # Response if username is taken

        # Add new user to the DataFrame
        new_user_data = {
            "name": name,
            "username": username,
            "password": password  # Handle passwords securely in production
        }

        users_df.loc[len(users_df)] = new_user_data
        save_dataframes()  # Save after adding a new user

        return redirect(url_for('login'))  # Redirect to login page

    return render_template('register.html')  # Render registration form for GET requests

@app.route('/hotels')
def hotels():
    """
    Renders the hotels page with a list of all hotels.
    """
>>>>>>> Stashed changes
    return render_template('hotels.html', hotels=hotels_df.to_dict(orient='records'))

@app.route('/hotel/<hotel_name>', methods=['GET', 'POST'])
def hotel_details(hotel_name):
<<<<<<< Updated upstream
    global hotels_df, comments_df
    # Obtener el hotel_address desde los parámetros de consulta
    hotel_address = request.args.get('hotel_address')
    if request.method == 'POST':
        comment = request.form['comment']
        rating = int(request.form['rating'])  # Obtener el rating enviado desde el formulario

        sentiment, score, comment_score = mock_sentiment_analysis(comment)

        # Agregar comentario y guardar cambios
        comments_df.loc[len(comments_df)] = [session['username'], hotel_name,hotel_address ,comment, sentiment, score,rating]

        # Filtrar los comentarios del hotel actual
        hotel_comments = comments_df[(comments_df['hotel_name'] == hotel_name) & (comments_df['hotel_address'] == hotel_address)]

        # Actualizar el dataframe de hoteles con el nuevo comentario y rating
        if not hotel_comments.empty:
            # Buscar el hotel correspondiente por nombre y dirección
            hotel_idx = hotels_df[(hotels_df['name'] == hotel_name) & (hotels_df['address'] == hotel_address)].index[0]

            # Actualizar el 'totalscore' sumando el 'comment_score' + (1.5 * rating)
            final_score=comment_score + (1.5 * rating)
            hotels_df.loc[hotel_idx, 'totalscore'] += final_score

            # Incrementar el contador de comentarios 'cantcomment'
            hotels_df.loc[hotel_idx, 'cantcomment'] += 1

            # Actualizar el 'rating' del hotel dividiendo 'totalscore' entre 'cantcomment'
=======
    """
    Displays details of a specific hotel, including user comments.
    Allows users to submit a new comment and rating for the hotel.
    
    Args:
        hotel_name (str): The name of the hotel.
    """
    global hotels_df, comments_df

    # Get hotel address from query parameters
    hotel_address = request.args.get('hotel_address')

    if request.method == 'POST':
        comment = request.form['comment']
        rating = int(request.form['rating'])  # Get rating from form

        sentiment, score, comment_score = mock_sentiment_analysis(comment)

        # Add the comment and save changes
        comments_df.loc[len(comments_df)] = [session['username'], hotel_name, hotel_address, comment, sentiment, score, rating]

        # Filter comments for the current hotel
        hotel_comments = comments_df[(comments_df['hotel_name'] == hotel_name) & (comments_df['hotel_address'] == hotel_address)]

        # Update the hotels DataFrame with new comment and rating
        if not hotel_comments.empty:
            hotel_idx = hotels_df[(hotels_df['name'] == hotel_name) & (hotels_df['address'] == hotel_address)].index[0]
            
            # Update 'totalscore' by adding 'comment_score' + (1.5 * rating)
            final_score = comment_score + (1.5 * rating)
            hotels_df.loc[hotel_idx, 'totalscore'] += final_score

            # Increment comment count
            hotels_df.loc[hotel_idx, 'cantcomment'] += 1

            # Update hotel rating by dividing 'totalscore' by 'cantcomment'
>>>>>>> Stashed changes
            hotels_df.loc[hotel_idx, 'rating'] = hotels_df.loc[hotel_idx, 'totalscore'] / hotels_df.loc[hotel_idx, 'cantcomment']

            hotels_df = hotels_df.sort_values(by='rating', ascending=False)

<<<<<<< Updated upstream
        # Guardar los cambios en los DataFrames después de agregar el comentario
        save_dataframes()

    # Obtener la información del hotel por nombre y dirección
=======
        # Save changes to the DataFrames after adding the comment
        save_dataframes()

    # Get hotel information by name and address
>>>>>>> Stashed changes
    hotel_info = hotels_df[(hotels_df['name'] == hotel_name) & (hotels_df['address'] == hotel_address)].to_dict(orient='records')[0]
    comments_info = comments_df[(comments_df['hotel_name'] == hotel_name) & (comments_df['hotel_address'] == hotel_address)].to_dict(orient='records')

    return render_template('hotel_details.html', hotel=hotel_info, comments=comments_info)

@app.route('/logout')
def logout():
<<<<<<< Updated upstream
    session.pop('username', None)  # Elimina el usuario de la sesión
    session.pop('is_admin', None)   # Elimina el estado del admin
    return redirect(url_for('login'))  # Redirige al login

@app.route('/admin', methods=['GET'])
def admin():
    if not session.get('is_admin'):
        return "Access denied", 403  # Denegar acceso si no es admin

    # Obtener la lista de hoteles desde el DataFrame
    hotels_list = hotels_df.to_dict(orient='records')  # Convertir a lista de diccionarios

=======
    """
    Logs the user out by removing their session information.
    """
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET'])
def admin():
    """
    Displays the admin page with a list of hotels.
    Access is restricted to admin users.
    """
    if not session.get('is_admin'):
        return "Access denied", 403  # Deny access if not admin

    hotels_list = hotels_df.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
>>>>>>> Stashed changes
    return render_template('admin.html', hotels=hotels_list)

@app.route('/admin/add_hotel', methods=['GET', 'POST'])
def add_hotel():
<<<<<<< Updated upstream
=======
    """
    Allows the admin to add a new hotel to the list.
    Handles hotel name, address, description, and image uploads.
    """
>>>>>>> Stashed changes
    if not session.get('is_admin'):
        return "Access denied", 403

    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
<<<<<<< Updated upstream
        description = request.form['description']  # Recibiendo la descripción
=======
        description = request.form['description']  # Hotel description
>>>>>>> Stashed changes
        
        image_file = request.files.get('image')

        if image_file and allowed_file(image_file.filename):
            image_filename = secure_filename(image_file.filename)
<<<<<<< Updated upstream
            image_path = os.path.join("static/images/", image_filename)
=======
            image_path = os.path.join("src/Webapp/static/images/", image_filename)
>>>>>>> Stashed changes
            image_file.save(image_path)

            new_hotel_data = {
                "name": name,
                "address": address,
<<<<<<< Updated upstream
                "description": description,  # Guardar la descripción
                "image": image_filename,
                "rating": 0.0,
                "totalscore":0.0,
                "cantcomment":0
=======
                "description": description,  # Save description
                "image": image_filename,
                "rating": 0.0,
                "totalscore": 0.0,
                "cantcomment": 0
>>>>>>> Stashed changes
            }

            hotels_df.loc[len(hotels_df)] = new_hotel_data
            save_dataframes()

            return redirect(url_for('admin'))

    return render_template('add_hotel.html')

<<<<<<< Updated upstream

# Función para verificar extensiones permitidas para las imágenes
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

from werkzeug.utils import secure_filename

if __name__ == '__main__':
    # Cargar los DataFrames al inicio
    load_dataframes()

    app.run(debug=True)



#     <!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{{ hotel.name }}</title>
#     <link href="/static/styles.css" rel="stylesheet">
# </head>

# <body>
#     <div class="container">
#         <h2>{{ hotel.name }}</h2>
#         <p>Address: {{ hotel.address }}</p>
#         <img src="{{ url_for('static', filename='images/' + hotel.image) }}" alt="{{ hotel.name }}">
#         <h3>Rating: {{ hotel.rating }}</h3>

#         <h4>Comments:</h4>
#         <ul id="comments-list">
#             {% for comment in comments %}
#             <li>
#                 <strong>{{ comment.username }}</strong>
#                 <span>{{ comment.comment }}</span><br>
#                 <span>Sentiment: {{ comment.sentiment }} | Score: {{ comment.score }}</span>
#             </li>
#             {% endfor %}
#         </ul>

#         <h4>Add a Comment:</h4>
#         <form method="post">
#             <textarea name="comment" placeholder="Write your comment here..." required></textarea>
#             <input type="submit" value="Submit Comment">
#         </form>
#         <a href="{{ url_for('hotels') }}">Back to Hotels List</a>
#     </div>
# </body>

# </html>
=======
# Function to check allowed file extensions for images
def allowed_file(filename):
    """
    Checks if the uploaded file has an allowed image extension.
    
    Args:
        filename (str): The name of the uploaded file.
    
    Returns:
        bool: True if the file is allowed, False otherwise.
    """
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to automatically open the browser
def open_web_browser(is_open):
    """
    Opens the web browser to the local server address if not already opened.
    
    Args:
        is_open (bool): A flag to check if the browser has already been opened.
    """
    if not is_open:
        webbrowser.open_new("http://127.0.0.1:5000/")
        is_open = True

from werkzeug.utils import secure_filename

if __name__ == '__main__':
    # Load DataFrames at the start
    users_df, hotels_df, comments_df = load_dataframes()
    open_web_browser(is_open)
    app.run(debug=True)
>>>>>>> Stashed changes
