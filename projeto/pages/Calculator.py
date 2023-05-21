import streamlit as st
def format_number(number):
    # Format the number with commas every three digits
    formatted_number = "{:,.2f}".format(number)
    return formatted_number

def calculate_hydrogen_production(electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer,
                                  annual_cost_electrolyzer, electrolyzer_efficiency, hydrogen_price, years):
    # Calculate annual energy output
    annual_energy_output = electrolyzer_power * electrolyzer_efficiency * 24 * 365

    # Calculate annual hydrogen mass output
    annual_h2_mass_output = annual_energy_output / 33.6

    # Calculate annual transport cost
    annual_transport_cost = 0.1 * annual_h2_mass_output

    # Calculate initial investment
    initial_investment = initial_cost_solar + initial_cost_electrolyzer

    # Calculate revenue in x years
    revenue = years * annual_h2_mass_output * hydrogen_price

    # Calculate operational cost in x years
    operational_cost = years * (annual_cost_solar + annual_cost_electrolyzer)

    # Calculate profit in x years
    profit = revenue - operational_cost - initial_investment

    return {
        'annual_energy_output': annual_energy_output,
        'annual_h2_mass_output': annual_h2_mass_output,
        'annual_transport_cost': annual_transport_cost,
        'initial_investment': initial_investment,
        'revenue': revenue,
        'operational_cost': operational_cost,
        'profit': profit
    }
st.write("This is the ROI page. Here, you can calculate the profit.")

electrolyzer_power = st.number_input("Electrolyzer Power (Watts)", value=1000)
initial_cost_solar = st.number_input("Initial Cost of Solar Plant (dollars)", value=1000000)
annual_cost_solar = st.number_input("Annual Operational Cost of Solar Plant (dollars)", value=5000)
initial_cost_electrolyzer = st.number_input("Initial Cost of Electrolyzer (dollars)", value=500000)
annual_cost_electrolyzer = st.number_input("Annual Operational Cost of Electrolyzer (dollars)", value=10000)
electrolyzer_efficiency = st.number_input("Efficiency of the Electrolyzer", value=0.7)
hydrogen_price = st.number_input("Current Green Hydrogen Price (dollars)", value=2.5)
max_years = st.number_input("Maximum Number of Years", value=10)

# Calculate and display the profit graph
if st.button("Calculate"):
    years = list(range(1, int(max_years) + 1))
    results = [calculate_hydrogen_production(
        electrolyzer_power, initial_cost_solar, annual_cost_solar, initial_cost_electrolyzer,
        annual_cost_electrolyzer, electrolyzer_efficiency, hydrogen_price, year
    ) for year in years]

    # Create and display the profit vs. years graph
    profits = [result['profit'] for result in results]
    st.line_chart(profits)

    # Find the year when profit reaches 0
    zero_profit_year = next((year for year, result in zip(years, results) if result['profit'] <= 0), None)
    if zero_profit_year:
        st.write(f"The profit reaches 0 at year {zero_profit_year}")