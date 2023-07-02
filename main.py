import streamlit as st

#def exibir_pagina_inicial():
#    st.write('Página de Login')

def autenticar_usuario(username, password):    
    # Verifique se o nome de usuário e a senha correspondem a um usuário válido
    # Retorne True se a autenticação for bem-sucedida, ou False caso contrário
    if username == "admin" and password == "senha123":
        return True
    else:
        return False

# Código da aplicação #=======================================================

def exibir_pagina_restrita():
    # Aqui você pode exibir a página restrita acessível somente após a autenticação
    st.sidebar.title('Sidebar')
    if st.sidebar.button("Logout"):
        st.session_state.autenticado = False
    st.title('Main')
    
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
        username = st.text_input("Nome de Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Login"):
            # Verifica a autenticação do usuário
            if autenticar_usuario(username, password):
                st.session_state.autenticado = True
            else:
                st.error("Falha na autenticação. Tente novamente.")

    # Exibe a página inicial se não estiver autenticado
    #if not st.session_state.autenticado:
    #    exibir_pagina_inicial()

if __name__ == "__main__":
    main()
