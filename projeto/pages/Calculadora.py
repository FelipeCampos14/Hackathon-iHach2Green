import streamlit as st

if 'card_counter' not in st.session_state:
    st.session_state['card_counter'] = 0

# Add logo to the sidebar
logo_path = "projeto/img/logo2.png"
st.sidebar.image(logo_path, width=280)


st.title("Hydro Capital")
def format_number(number):
    # Format the number with commas every three digits
    formatted_number = "{:,.2f}".format(number)
    return formatted_number

def calculate_hydrogen_production(electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer,
                                  annual_cost_electrolyzer, electrolyzer_efficiency, years):
    x=years
    # Calculate annual energy output
    annual_energy_output = electrolyzer_power * electrolyzer_efficiency * 24 * 365

    # Calculate annual hydrogen mass output
    annual_h2_mass_output = annual_energy_output / 33.6

    # Calculate annual transport cost
    annual_transport_cost = 15 * annual_h2_mass_output

    # Calculate initial investment
    initial_investment = initial_cost_solar + initial_cost_electrolyzer

    # Numerical integration using Trapezoidal Rule
    num_segments = 1000  # Number of segments for numerical integration
    delta_x = years / num_segments
    revenue = 0

    for i in range(num_segments):
        x1 = i * delta_x
        x2 = (i + 1) * delta_x
        y1 = 0.0066666666666667 * x1**2 - 0.36666666666667 * x1 + 8
        y2 = 0.0066666666666667 * x2**2 - 0.36666666666667 * x2 + 8
        revenue += (y1 + y2) / 2 * annual_h2_mass_output * delta_x

    # Calculate operational cost in x years
    operational_cost = years * (annual_cost_solar + annual_cost_electrolyzer)

    # Calculate profit in x years
    profit = revenue - operational_cost - initial_investment

    return {
        'year': x,
        'annual_energy_output': annual_energy_output,
        'annual_h2_mass_output': annual_h2_mass_output,
        'annual_transport_cost': annual_transport_cost,
        'initial_investment': initial_investment,
        'revenue': revenue,
        'operational_cost': operational_cost,
        'profit': profit

    }
st.header("Calculadora de Investimentos")
electrolyzer_power = st.number_input("Potência do Eletrolizador (Watts)", value=50000)
initial_cost_solar = st.number_input("Custo inicial usina energia sustentável (dólares)", value=200000000)
annual_cost_solar = st.number_input("Custo operacional usina energia sustentável (dólares por ano)", value=2000000)
initial_cost_electrolyzer = st.number_input("Custo inicial eletrolizador (dólares)", value=100000000)
annual_cost_electrolyzer = st.number_input("Custo operacional eletrolizador (dólares por ano)", value=1000000)
electrolyzer_efficiency = st.number_input("Eficiência do eletrolisador()", value=0.7)
max_years = st.number_input("Número de anos", value=10)
name = st.text_input("Nome do projeto")

# Calculate and display the profit graph
if st.button("Calcular"):
    if all(value is not None and value != '' for value in [electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer, annual_cost_electrolyzer, electrolyzer_efficiency, max_years, name]):
        years = list(range(1, int(max_years) + 1))
        results = [calculate_hydrogen_production(
            electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer,
            annual_cost_electrolyzer, electrolyzer_efficiency, year
        ) for year in years]
        annual_energy_output_formatted = [format_number(result['annual_energy_output']) for result in results]
        annual_h2_mass_output_formatted = [format_number(result['annual_h2_mass_output']) for result in results]
        annual_transport_cost_formatted = [format_number(result['annual_transport_cost']) for result in results]
        initial_investment_formatted = [format_number(result['initial_investment']) for result in results]
        revenue_formatted = [format_number(result['revenue']) for result in results]
        operational_cost_formatted = [format_number(result['operational_cost']) for result in results]
        profit_formatted = [format_number(result['profit']) for result in results]

        st.header("Resultados")
        st.write(f"Energia gerada e armazenada em H2V anualmente (kWh): {annual_energy_output_formatted[-1]}")
        st.write(f"Massa de H2 gerada anualmente (kg): {annual_h2_mass_output_formatted[-1]}")
        st.write(f"Custo anual de transporte (dólares): {annual_transport_cost_formatted[-1]}")
        st.write(f"Investimento inicial (dólares): {initial_investment_formatted[-1]}")
        st.write(f"Receita em {years[-1]} anos (dólares): {revenue_formatted[-1]}")
        st.write(f"Custo Operacional de {years[-1]} anos (dólares): {operational_cost_formatted[-1]}")
        st.write(f"Lucro em{years[-1]} anos (dólares): {profit_formatted[-1]}")

        # Create and display the profit vs. years graph
        profits = [result['profit'] for result in results if result['year'] > 0]
        st.line_chart(profits)
        st.caption("Investment over time")

    else: 
        st.warning("Preencha todos os campos")

if st.button("Adicionar a Investimento"):
    if all(value is not None and value != '' for value in [electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer, annual_cost_electrolyzer, electrolyzer_efficiency, max_years, name]):
        years = list(range(1, int(max_years) + 1))
        results = [calculate_hydrogen_production(
            electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer,
            annual_cost_electrolyzer, electrolyzer_efficiency, year
        ) for year in years]
        card_counter = st.session_state['card_counter']
        st.session_state[f'name{card_counter}'] = name
        st.session_state[f'time{card_counter}'] = max_years
        st.session_state[f'initial_investment{card_counter}'] = format_number(initial_cost_solar + initial_cost_electrolyzer)
        st.session_state[f'profits{card_counter}'] = [format_number(result['profit'])for result in results]

        st.session_state['card_counter'] +=1
        st.success('Enviado para Investimento', icon="✅")
    else: 
        st.warning("Preencha todos os campos")

st.markdown(
    """
    <style>
        /* Add your CSS styles specific to the Marketplace page */
        .st-bc{
            background-color: white;
            color: black;
        }
        .st-c0{
            background-color: white;
            color: black;
        }
        .css-76z9jo{
            background-color: white;
            color: black;
        }
        .step-down {
            background-color: white;
            color: white;
        }
        .step-up {
            background-color: white;
            color: white;
        }
        .marketplace-container {
            background-color: #d5ffd3;
            padding: 1rem;
            border-radius: 0.5rem;
            color: white;
            margin-bottom: 1rem;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .marketplace-container h3 {
            font-size: 25px;
            margin-top: 0;
            margin-bottom: 0.5rem;
        }
        .marketplace-container p {
            font-size: 15px;
            line-height: 0.9;
            margin-top: 0;
            margin-bottom: 0.5rem;
            color: black;
        }
        .marketplace-container button {
            border-radius: 0.5rem;
            border: 1px;
            color: white;
            background-color: #032305;
            margin: 1px;
            align-self: flex-end;
        }
        .marketplace-container button:hover {
            background-color: white;
            color: #032305;
            border: 1px solid #032305;
        }
        /* body*/
        .css-uf99v8{
            background: #fefdf4;
        }
        /* sidebar*/
        .css-1cypcdb{
            background-color:#032305;
        }
        /* Title n headers*/
        .css-10trblm{
            color: black;
        }
        /* body text*/
        .css-q8sbsg {
            color: black;
            font-size: 40px;
        }
        /* info*/
        .st-ae {
            background-color: #d5ffd3;
        }
        /* info text*/
        .css-nahz7x{
            color: black;
        }
        /* button*/
        .css-b3z5c9{
            color:white;
            background-color: #032305;
            border: #032305;
        }
        .css-b3z5c9:focus:not(:active){
            color:#032305;
            background-color: white;
            border:#032305;
        }
        .css-b3z5c9:hover{
            color:#032305;
            background-color: white;
            border:#032305;
        }
        .css-1y4p8pa{
            /* From https://css.glass */
            background: rgba(255, 255, 255, 0.3);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)
