# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
import numpy as np


class number_of_certificates(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Equation 1 of the ESS Rule 2009, used to calculate the number' \
            ' of ESCs generated from a Recognised Energy Savings Activity.' \
            ' As defined in Clause 6.5 of the ESS Rule 2009.'

    def formula(buildings, period, parameters):
        elec_savings = buildings('electricity_savings', period)
        elec_cert_conversion_factor = parameters(period).general_ESS.electricity_certificate_conversion_factor
        gas_savings = buildings('gas_savings', period)
        gas_cert_conversion_factor = parameters(period).general_ESS.gas_certificate_conversion_factor
        return np.floor((elec_savings * elec_cert_conversion_factor) + (gas_savings * gas_cert_conversion_factor))


class electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Electricity savings created from implementation.'


class gas_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'gas savings created from implementation.'


class ESC_creation_date(Variable):
    value_type = date
    entity = Building
    definition_period = ETERNITY
    label = 'What is the date on which ESCs are registered and created?'


class ESC_created_on_or_after_1_July_2009(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Were the ESCs created on or after 1 July 2009?'

    def formula(buildings, period, parameters):
        ESC_creation_date = buildings('ESC_creation_date', period)
        ESS_commencement_date = np.datetime64('2009-01-07')
        return where((ESC_creation_date >= ESS_commencement_date), True, False)
