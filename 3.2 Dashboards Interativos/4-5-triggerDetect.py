"""
DETECÇÃO DE TRIGGERS EM CALLBACKS
"""

from dash import Dash, html, dcc, Input, Output, callback_context

app = Dash(__name__)

app.layout = html.Div([
    html.Button(children='Button 1', id='b1'),
    html.Button(children='Button 2', id='b2'),
    html.Button(children='Button 3', id='b3'),

    html.Div(id='container-ctx-example')
])

@app.callback(
    Output(component_id='container-ctx-example', component_property='children'),
    Input(component_id='b1', component_property='n_clicks'),
    Input(component_id='b2', component_property='n_clicks'),
    Input(component_id='b3', component_property='n_clicks')
)
# def display(btn1, btn2, btn3):
#     import pdb
#     pdb.set_trace()

#     return ''
def display(btn1, btn2, btn3):
    trig_id = callback_context.triggered[0]['prop_id'].split('.')[0]

    if trig_id == 'b1':
        # Operações que você quiser com base em qual trig ativou o callback
        pass

    return trig_id

if __name__ == '__main__':
    app.run_server(debug=True)