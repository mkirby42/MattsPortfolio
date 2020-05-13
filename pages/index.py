import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

mars_content = [
    dbc.CardHeader("Web App"),
    dbc.CardImg(src = "/assets/missle_row.jpg", top = True),
    dbc.CardBody([
        html.H5("Getting To Mars", className = "card-title"),
        html.P(
            "Optimizing an interplanetary trajectory",
            className = "card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href='http://ec2-18-189-7-104.us-east-2.compute.amazonaws.com',
            style = dict(color = 'white')
        ), color = "primary")
    ])]

resume_content = [
    dbc.CardHeader("File Download"),
    dbc.CardImg(src = "assets/resume.jpg", top = True),
    dbc.CardBody([
        html.H5("Resume", className = "card-title"),
        html.P(
            "Download Matt's resume as a PDF file",
            className = "card-text",
        ),
        dbc.Button(html.A(
        'Download',
        download = 'Matts Resume.pdf', href='/assets/matts resume.pdf',
        style = dict(color = 'white')
        ), color = "primary")
    ])]

congress_content = [
    dbc.CardHeader("Blog Post"),
    dbc.CardImg(src = "assets/washington.jpg", top = True),
    dbc.CardBody([
        html.H5("Fiscal Policy", className = "card-title"),
        html.P(
            "Exploring 50 years of federal fiscal policy",
            className = "card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href = """
            https://medium.com/@matt42kirby/tracking-congressional-revenue-and-
            spending-from-nixon-to-trump-4586ca720bf7?source=friends_
            link&sk=e34b53d86bc4d3f6f09eaeb39002391a
            """,
            style = dict(color = 'white')
        ), color = "primary")
    ])]

mushroom_content = [
    dbc.CardHeader("Web App"),
    dbc.CardImg(src = "/assets/mushroom.jpg", top = True),
    dbc.CardBody([
        html.H5("Classifing Mushrooms", className = "card-title"),
        html.P(
            "Using tree-based models to classify mushrooms as edible or poisonious",
            className = "card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href='https://mushroom-dash-app.herokuapp.com/',
            style = dict(color = 'white')
        ), color = "primary")
    ])]

tanzania_content = [
    dbc.CardHeader("Blog Post"),
    dbc.CardImg(src = "assets/tanzania.jpg", top = True),
    dbc.CardBody([
        html.H5("Tanzanian Water Pumps", className = "card-title"),
        html.P(
            "Utilizing machine learning for pedictive maintenance",
            className = "card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href = """
            https://medium.com/analytics-vidhya/predictive-modeling-for-
            tanzanian-water-pumps-701bcc7760b2?source=friends_
            link&sk=90b471fe246badc2a32046ec763ecf90
            """,
            style = dict(color = 'white')
        ), color = "primary")
    ])]

nlp_content = [
    dbc.CardHeader("Blog Post"),
    dbc.CardImg(src = "assets/nlp.jpg", top = True),
    dbc.CardBody([
        html.H5("Natural Language Processing with Python", className = "card-title"),
        html.P(
            "Demonstrating NLP techniques with Python",
            className = "card-text",
        ),
        dbc.Button(html.A(
            "See More",
            href = """
            https://medium.com/analytics-vidhya/natural
            -language-processing-with-python-cb3f83d5a393?source=friends_
            link&sk=4cbf63c34f97ca048755d172fab7ed9f
            """,
            style = dict(color = 'white')
        ), color = "primary")
    ])]


row_1 = dbc.Row([
    dbc.Col([
        dbc.Card(
            mars_content,
            color = "light",
            style = {"width": "18rem", "height": "28rem"},
        )
    ]),
    dbc.Col([
        dbc.Card(
            resume_content,
            color = "light",
            style = {"width": "18rem", "height": "28rem"},
        ),
    ]),
    dbc.Col([
        dbc.Card(
            mushroom_content,
            color = "light",
            style = {"width": "18rem", "height": "28rem"},
        )
    ]),
], className="mb-4")

row_2 = dbc.Row([
    dbc.Col([
        dbc.Card(
            nlp_content,
            color = "light",
            style = {"width": "18rem", "height": "28rem"},
        )
    ]),
    dbc.Col([
        dbc.Card(
            tanzania_content,
            color = "light",
            style = {"width": "18rem", "height": "28rem"},
        ),
    ]),
    dbc.Col([
        dbc.Card(
            congress_content,
            color = "light",
            style = {"width": "18rem", "height": "28rem"},
        )
    ]),
], className="mb-4")

layout = [html.Div([row_1, row_2])]
