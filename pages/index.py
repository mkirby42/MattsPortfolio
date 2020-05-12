import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

mars_content = [
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
    dbc.CardImg(src = "/assets/washington.jpeg", top = True),
    dbc.CardBody([
        html.H5("Fiscal Policy", className = "card-title"),
        html.P(
            "Exploring 50 years of federal fiscal policy",
            className = "card-text",
        ),
        dbc.Button("See More", color = "primary"),
    ])]

mushroom_content = [
    dbc.CardBody([
        html.H5("Classifing Mushrooms", className = "card-title"),
        html.P(
            "Using tree-based models to classify mushrooms as edible or poisonious",
            className = "card-text",
        ),
        dbc.Button("See More", color = "primary"),
    ]),
    dbc.CardImg(src = "/assets/mushroom.jpg", bottom = True)]



column1 = html.Div([dbc.Row([
    dbc.Col([
        dbc.Card(
            mars_content,
            color = "light",
            style = {"width": "18rem"},
        )
    ]),
    dbc.Col([
        dbc.Card(
            resume_content,
            color = "light",
            style = {"width": "18rem"},
        ),
    ]),
    dbc.Col([
        dbc.Card(
            mushroom_content,
            color = "light",
            style = {"width": "18rem"},
        )
    ]),
    #dbc.Col([
        #dbc.Card(
            #congress_content,
            #color = "light",
            #style = {"width": "18rem"},
        #)
    #])
])])

column2 = html.Div([dbc.Row([
    dbc.Col([
        dbc.Card(
            mars_content,
            color = "light",
            style = {"width": "18rem"},
        )
    ]),
    dbc.Col([
        dbc.Card(
            resume_content,
            color = "light",
            style = {"width": "18rem"},
        ),
    ]),
    dbc.Col([
        dbc.Card(
            mushroom_content,
            color = "light",
            style = {"width": "18rem"},
        )
    ]),
    #dbc.Col([
        #dbc.Card(
            #congress_content,
            #color = "light",
            #style = {"width": "18rem"},
        #)
    #])
])])

layout = [dbc.Row([column1]), dbc.Row([column2])]
