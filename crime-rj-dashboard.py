import dash
from dash import dcc, Dash, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json

df = pd.read_csv("crimesRJ.csv",delimiter=";", encoding='latin')
rj = json.load(open("rj.json",'r'))

df_anual = df.groupby(['ano', 'fmun', 'fmun_cod']).sum().reset_index()

options1 = [
    {'label': 'Homicídio doloso', 'value': 'hom_doloso'},
    {'label': 'Lesão corporal seguida de morte', 'value': 'lesao_corp_morte'},
    {'label': 'Latrocínio', 'value': 'latrocinio'},
    {'label': 'CVLI', 'value': 'cvli'},
    {'label': 'Homicídio por intervenção policial', 'value': 'hom_por_interv_policial'},
    {'label': 'Letalidade violenta', 'value': 'letalidade_violenta'},
    {'label': 'Tentativa de homicídio', 'value': 'tentat_hom'},
    {'label': 'Lesão corporal dolosa', 'value': 'lesao_corp_dolosa'},
    {'label': 'Estupro', 'value': 'estupro'},
    {'label': 'Homicídio culposo', 'value': 'hom_culposo'},
    {'label': 'Lesão corporal culposa', 'value': 'lesao_corp_culposa'},
    {'label': 'Roubo a transeunte', 'value': 'roubo_transeunte'},
    {'label': 'Roubo de celular', 'value': 'roubo_celular'},
    {'label': 'Roubo em coletivo', 'value': 'roubo_em_coletivo'},
    {'label': 'Roubo de rua', 'value': 'roubo_rua'},
    {'label': 'Roubo de veículo', 'value': 'roubo_veiculo'},
    {'label': 'Roubo de carga', 'value': 'roubo_carga'},
    {'label': 'Roubo em comércio', 'value': 'roubo_comercio'},
    {'label': 'Roubo em residência', 'value': 'roubo_residencia'},
    {'label': 'Roubo a banco', 'value': 'roubo_banco'},
    {'label': 'Roubo de caixa eletrônico', 'value': 'roubo_cx_eletronico'},
    {'label': 'Roubo após saque', 'value': 'roubo_apos_saque'},
    {'label': 'Roubo de bicicleta', 'value': 'roubo_bicicleta'},
    {'label': 'Outros roubos', 'value': 'outros_roubos'},
    {'label': 'Total de roubos', 'value': 'total_roubos'},
    {'label': 'Furto de veículos', 'value': 'furto_veiculos'},
    {'label': 'Furto a transeunte', 'value': 'furto_transeunte'},
    {'label': 'Furto em coletivo', 'value': 'furto_coletivo'},
    {'label': 'Furto de celular', 'value': 'furto_celular'},
    {'label': 'Furto de bicicleta', 'value': 'furto_bicicleta'},
    {'label': 'Outros furtos', 'value': 'outros_furtos'},
    {'label': 'Total de furtos', 'value': 'total_furtos'},
    {'label': 'Sequestro', 'value': 'sequestro'},
    {'label': 'Extorsão', 'value': 'extorsao'},
    {'label': 'Sequestro relâmpago', 'value': 'sequestro_relampago'},
    {'label': 'Estelionato', 'value': 'estelionato'},
    {'label': 'Apreensão de drogas', 'value': 'apreensao_drogas'},
    {'label': 'Posse de drogas', 'value': 'posse_drogas'},
    {'label': 'Tráfico de drogas', 'value': 'trafico_drogas'},
    {'label': 'Apreensão de drogas sem autor', 'value': 'apreensao_drogas_sem_autor'},
    {'label': 'Recuperação de veículos', 'value': 'recuperacao_veiculos'},
    {'label': 'Auto de prisão em flagrante', 'value': 'apf'},
    {'label': 'Auto de apreensão de adolescente por ato infracional', 'value': 'aaapai'},
    {'label': 'Cumprimento de mandado de busca e apreensão', 'value': 'cmp'},
    {'label': 'Cumprimento de mandado de busca e apreensão (busca e apreensão)', 'value': 'cmba'},
    {'label': 'Ameaça', 'value': 'ameaca'},
    {'label': 'Pessoas desaparecidas', 'value': 'pessoas_desaparecidas'},
    {'label': 'Encontro de cadáver', 'value': 'encontro_cadaver'},
    {'label': 'Encontro de ossada', 'value': 'encontro_ossada'},
    {'label': 'Policiais militares mortos em serviço', 'value': 'pol_militares_mortos_serv'},
    {'label': 'Policiais civis mortos em serviço', 'value': 'pol_civis_mortos_serv'},
    {'label': 'Registro de ocorrências', 'value': 'registro_ocorrencias'},
    {'label': 'Fase', 'value': 'fase'}
]

options2 = [
    {'label': 'Angra dos Reis', 'value': 'Angra dos Reis'},
    {'label': 'Aperibé', 'value': 'Aperibé'},
    {'label': 'Araruama', 'value': 'Araruama'},
    {'label': 'Areal', 'value': 'Areal'},
    {'label': 'Armação dos Búzios', 'value': 'Armação dos Búzios'},
    {'label': 'Arraial do Cabo', 'value': 'Arraial do Cabo'},
    {'label': 'Barra do Piraí', 'value': 'Barra do Piraí'},
    {'label': 'Barra Mansa', 'value': 'Barra Mansa'},
    {'label': 'Belford Roxo', 'value': 'Belford Roxo'},
    {'label': 'Bom Jardim', 'value': 'Bom Jardim'},
    {'label': 'Bom Jesus do Itabapoana', 'value': 'Bom Jesus do Itabapoana'},
    {'label': 'Cabo Frio', 'value': 'Cabo Frio'},
    {'label': 'Cachoeiras de Macacu', 'value': 'Cachoeiras de Macacu'},
    {'label': 'Cambuci', 'value': 'Cambuci'},
    {'label': 'Carapebus', 'value': 'Carapebus'},
    {'label': 'Comendador Levy Gasparian', 'value': 'Comendador Levy Gasparian'},
    {'label': 'Campos dos Goytacazes', 'value': 'Campos dos Goytacazes'},
    {'label': 'Cantagalo', 'value': 'Cantagalo'},
    {'label': 'Cardoso Moreira', 'value': 'Cardoso Moreira'},
    {'label': 'Carmo', 'value': 'Carmo'},
    {'label': 'Casimiro de Abreu', 'value': 'Casimiro de Abreu'},
    {'label': 'Conceição de Macabu', 'value': 'Conceição de Macabu'},
    {'label': 'Cordeiro', 'value': 'Cordeiro'},
    {'label': 'Duas Barras', 'value': 'Duas Barras'},
    {'label': 'Duque de Caxias', 'value': 'Duque de Caxias'},
    {'label': 'Engenheiro Paulo de Frontin', 'value': 'Engenheiro Paulo de Frontin'},
    {'label': 'Guapimirim', 'value': 'Guapimirim'},
    {'label': 'Iguaba Grande', 'value': 'Iguaba Grande'},
    {'label': 'Itaboraí', 'value': 'Itaboraí'},
    {'label': 'Itaguaí', 'value': 'Itaguaí'},
    {'label': 'Italva', 'value': 'Italva'},
    {'label': 'Itaocara', 'value': 'Itaocara'},
    {'label': 'Itaperuna', 'value': 'Itaperuna'},
    {'label': 'Itatiaia', 'value': 'Itatiaia'},
    {'label': 'Japeri', 'value': 'Japeri'},
    {'label': 'Laje do Muriaé', 'value': 'Laje do Muriaé'},
    {'label': 'Macaé', 'value': 'Macaé'},
    {'label': 'Macuco', 'value': 'Macuco'},
    {'label': 'Magé', 'value': 'Magé'},
    {'label': 'Mangaratiba', 'value': 'Mangaratiba'},
    {'label': 'Maricá', 'value': 'Maricá'},
    {'label': 'Mendes', 'value': 'Mendes'},
    {'label': 'Mesquita', 'value': 'Mesquita'},
    {'label': 'Miguel Pereira', 'value': 'Miguel Pereira'},
    {'label': 'Miracema', 'value': 'Miracema'},
    {'label': 'Natividade', 'value': 'Natividade'},
    {'label': 'Nilópolis', 'value': 'Nilópolis'},
    {'label': 'Niterói', 'value': 'Niterói'},
    {'label': 'Nova Friburgo', 'value': 'Nova Friburgo'},
    {'label': 'Nova Iguaçu', 'value': 'Nova Iguaçu'},
    {'label': 'Paracambi', 'value': 'Paracambi'},
    {'label': 'Paraíba do Sul', 'value': 'Paraíba do Sul'},
    {'label': 'Paraty', 'value': 'Paraty'},
    {'label': 'Paty do Alferes', 'value': 'Paty do Alferes'},
    {'label': 'Petrópolis', 'value': 'Petrópolis'},
    {'label': 'Pinheiral', 'value': 'Pinheiral'},
    {'label': 'Piraí', 'value': 'Piraí'},
    {'label': 'Porciúncula', 'value': 'Porciúncula'},
    {'label': 'Porto Real', 'value': 'Porto Real'},
    {'label': 'Quatis', 'value': 'Quatis'},
    {'label': 'Queimados', 'value': 'Queimados'},
    {'label': 'Quissamã', 'value': 'Quissamã'},
    {'label': 'Resende', 'value': 'Resende'},
    {'label': 'Rio Bonito', 'value': 'Rio Bonito'},
    {'label': 'Rio Claro', 'value': 'Rio Claro'},
    {'label': 'Rio das Flores', 'value': 'Rio das Flores'},
    {'label': 'Rio das Ostras', 'value': 'Rio das Ostras'},
    {'label': 'Rio de Janeiro', 'value': 'Rio de Janeiro'},
    {'label': 'Santa Maria Madalena', 'value': 'Santa Maria Madalena'},
    {'label': 'Santo Antônio de Pádua', 'value': 'Santo Antônio de Pádua'},
    {'label': 'São Francisco de Itabapoana', 'value': 'São Francisco de Itabapoana'},
    {'label': 'São Fidélis', 'value': 'São Fidélis'},
    {'label': 'São Gonçalo', 'value': 'São Gonçalo'},
    {'label': 'São João da Barra', 'value': 'São João da Barra'},
    {'label': 'São João de Meriti', 'value': 'São João de Meriti'},
    {'label': 'São José de Ubá', 'value': 'São José de Ubá'},
    {'label': 'São José do Vale do Rio Preto', 'value': 'São José do Vale do Rio Preto'},
    {'label': 'São Pedro da Aldeia', 'value': 'São Pedro da Aldeia'},
    {'label': 'São Sebastião do Alto', 'value': 'São Sebastião do Alto'},
    {'label': 'Sapucaia', 'value': 'Sapucaia'},
    {'label': 'Saquarema', 'value': 'Saquarema'},
    {'label': 'Seropédica', 'value': 'Seropédica'},
    {'label': 'Silva Jardim', 'value': 'Silva Jardim'},
    {'label': 'Sumidouro', 'value': 'Sumidouro'},
    {'label': 'Tanguá', 'value': 'Tanguá'},
    {'label': 'Teresópolis', 'value': 'Teresópolis'},
    {'label': 'Trajano de Moraes', 'value': 'Trajano de Moraes'},
    {'label': 'Três Rios', 'value': 'Três Rios'},
    {'label': 'Valença', 'value': 'Valença'},
    {'label': 'Varre-Sai', 'value': 'Varre-Sai'},
    {'label': 'Vassouras', 'value': 'Vassouras'},
    {'label': 'Volta Redonda', 'value': 'Volta Redonda'}
]

options3 = [
    {'label': 'Criminalidade Anual das Cidades', 'value': 'opcao1'},
    {'label': 'As 10 Cidades Mais Criminosas', 'value': 'opcao2'}
]

# Lista dos crimes
crimes = [
    'hom_doloso', 'lesao_corp_morte', 'latrocinio', 'cvli',
       'hom_por_interv_policial', 'letalidade_violenta', 'tentat_hom',
       'lesao_corp_dolosa', 'estupro', 'hom_culposo', 'lesao_corp_culposa',
       'roubo_transeunte', 'roubo_celular', 'roubo_em_coletivo', 'roubo_rua',
       'roubo_veiculo', 'roubo_carga', 'roubo_comercio', 'roubo_residencia',
       'roubo_banco', 'roubo_cx_eletronico', 'roubo_conducao_saque',
       'roubo_apos_saque', 'roubo_bicicleta', 'outros_roubos', 'total_roubos',
       'furto_veiculos', 'furto_transeunte', 'furto_coletivo', 'furto_celular',
       'furto_bicicleta', 'outros_furtos', 'total_furtos', 'sequestro',
       'extorsao', 'sequestro_relampago', 'estelionato', 'apreensao_drogas',
       'posse_drogas', 'trafico_drogas', 'apreensao_drogas_sem_autor',
       'recuperacao_veiculos', 'apf', 'aaapai', 'cmp', 'cmba', 'ameaca',
       'pessoas_desaparecidas', 'encontro_cadaver', 'encontro_ossada',
       'pol_militares_mortos_serv', 'pol_civis_mortos_serv'
]

top_cidades_por_crime = pd.DataFrame(columns=['Crime', 'Cidade', 'Total de Ocorrências'])

for crime in crimes:
    top_cidades = df.groupby('fmun')[crime].sum().nlargest(10).reset_index()
    top_cidades.columns = ['Cidade', 'Total de Ocorrências']

    top_cidades['Crime'] = crime
    top_cidades_por_crime = pd.concat([top_cidades_por_crime, top_cidades], ignore_index=True)

top_cidades_por_crime['Total de Ocorrências'] = top_cidades_por_crime['Total de Ocorrências'].astype('int64')

custom_color_scale = [
    (0.0, 'white'),
    (0.01, '#F2F2F2'),
    (0.015, '#D7D8D9'),
    (0.025, '#BABCBF'),
    (0.05, '#D99CA7'),
    (0.1, '#FF293B'),
    (0.2, '#7F151D'),
    (1, '#400A0F')
]

def mapa(year,crime):

    fig2 = px.choropleth_mapbox(

                                df_anual.query("ano==@year"),
                                geojson=rj,
                                color=crime,
                                locations="fmun_cod",
                                featureidkey="properties.id",
                                mapbox_style="carto-darkmatter",
                                color_continuous_scale=custom_color_scale,
                                opacity=0.5,
                                center={"lat": -21.9068,
                                        "lon": -42.95},
                                zoom = 6.5,
                                hover_data = {"fmun": True,
                                               crime:True,
                                              "fmun_cod":False,
                                              "ano":False},
                                animation_frame="ano",
                                animation_group="fmun_cod"

                                )

    fig2.update_layout(

        paper_bgcolor = "#242424",
        autosize=True,
        showlegend = False,
        mapbox_pitch = 45,
        mapbox_bearing = 10

)


    return fig2

cores_grafico = {
    "borda": "#797D7F",
    "fundo":"#797D7F",
    "texto": "white"
    }

def barras(cidade, crime):
    fig1 = px.bar(df_anual.query("fmun == @cidade"),
                  x="ano",
                  y=crime,
                  color=crime,
                  color_continuous_scale=custom_color_scale,
                  template="plotly_dark")

    fig1.update_layout(
    title = f"Evolução da Criminalidade em {cidade}",
    xaxis_title = "Ano",
    yaxis_title = "Número de Ocorrências",
    legend_title = "Tipo de Crime",
    template="plotly_dark",
    plot_bgcolor=cores_grafico["fundo"],
    paper_bgcolor=cores_grafico["borda"],
    font_color=cores_grafico["texto"],
    margin = dict(l=0,r=0,t=35,b=10)
    )

    fig1.update_xaxes(showgrid=False, dtick=1)
    fig1.update_yaxes(showgrid=False)
    return fig1

def barras2(crime):
    # Filtrar o DataFrame para um crime específico
    crime_especifico = crime
    dados_crime_especifico = top_cidades_por_crime[top_cidades_por_crime['Crime'] == crime_especifico]

    # Criar o gráfico de barras agrupadas
    fig3 = px.bar(
                  dados_crime_especifico,
                  x='Cidade',
                  y='Total de Ocorrências',
                  color='Total de Ocorrências',
                  color_continuous_scale=custom_color_scale,
                  log_y=True
                  )

    fig3.update_layout(
      title=f'Top 10 Cidades para o Crime: {crime_especifico}',
      xaxis_title = "Cidade",
      yaxis_title = "Número de Ocorrências",
      legend_title = "Tipo de Crime",
      template="plotly_dark",
      plot_bgcolor=cores_grafico["fundo"],
      paper_bgcolor=cores_grafico["borda"],
      font_color=cores_grafico["texto"],
      margin = dict(l=0,r=0,t=35,b=10)
    )

    fig3.update_xaxes(showgrid=False)
    fig3.update_yaxes(showgrid=False)
    return fig3

# -------- Aplicativo -----------


app = Dash(__name__, external_stylesheets = [dbc.themes.CYBORG])
server = app.server

# -------- Layout -----------

app.layout = dbc.Container([

    dbc.Row([

        dbc.Col([

            html.H4("Evolução criminal"),
            html.P("Selecione o Gráfico,a Cidade, o Crime e o Ano"),
            html.P(""),
            dcc.RadioItems(id='opções3',
                            options = options3,
                            value = "opcao1",
                            style={"margin-top":"10px"}),
            dcc.Dropdown(id='opções2',
                         options = options2,
                         value = "Angra dos Reis",
                         style={"margin-top":"10px"}),
            html.P(""),
            dcc.Dropdown(id='opções1',
                         options = options1,
                         value = "hom_doloso",
                         style={"margin-top":"10px"}),
            html.P(""),

            dcc.Graph(id='Gráfico1', figure=barras(cidade="Angra dos Reis", crime="hom_doloso")),

        ],md=5, className="mx-Auto"),



        dbc.Col([


            dcc.Graph(id="Gráfico2", figure=mapa(year=2014, crime="hom_doloso"),
                       style={"height": "100vh", "margin-right": "10px"}),
            dcc.Slider(
                id='year-slider',
                min=2014,
                max=2023,
                step=1,
                value=2014,
                marks={str(year): str(year) for year in range(2014, 2023, 1)}
            )

        ], md=7, className="mx-Auto"),



    ]),




], fluid=True)


# -------- Funções -----------


@app.callback(
    [Output('Gráfico1', 'figure'),
     Output('Gráfico2', 'figure')],
    Input('opções3', 'value'),
    Input('opções2', 'value'),
    Input('opções1', 'value'),
    Input('year-slider', 'value')
)
def update_graphs(opcao, cidade, crime, year):
    if opcao == "opcao1":
        fig1 = barras(cidade, crime)
        fig2 = mapa(year, crime)
    elif opcao == "opcao2":
        fig1 = barras2(crime)
        fig2 = mapa(year, crime)
    return fig1, fig2

# -------- Iniciar App -----------

if __name__ == "__main__":
  app.run_server()