import investpy
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Dashboard de Ações Brasileiras",
    page_icon="chart_with_upwards_trend",
    #layout="wide",
    initial_sidebar_state="expanded",
)

#def exibir_pagina_inicial():
#    st.write('Página de Login')

def autenticar_usuario(nome, senha):    
    # Verifique se o nome de usuário e a senha correspondem a um usuário válido
    # Retorne True se a autenticação for bem-sucedida, ou False caso contrário
    if nome == "admin" and senha == "senha123":
        return True
    else:
        return False

def candlestick_with_line_chart(data):
    fig = go.Figure()

    # Gráfico de velas
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name='Candles'))

    # Gráfico de linhas
    fig.add_trace(go.Scatter(x=data.index,
                             y=data['Close'],
                             mode='lines',
                             name='Line Chart'))

    fig.update_layout(
        title='Gráfico de Velas com Linha',
        yaxis_title='Preço',
        xaxis_rangeslider_visible=False
    )

    return fig

# Sidebar # ========================================
def exibir_pagina_restrita():

    tickers = investpy.get_stocks_list(country='brazil')
    tickers = sorted(tickers)

    st.sidebar.title('Dashboard de ações brasileiras')
    st.sidebar.write(f'Olá, {st.session_state.textNome}')

    ticker = st.sidebar.selectbox('Selecione uma ação: ', tickers)

    ticker = ticker + ".SA"

    st.sidebar.write('Total de ações da B3: ', len(tickers))

    st.header(ticker)

    st.write('Você selecionou ', ticker)

    períodos = ['5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'max'] 

    periodo = st.sidebar.selectbox('Selecione o período: ', períodos)

    dados = yf.download(ticker, period=periodo)

    st.title('Gráfico de Velas com Linha')
    fig = candlestick_with_line_chart(dados)
    st.plotly_chart(fig)

    # Aqui você pode exibir a página restrita acessível somente após a autenticação

    if st.sidebar.button("Logout"):
        st.session_state.autenticado = False
        
# Main # =========================================    
    st.header(ticker)
    
# Fim do código da aplicação #===============================================

def main():
    # Inicializa o estado de autenticação como False (não autenticado)
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    # Se estiver autenticado, exibe a página restrita
    if st.session_state.autenticado:
        exibir_pagina_restrita()
    else:
        # Se não estiver autenticado, exibe a página de login
        nome = st.text_input("Nome de Usuário", key="textNome")
        senha = st.text_input("Senha", type="password")

        if st.button("Login"):
            # Verifica a autenticação do usuário
            if autenticar_usuario(nome, senha):
                st.session_state.autenticado = True
            else:
                st.error("Falha na autenticação. Tente novamente.")

    # Exibe a página inicial se não estiver autenticado
    #if not st.session_state.autenticado:
    #    exibir_pagina_inicial()

if __name__ == "__main__":
    main()