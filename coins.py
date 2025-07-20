import requests
import json
import streamlit as st
url = "https://api.coingecko.com/api/v3/coins/markets"
# Parâmetros da requisição
params = {
    'vs_currency': 'usd',
    'ids': 'bitcoin,ethereum,solana,ripple,cardano',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False
}

# Fazendo a requisição 'Bitcoin é uma criptomoeda descentralizada e de código aberto, um dinheiro eletrônico para transações financeiras ponto a ponto'
response = requests.get(url, params=params)
bitcoin = response.json()
with open('bitcoins.json', 'w', encoding='utf-8') as arquivo:
    json.dump(bitcoin, arquivo, indent=4)

st.title('Veja 5 principais criptomoedas')
st.button('Veja')
st.header(f'{bitcoin[0]['name']}')
st.image(bitcoin[0]['image'])
st.markdown('Bitcoin é uma criptomoeda descentralizada e de código aberto, um dinheiro eletrônico para transações financeiras ponto a ponto')
st.write(f'Preço atual: US$ {bitcoin[0]['current_price']}')
st.write(f'Mudanças nas ultimas 24h: US$ {bitcoin[0]['price_change_24h']}')
st.write(f'Volume total: {bitcoin[0]['total_volume']}')
st.write(f'Moedas em circulação: {bitcoin[0]['circulating_supply']}')

st.header(f'{bitcoin[1]['name']}:')
st.image(bitcoin[1]['image'])
st.write ('Ethereum é uma plataforma descentralizada capaz de executar contratos inteligentes e aplicações descentralizadas usando a tecnologia blockchain.')
st.write(f'Preço atual: US$ {bitcoin[1]['current_price']}')
st.write(f'Mudanças nas ultimas 24h: US$ {bitcoin[1]['price_change_24h']}')
st.write(f'Volume total: {bitcoin[1]['total_volume']}')
st.write(f'Moedas em circulação: {bitcoin[1]['circulating_supply']:.2f}')

st.header(f'{bitcoin[2]['name']}:')
st.image(bitcoin[2]['image'])
st.write('XRP é um ativo digital nativo do XRP Ledger, uma tecnologia blockchain de código aberto, sem permissão e descentralizada.')
st.write(f'Preço atual: US$ {bitcoin[2]['current_price']}')
st.write(f'Mudanças nas ultimas 24h: US$ {bitcoin[2]['price_change_24h']:.2f}')
st.write(f'Volume total: {bitcoin[2]['total_volume']}')
st.write(f'Moedas em circulação: {bitcoin[2]['circulating_supply']:.2f}')

st.header(f'{bitcoin[3]['name']}:')
st.image(bitcoin[3]['image'])
st.write('Solana é uma plataforma de blockchain de alta performance projetada para oferecer velocidade e escalabilidade para aplicações descentralizadas e projetos de criptoativos.')
st.write(f'Preço atual: US$ {bitcoin[3]['current_price']}')
st.write(f'Mudanças nas ultimas 24h: US$ {bitcoin[3]['price_change_24h']}')
st.write(f'Volume total: {bitcoin[3]['total_volume']}')
st.write(f'Moedas em circulação: {bitcoin[3]['circulating_supply']:.2f}')

st.header(f'{bitcoin[4]['name']}:')
st.image(bitcoin[4]['image'])
st.write('Cardano é uma plataforma de computação distribuída que executa o blockchain para a criptomoeda ADA')
st.write(f'Preço atual: US$ {bitcoin[4]['current_price']:.2f}')
st.write(f'Mudanças nas ultimas 24h: US$ {bitcoin[4]['price_change_24h']:.2f}')
st.write(f'Volume total: {bitcoin[4]['total_volume']}')
st.write(f'Moedas em circulação: {bitcoin[4]['circulating_supply']:.2f}')