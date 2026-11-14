from datascience import *
ice=Table().with_columns(
    'Flavour',make_array('strawbery','choclate','strawbery','vennila'),
    'Price',make_array(40,88,88,77))
rat=Table().with_columns(
    'kind',make_array('strawbery','choclate','vennila'),
    'stars',make_array(22,33,44)
)
rated=ice.join('Flavour',rat,'kind')
rated



