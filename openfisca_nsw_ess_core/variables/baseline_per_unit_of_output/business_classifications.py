# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class BusinessClassification(Enum):
    Division_A = 'Business classification is Agriculture, Forestry and Fishing.'
    Division_B = 'Business classification is Mining.'
    Division_C = 'Business classification is Manufacturing.'
    Division_D = 'Business classification is Electricity, Gas, Water and Waste' \
                 ' Services.'
    Division_E = 'Business classification is Construction.'
    Division_F = 'Business classification is Wholesale Trade.'
    Division_G = 'Business classification is Retail Trade.'
    Division_H = 'Business classification is Accomodation and Food Services.'
    Division_I = 'Business classification is Transport, Postal and Warehousing.'
    Division_J = 'Business classification is Information Media and Telecommunications.'
    Division_K = 'Business classification is Financial and Insurance Services.'
    Division_L = 'Business classification is Rental, Hiring and Real Estate Services.'
    Division_M = 'Business classification is Professional, Scientific and Technical' \
                 ' Services.'
    Division_N = 'Business classification is Administrative and Support Services.'
    Division_O = 'Business classification is Public Administration and Safety.'
    Division_P = 'Business classification is Education and Training.'
    Division_Q = 'Business classification is Health Care and Social Assistance.'
    Division_R = 'Business classification is Arts and Recreation Services.'
    Division_S = 'Business classification is Other Services.'
    Residential = 'Business classification is Residential.'
    Unknown = 'Business classification is unknown.'


class MBM_8_5_is_linear_function_of_output(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the energy consumption for the Site a linear function of output?'
    # I presume there's a formula to determine this. What's the formula?


class fixed_energy_consumption_can_be_measured(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Can the fixed energy consumption, which is the consumption of the' \
            'Site that does not vary with variations in output, be measured?'


class fixed_energy_consumption_can_be_estimated(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Can the fixed energy consumption, which is the consumption of the' \
            'Site that does not vary with variations in output, be estimated?'


class variation_in_output_changed_by_more_than_50_percent(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Has the variation in output over the variable energy baseline' \
            ' measurement period changed by more than 50%?'

    def formula(buildings, period, parameters):
        current_output = buildings('MBM_current_output', period)
        average_output = buildings('MBM_average_output', period)
        percentage_increase = ((current_output - average_output) / average_output * 100)
        percentage_decrease = ((average_output - current_output) / average_output * 100)
        percentage_increase_more_than_50_percent = (percentage_increase > 50)
        percentage_decrease_more_than_50_percent = (percentage_decrease > 50)
        return (percentage_increase_more_than_50_percent + percentage_decrease_more_than_50_percent)
