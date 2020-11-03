import openpyxl
from us_state_abbrev import us_state_abbrev
import plotly.graph_objects

def get_data_rows(filename):
    excel_file = openpyxl.load_workbook(filename)
    first_sheet = excel_file.active
    return first_sheet.rows

def display_data(state_list, unemploy_list):
    unemployment_map = plotly.graph_objects.Figure(
        data=plotly.graph_objects.Choropleth(
            locations=state_list,
            z=unemploy_list,
            locationmode="USA-states",
            colorscale='blues',
            colorbar_title="Unemployment"
        ))
    unemployment_map.update_layout(
        title_text= "Unemployment Rates in the US",
        geo_scope="usa")
    unemployment_map.show()

def main():
    unemployment_data = get_data_rows("lanrderr-unemployment.xlsx")
    state_abbreviations = []
    unemployment_rates = []
    for row in unemployment_data:
        state_name = row[0].value
        if state_name in us_state_abbrev:
            state_abbreviations.append(us_state_abbrev[state_name])
            unemployment_rate = row[1].value
            unemployment_rates.append(unemployment_rate)
    display_data(state_abbreviations, unemployment_rates)


main()