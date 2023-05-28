"""
LIDANDO COM VARIÁVEIS GLOBAIS
"""

from dash import Dash, html, dcc, Input, Output
import pandas as pd
from numpy.random import randint

n = 40
df = pd.DataFrame({
    'student_id': range(1, n+1),
    'score': randint(low=0, high=11, size=n)
})

app = Dash(__name__)

app.layout = html.Div([

    'Em uma turma de {} alunos'.format(n),

    dcc.Slider(
        id='score-slider',
        min=0,
        max=10,
        value=7,
        marks={str(i): str(i) for i in range(0,11)},
        step=1
    ),

    html.Div(id='qtd-aluno'),

    dcc.Store(id='stored-data'),
    html.Div(id='stored-qtd-aluno')
])

@app.callback(
    Output(component_id='qtd-aluno', component_property='children'),
    Input(component_id='score-slider', component_property='value')
)
def update_output(value):
    
    global df
    """
    NUNCA. NUNCA manipule ou atribua novos valores a uma varGlobal
    crie uma varAuxiliar e continue com sua vida!
    """
    filtered_df = df[df['score'] >= value]
    return '[NO_CACHE] Quantidade de alunos com nota igual ou superior a {}: {}'.format(value, len(filtered_df))



"""
O atributo Store pode ser usado para armazenar interações
e filtros que cada usuário aplica sem afetar a app para os outros.

Store pega o que o usuário fez com uma variável e armazena na cache do browser.
"""
@app.callback(
    Output(component_id='stored-data', component_property='data'),
    Input(component_id='score-slider', component_property='value')
)
def update_stored_data(value):
    
    global df
    """
    NUNCA. NUNCA manipule ou atribua novos valores a uma varGlobal
    crie uma varAuxiliar e continue com sua vida!
    """
    filtered_df = df[df['score'] >= value]
    # return 'Quantidade de alunos com nota igual ou superior a {}: {}'.format(value, len(filtered_df))
    return filtered_df.to_dict()

@app.callback(
    Output(component_id='stored-qtd-aluno', component_property='children'),
    Input(component_id='stored-data', component_property='data')
)
def update_stored_output(data):
    filtered_df = pd.DataFrame(data)

    return '[CACHED] Quantidade de alunos com nota igual ou superior a {}: {}'.format(min(filtered_df['score']), len(filtered_df))

if __name__ == '__main__':
    app.run_server(debug=True)